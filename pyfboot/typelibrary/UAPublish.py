'''
This module implements the `PUBLISH_1`
function blocks\n
Copyright (c) 2017 Aimirim STI.\n
'''

# Import custom libs
from pyfboot.typelibrary.templates import FB


#######################################

class Publish_1FB(FB):
    ''' Implementation of a variable insertion in
    OPCUA server
    '''
    PROTOCOL = 'opc_ua'

    # --------------------
    def __init__(self, var:str):
        ''' OPCUA variable publish initialization.\n
        `var` (str): Variable name. Must be unique.\n
        '''
        # Set variable name
        self.var = var
        # Default 
        self.a_type = 'WRITE'
        self.path = '/Objects'
        self.ns = 1
    # --------------------

    # --------------------
    def get_fb_type(self):
        ''' Mount the FB name string.\n
        '''
        return("PUBLISH_1")
    # --------------------
    
    # --------------------
    def get_inputs(self):
        ''' Mount the input \n
        return `inp` (dict): \n
        '''
        inp = {
            'QI':'TRUE',
            'ID':f'{self.dquotes}{self.get_comm_string()}{self.dquotes}'
        }
        return(inp)
    # --------------------

    # --------------------
    def get_comm_string(self):
        ''' Mount the communication string for this protocol\n
        '''
        comm = f"{self.PROTOCOL}[{self.a_type};{self.path}/"+ \
            f"{self.var},{self.ns}:s={self.var}]"
        return(comm)
    # --------------------