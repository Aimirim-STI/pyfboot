# Forte Fboot Generator library
Create projects for 4diac-Forte programatically by writing it's `fboot` file.

## Installing for usage
To use this there are basically two types of install, one use a

#### Using a virtual enviroment
Create the enviroment
``` sh
$ python3.8 -m venv .venv
$ source .venv/bin/activate
```
Install the library
``` sh
$ pip install ssh://git@aimirimsti.ddns.net:3022/application_eng/data-collector/pyfboot.git
```

#### Using a conda
Crete the conda enviroment
``` sh
$ conda create -n my_project python=3.8
$ conda activate my_project
```
Install the library
``` sh
$ pip install ssh://git@aimirimsti.ddns.net:3022/application_eng/data-collector/pyfboot.git
```

## Installing for development
To start developtin in this project, just clone this git repository.
``` sh
$ git clone https://aimirimsti.ddns.net/gitlab/application_eng/data-collector/pyfboot
```
Go into the `pyfboot` folder and create and activate the virtual environment
``` sh
$ python3.8 -m venv .venv
$ source .venv/bin/activate
```
Install it directly by the library folder
``` sh
$ pip install .
```
