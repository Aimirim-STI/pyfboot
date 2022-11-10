'''
This module implements the `E_CYCLE`
function block.\n
Copyright (c) 2017 Aimirim STI.\n
'''

# Import custom libs
from pyfboot.typelibrary.templates import FB

#######################################

class CycleFB(FB):

    # --------------------
    def __init__(self, time_ms:int):
        ''' Cycle block to generate Request events
        over time.\n
        `time_ms` (int): Time in miliseconds.\n
        '''
        self.time = time_ms 
    # --------------------

    # --------------------
    def get_fb_type(self):
        ''' Mount the FB name string.\n
        '''
        return("E_CYCLE")
    # --------------------

    # --------------------
    def get_inputs(self):
        ''' Mount the inputs \n
        '''
        inp = {
            'DT':f'T#{self.time}ms'
        }
        return(inp)
    # --------------------