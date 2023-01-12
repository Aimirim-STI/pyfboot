'''
This module contains the database
mock in a json format to test 
the gateway project.\n
Copyright (c) 2017 Aimirim STI.\n
'''

#######################################

data_mock = {
    'DataSources':[
        {
        'name': 'Predio 23_1',
        'plc_ip': '193.30.10.10',
        'plc_port': '102',
        'protocol': {
            'name': 'Siemens',
            'data':{
                'plc': 'S7-300',
                'rack': 0,
                'slot': 1,
            }
        },
        'cycletime': 2000,
        'timeout': 5000,
        'DataPoints': [
            {
                'name': 'FT_PF02A1_1_1',
                'description': 'Alimentação MOB1',
                'num_type': 'REAL',
                'access':{
                    'name': 'Siemens',
                    'data':{
                        'address': 'DB101.DBD8'
                    }
                }
            },{
                'name': 'FT_PI2634AC_1',
                'description': 'Vazão de dosagem de ácido cítrico',
                'num_type': 'REAL',
                'access':{
                    'name': 'Siemens',
                    'data':{
                        'address': 'DB100.DBD148'
                    }
                }
            }
        ]
        },
        {
            'name': 'Predio 23_2',
            'plc_ip': '193.30.10.12',
            'plc_port': '102',
            'protocol': {
                'name': 'Siemens',
                'data':{
                    'plc': 'S7-1500',
                    'rack': 0,
                    'slot': 1,
                }
            },
            'cycletime': 3000,
            'timeout': 7000,
            'DataPoints': [
                {
                    'name': 'A07TT153',
                    'description': 'Medidor de Temperatura do tanque 07-TQI-153',
                    'num_type': 'INT',
                    'access':{
                        'name': 'Siemens',
                        'data':{
                            'address': 'DB101.DBW14'
                        }
                    }
                }
            ]
        },
    ],
}

