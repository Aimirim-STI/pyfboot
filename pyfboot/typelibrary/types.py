'''
This module creates a set of standard
types needed in the function block builds.\n
Copyright (c) 2017 Aimirim STI.\n
'''

#######################################

class CommType:
    READ = 'RD'
    WRITE = 'WR'

class NumType:
    BOOL = {'FB':'BOOL','OPC':'0:i=1' }
    INT  = {'FB':'INT' ,'OPC':'0:i=4' }
    DINT = {'FB':'DINT','OPC':'0:i=6' }
    REAL = {'FB':'REAL','OPC':'0:i=10'}