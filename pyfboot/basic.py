'''
This module contain the class for
building a 4diac project as an fboot file.\n
Copyright (c) 2017 Aimirim STI.\n
## Dependencies are:
* lxml
'''

# Import system libs
import os
from lxml import etree as ET

# Import custom libs
from pyfboot.typelibrary.templates import FB

#######################################

class Project:
    ''' Creates a 4diac Project. Calling
    `Project.initialize()` is mandatory before 
    adding blocks and `Project.finalize()` must be 
    called before `Project.write_to_file`.\n
    '''

    # --------------------
    def __init__(self):

        self.Res = 'EMB_RES'
        self.ID = 1

        self.fbootlist = []
    # --------------------

    # --------------------
    def create_fb(self, fb:FB):
        ''' Insert a new function block to be
        executed.\n
        `fb` (templates.FB): An instance of the FB 
        class such as the ones in `pyfboot.typelibrary`.\n
        return `fbname` (str): The name of the function 
        block added to the project. This name is needed 
        to connect data and events to this block in the future.\n
        '''
        self.ID+=1
        
        fbtype = fb.get_fb_type()
        fbname = fbtype+f'_{self.ID}'

        blk = ET.Element('Request')
        blk.set('ID',f'{self.ID}')
        blk.set('Action','CREATE')
        blk_fb = ET.SubElement(blk,'FB')
        blk_fb.set('Name',fbname)
        blk_fb.set('Type',fbtype)

        self.fbootlist.append(self._fbootline(blk))

        static_inputs = fb.get_inputs()
        for key,value in static_inputs.items():
            self.ID+=1
            blk = ET.Element('Request')
            blk.set('ID',f'{self.ID}')
            blk.set('Action','WRITE')
            blk_conn = ET.SubElement(blk,'Connection')
            blk_conn.set('Source',value)
            blk_conn.set('Destination',fbname+f'.{key}')
            
            self.fbootlist.append(self._fbootline(blk))
        
        return(fbname)
    # --------------------

    # --------------------
    def create_connection(self, conn:dict):
        ''' Insert a new data or event connection to the project.\n
        `conn` (dict): Dictionary of the form `{'FROM':str,'TO':str}`
        with the data or events to connect.\n
        '''
        self.ID+=1

        blk = ET.Element('Request')
        blk.set('ID',f'{self.ID}')
        blk.set('Action','CREATE')
        blk_conn = ET.SubElement(blk,'Connection')
        blk_conn.set('Source',conn['FROM'])
        blk_conn.set('Destination',conn['TO'])

        self.fbootlist.append(self._fbootline(blk))        
    # --------------------

    # --------------------
    def _fbootline(self, req:ET.Element, first:bool=False):
        ''' Export xml element as a line to fboot file.\n
        `req` (etree.Element): Xml tree element to transform.\n
        `first` (bool) Flag to insert resource.\n
        return `line` (str): Fboot line to file.\n
        '''
        line = ET.tostring(req,encoding='unicode',xml_declaration=None)
        line = ';'+line

        if (not first):
            line = self.Res+line
        
        line = line+'\n'
        return(line)
    # --------------------

    # --------------------
    def initialize(self):
        ''' Mandatory method to call before any `create`
        method. This inserts the Embeded Resource line that must
        exist as the file header.\n
        '''
        self.ID+=1

        blk = ET.Element('Request')
        blk.set('ID',f'{self.ID}')
        blk.set('Action','CREATE')
        blk_fb = ET.SubElement(blk,'FB')
        blk_fb.set('Name',self.Res)
        blk_fb.set('Type','EMB_RES')
        
        self.fbootlist.append(self._fbootline(blk,True))
    # --------------------

    # --------------------
    def finish(self):
        ''' Mandatory method to call before `write_to_file`.
        This will insert the `START` command at the end of
        the fboot file to signal forte the begining of it's 
        execution.\n
        '''
        
        blk = ET.Element('Request')
        blk.set('ID',f'{self.ID}')
        blk.set('Action','START')
        
        self.fbootlist.append(self._fbootline(blk))
    # --------------------

    # --------------------
    def write_to_file(self, filepath:str, overwrite:bool=False):
        ''' Export the 4diac Project into an `fboot` file. \n
        `filepath` (str): Path to save the fboot file into.\n
        `overwrite` (bool): Overwrite file if it already exists.\n
        #### Warning: This must be called AFTER the `finish` method
        otherwise the forte won't begin the project execution.
        '''

        # Separate path
        folder,filename = os.path.split(filepath)

        # Check if folder needs creation
        if (folder!='' and not os.path.exists(folder)):
            print(f'WARNING: Folder "{folder}" do not exist, creating ...')
            os.makedirs(folder,exist_ok=True)
        
        # Check file
        if(os.path.exists(filepath) and not overwrite):
            print(f'WARNING: File "{filename}" already exists, skiping ...')
        else:
            # Write fboot
            with open(filepath,'w') as fboot:
                fboot.writelines(self.fbootlist)
    # --------------------