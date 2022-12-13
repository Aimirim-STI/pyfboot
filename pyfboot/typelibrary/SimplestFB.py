'''
This module implements a very simple
generic function block with no presets.\n
Copyright (c) 2017 Aimirim STI.\n
'''

# Import custom libs
from pyfboot.typelibrary.templates import FB

#######################################

class SimplestFB(FB):

    # --------------------
    def __init__(self,typename:str):
        ''' Interface for simple FBs that have no preset input
        or initial configuration.\n
        '''
        self.typename = typename
    # --------------------

    # --------------------
    def get_fb_type(self):
        ''' Mount the FB name string.\n
        '''
        return(self.typename)
    # --------------------

    # --------------------
    def get_inputs(self):
        ''' Mount the inputs \n
        '''
        inp = {}
        return(inp)
    # --------------------