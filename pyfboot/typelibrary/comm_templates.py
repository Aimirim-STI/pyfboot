'''
This module extends the FB class
to a new template for Communication
Blocks.\n
Copyright (c) 2017 Aimirim STI.\n
'''

# Import custom libs
from pyfboot.typelibrary.templates import FB
from pyfboot.typelibrary.types import CommType, NumType

#######################################

class CommunicationFB(FB):

    PROTOCOL=None

    # --------------------
    def __init__(self, timeout:int=2000, a_type:str=CommType.READ, n_type:dict=NumType.REAL):
        ''' Communication protocol initialization.\n
        `timeout` (int): Read/Write operation timeouts. Defaults
        to 2000ms.\n
        `a_type` (str): The action type to be done. Can be one of 
        `CommType.READ` and `CommType.WRITE`\n
        `n_type` (dict): The Numeric type to expect. Can be one of 
        `NumType` members, such as `NumType.REAL`\n
        '''
        # Parameter separator
        self.sep = ":"
        # Set pooling time (only dummy)
        self.pooltime = 1000
        
        # Set response timeout
        self.timeout = timeout

        # Set default parameters
        self.a_type = a_type
        self.n_type = n_type
    # --------------------

    # --------------------
    def get_fb_type(self):
        ''' Mount the FB name string.\n
        return `name` (str): Function block name.\n
        '''
        name = f"{self.PROTOCOL}_{self.a_type}_{self.n_type}"
        return(name)
    # --------------------

    # --------------------
    def get_inputs(self):
        ''' Mount the input \n
        return `inp` (dict): \n
        '''
        inp = {
            'QI':'TRUE',
            'PARAMS':f'{self.dquotes}{self.get_comm_string()}{self.dquotes}'
        }
        return(inp)
    # --------------------

    # --------------------
    def parse_params(self, dsource:dict, dpoint:dict):
        ''' Parameters input to protocol\n
        `dsource` (dict): Data Source informations.\n
        `dpoint` (dict): Data Point informations.\n
        '''
        raise NotImplementedError()
    # --------------------

    # --------------------
    def get_comm_string(self):
        ''' Mount the communication string for this protocol\n
        return `comm` (str): Joined parameters formated in a string.\n
        '''
        raise NotImplementedError()
    # --------------------