'''
This module implements the `S7_RD_` and 
`SNAP7_RD_` familly of function blocks\n
Copyright (c) 2017 Aimirim STI.\n
'''

# Import custom libs
from pyfboot.typelibrary.comm_templates import CommunicationFB

#######################################

class SiemensFB(CommunicationFB):
    ''' Implementation of Siemens Communication
    Function Block
    '''

    # --------------------
    def _is_old_plc(self):
        ''' Check PLC model.\n
        return `is_it` (bool): True when models older than S7-1200.\n
        '''
        is_it = int(self.PARAM_target.split('S7')[-1]) < 1200
        return(is_it)
    # --------------------

    # --------------------
    def parse_params(self, dsource:dict, dpoint:dict):
        ''' Parameters input to protocol\n
        '''

        self.PARAM_ip = dsource['ip']
        self.PARAM_port = dsource['port']
        self.PARAM_address = dpoint['address']

        self.PARAM_target = dsource['protocol']['con_type'].upper()
        self.PARAM_rack = dsource['protocol']['rack']
        self.PARAM_slot = dsource['protocol']['slot']

        if (self._is_old_plc()):
            self.PROTOCOL = 'S7'
        else:
            self.PROTOCOL = 'SNAP7'
    # --------------------

    # --------------------
    def get_comm_string(self):
        ''' Mount the communication string for this protocol\n
        return `comm` (str): Joined parameters formated in a string.\n
        '''

        head = f"{self.PARAM_ip}{self.sep}{self.PARAM_port}{self.sep}{self.pooltime}{self.sep}"
        tail = f"{self.PARAM_rack}{self.sep}{self.PARAM_slot}{self.sep}{self.timeout}{self.sep}{self.PARAM_address}"

        if (self._is_old_plc()):
            comm = head + f"{self.PARAM_target}{self.sep}" + tail
        else:
            comm = head + tail
        
        return(comm)
    # --------------------
