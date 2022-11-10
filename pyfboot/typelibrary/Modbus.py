'''
This module implements the `MB_RD_`
familly of function blocks.\n
Copyright (c) 2017 Aimirim STI.\n
'''

# Import custom libs
from pyfboot.typelibrary.comm_templates import CommunicationFB

#######################################

class ModbusFB(CommunicationFB):
    ''' Implementation of Modbus Ethernet Communication
    Function Block
    '''
    PROTOCOL = 'MB'
    
    # --------------------
    def parse_params(self, dsource:dict, dpoint:dict):
        ''' Parameters input to protocol\n
        '''

        self.PARAM_ip = dsource['ip']
        self.PARAM_port = dsource['port']
        self.PARAM_address = dpoint['address']
        
        self.PARAM_func_code = dpoint['func_code']
        self.PARAM_slave_id = dsource['protocol']['slave_id']
    # --------------------

    # --------------------
    def get_comm_string(self):
        ''' Mount the communication string for this protocol\n
        return `comm` (str): Joined parameters formated in a string.\n
        '''
        comm = f"{self.PARAM_ip}{self.sep}{self.PARAM_port}{self.sep}"+ \
            f"{self.pooltime}{self.sep}{self.PARAM_slave_id}{self.sep}"+ \
            f"{self.func_code}{self.sep}{self.PARAM_address}{self.sep}{self.timeout}"
        return(comm)
    # --------------------