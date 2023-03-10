'''
This module contains the pre-built
gateway projects for 4diac forte application.\n
Copyright (c) 2017 Aimirim STI.\n
'''

# Import custom libs
from pyfboot.basic import Project
import pyfboot.typelibrary as tlib
from pyfboot.typelibrary.types import CommType, NumType

#######################################

class MonoGatewayProject:

    PROTOCOL_MAPPING = {
        'Siemens':tlib.SiemensFB,
        'Modbus':tlib.ModbusFB,
        'Rockwell':tlib.CipFB,
    }

    # --------------------
    def __init__(self, cycle_time:int=5000):
        ''' Creates a single OPCUA Gateway project for all
        DataSources and DataPoints.\n
        `cycle_time` (int): Time in miliseconds to execute the project cycle.
        Defaults to 5000ms or 5s.\n
        '''
        
        self.proj = Project()
        self.proj.initialize()

        e_cycle = tlib.CycleFB(cycle_time)
        self.cyclefb = self.proj.create_fb(e_cycle)

        self.lastfb = None
        self.Connections = []
    # --------------------

    # --------------------
    def build_comm_block(self, dsource:dict, dpoint:dict):
        ''' Selects and instanciate the correct communication
        function block for the desired Data Point.\n
        `dsource` (dict): Data Souce informations.\n
        `dpoint` (dict): Data Point informations.\n
        return `comfb` (typelibrary.CommunicationFB): The instance of the
        correct block to conect to the specified Data Point.\n
        '''

        fbclass = self.PROTOCOL_MAPPING[dsource['protocol']['name']]
        fbtype = getattr(NumType,dpoint['num_type'])
        comfb = fbclass(dsource['timeout'], CommType.READ, fbtype['FB'])
        comfb.parse_params(dsource, dpoint)
        
        return(comfb)
    # --------------------

    # --------------------
    def addVariable(self, var:str, comfb:tlib.CommunicationFB):
        ''' Insert a new variable in the gateway project. This will create
        both the block that reads from plc and the one that writes into
        the OPCUA server.\n
        `var` (str): Variable name to access in OPCUA.\n
        `comfb` (typelibrary.CommunicationFB): \n
        '''
        
        commfb = self.proj.create_fb(comfb)

        if (self.lastfb is None):
            self.Connections.append({'FROM':'START.COLD','TO':f'{commfb}.INIT'})
            self.Connections.append({'FROM':f'{self.cyclefb}.EO','TO':f'{commfb}.REQ'})
        else:
            self.Connections.append({'FROM':f'{self.lastfb}.INITO','TO':f'{commfb}.INIT'})
            self.Connections.append({'FROM':f'{self.lastfb}.CNF','TO':f'{commfb}.REQ'})

        uapub = tlib.Publish_1FB(var)

        uafb = self.proj.create_fb(uapub)
        self.Connections.append({'FROM':f'{commfb}.INITO','TO':f'{uafb}.INIT'})
        self.Connections.append({'FROM':f'{commfb}.CNF','TO':f'{uafb}.REQ'})
        self.Connections.append({'FROM':f'{commfb}.RD','TO':f'{uafb}.SD_1'})

        self.lastfb = uafb
    # --------------------

    # --------------------
    def _addObservers(self):
        ''' Insert the last blocks for observability
        and helthcheck \n
        '''

        stopwatchfb = self.proj.create_fb( tlib.SimplestFB('E_STOPWATCH') )
        time_convertfb = self.proj.create_fb( tlib.SimplestFB('F_TIME_IN_S_TO_LREAL') )
        uafb = self.proj.create_fb( tlib.Publish_1FB('_ForteCycleTime') )

        self.Connections.append({'FROM':f'{self.cyclefb}.EO','TO':f'{stopwatchfb}.START'})
        self.Connections.append({'FROM':f'{self.lastfb}.CNF','TO':f'{stopwatchfb}.STOP'})
        self.Connections.append({'FROM':f'{stopwatchfb}.TD','TO':f'{time_convertfb}.IN'})
        self.Connections.append({'FROM':f'{time_convertfb}.OUT','TO':f'{uafb}.SD_1'})

        self.Connections.append({'FROM':f'{self.lastfb}.INITO','TO':f'{uafb}.INIT'})
        self.Connections.append({'FROM':f'{stopwatchfb}.EO','TO':f'{time_convertfb}.REQ'})
        self.Connections.append({'FROM':f'{time_convertfb}.CNF','TO':f'{uafb}.REQ'})

        self.lastfb = uafb
    # --------------------

    # --------------------
    def write_fboot(self, filepath:str, overwrite:bool=True, **prot_opts):
        ''' Export the single gateway Project into an fboot file.\n
        `filepath` (str): ocal or remote path to save the fboot file into.\n
        `overwrite` (bool): Overwrite file if it already exists.\n
        `prot_opts`: Extra options that make sense to a particular
        prococol connection, e.g. host, port, username, etc..\n
        '''
        self._addObservers()

        self.Connections.append({'FROM':f'{self.lastfb}.INITO','TO':f'{self.cyclefb}.START'})

        for conn in self.Connections:
            self.proj.create_connection(conn)
        
        self.proj.finish()
        
        self.proj.write_to_file(filepath,overwrite,**prot_opts)
    # --------------------