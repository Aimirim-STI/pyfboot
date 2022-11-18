'''
This module implements the `CIP_RD_` and 
`CIPDH_RD_` familly of function blocks.\n
Copyright (c) 2017 Aimirim STI.\n
'''

# Import custom libs
from pyfboot.typelibrary.comm_templates import CommunicationFB

#######################################

class CipFB(CommunicationFB):
    ''' Implementation of Cip Ethernet Communication
    Function Block
    '''

    # --------------------
    def _is_dhplus(self):
        ''' Check DH+ network.\n
        return `is_it` (bool): True when connecting though DH+ network.\n
        '''
        is_it = self.PARAM_conn == 'DH+'
        return(is_it)
    # --------------------

    # --------------------
    def parse_params(self, dsource:dict, dpoint:dict):
        ''' Parameters input to protocol\n
        '''
        
        self.PARAM_ip = dsource['ip']
        self.PARAM_port = dsource['port']
        self.PARAM_tag_name = dpoint['tag_name']

        self.PARAM_conn = dsource['protocol']['con_type']
        self.PARAM_path = dsource['protocol']['path']
        self.PARAM_slot = dsource['protocol']['slot']

        if (self._is_dhplus()):
            self.PROTOCOL = 'CIPDH'
        else:
            self.PROTOCOL = 'CIP'
    # --------------------

    # --------------------
    def get_comm_string(self):
        ''' Mount the communication string for this protocol\n
        return `comm` (str): Joined parameters formated in a string.\n
        '''
        comm = f"{self.PARAM_ip}{self.sep}{self.PARAM_port}{self.sep}"+ \
            f"{self.pooltime}{self.sep}{self.PARAM_path}{self.sep}"+ \
            f"{self.PARAM_slot}{self.sep}{self.timeout}{self.sep}{self.PARAM_tag_name}"
        return(comm)
    # --------------------