'''
This module contains the abstract class
that is the base of all 4diac function blocks.\n
Copyright (c) 2017 Aimirim STI.\n
'''

#######################################

class FB:
    ''' Abstract class as template to 
    any function block.\n
    '''
    
    dquotes = '\"'

    # --------------------
    def __init__(self):
        raise NotImplementedError()
    # --------------------
    
    # --------------------
    def get_fb_type(self):
        ''' Mount the FB name string.\n
        '''
        raise NotImplementedError()
    # --------------------

    # --------------------
    def get_inputs(self):
        ''' Mount the inputs \n
        '''
        raise NotImplementedError()
    # --------------------