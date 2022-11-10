'''
This module holds tests to be executed
with `pytest` program.\n
Copyright (c) 2017 Aimirim STI.\n
## Dependencies are:
* pyfboot
* pytest
'''

# Import system libs
import os

# Import custom libs
from pyfboot.gateway import MonoGatewayProject
from . import data_mock

#######################################

# --------------------
def test_data_parser():
    ''' Loads a database mock (json file)
    and create the projects accourdingly.\n
    '''
    # Create the 4diac Gateway Project
    prj = MonoGatewayProject(cycle_time=5000)

    # Get DataSources
    for ds in data_mock['DataSources']:
        # Get all DataPoints in this DataSource
        for dp in ds['DataPoints']:
            # Create communication blocks and associate them with an OPC variable
            comFB = prj.build_comm_block(ds,dp)
            prj.addVariable(dp['name'],comFB)

    # Write project
    prj.write_fboot(f'test_data_parser.fboot',overwrite=True)
    
    # TODO: Actualy validate if the fboot file make sense
    assert os.path.exists(f'test_data_parser.fboot')
    
    # # NOTE: Comment the next line to validate the file in forte
    os.remove(f'test_data_parser.fboot')
# --------------------
