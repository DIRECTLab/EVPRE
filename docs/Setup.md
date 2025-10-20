# Setup
The various pieces of software that the Electric Vehicle Range Prediction Project uses are in python.  In order to run this, the machine running it must have python version 3.10.  In the next few sections we will be going over all dependencies that the software requires and how to install them. You should also make a `.env` file in the root directory of this project containing the API keys. 

## Auto-Installation
It is recommended to build and install everything within a conda environment with python=3.10. Once inside the conda environment run `pip install -r requirements.txt`. This will install all of the dependancies required for the application except for Fiona, gdal, and FASTSim. Please refer to [Fiona Installation](#fiona-installation), [GDAL Installation](#gdal-installation), and [FASTSim](#fastsim-installation) to correctly install these packages. 

## Manual-Installation

### Jupyter Notebook Installation
Jupyter Notebook provides majority of the services that the software requires to run.  Jupyter Notebook has specially made map visualization that makes our software easy to use.  To get Jupyter Notebook, simply follow the install link down below.

[Juptyter Notebook Installer](https://jupyter.org/install.html) 

### Python Installation
The backbone of the project is built on Python, so it is crucial that all users wanting to run this must have it.  Python packages and instructions to install it can be found here in a link below.  Additionally, for Windows users, you must set up environment variables in order for this to work.  An additional guide can be found below in a link as well.

[Python Installer](https://www.python.org/downloads/)
 
[Setting Up Enviorment Variables on Windows](https://www.tutorialspoint.com/python/python_environment.htm) 

### Pip Installation
In order to install dependencies, we must install pip.  pip is the standard package manager for Python. It allows you to install and manage additional packages that are not part of the Python standard library.  Instructions on how to install and set up pip can be found in a link below.

[pip Installer](https://pip.pypa.io/en/stable/installation/)

[More information on pip](https://realpython.com/what-is-pip/) 

### GDAL Installation
Now that pip is installed, we must install GDAL.  GDAL is a python library that provides a way to install vector and geospatial packages and library.  Almost every package from here on out will be under this categrory, so it is essential to install.  To install simply use conda-forge so that it will handle all underlying libraries. `conda install -c conda-forge gdal`

[More information on GDAL](https://gdal.org) 

### Fiona Installation
Fiona is GDAL's vector API for Python programmers.  Fiona is essentially an extension to GDAL, so it is also required to install the rest of the dependancies. To install simply use conda-forge so that it will handle all underlying libraries. `conda install -c conda-forge fiona`

[More information on Fiona](https://pypi.org/project/fiona/#:~:text=Fiona%20is%20GDAL)

### OSMNX Installation
Osmnx is talked about in the dependencies section.  If you want more information on it, reference that.  However, if you want to install it, run the following command 'pip install osmnx'

[Installation](https://osmnx.readthedocs.io/en/stable/) 

### Geopandas Installation
Geopandas is talked about in the dependencies section.  If you want more information on it, reference that.  However, if you want to install it, run the following command 'pip install geopandas'

[Geopandas Installer](https://geopandas.org/getting_started/install.html) 

### python-dotenv Installation
Python-Dotenv is used to load enviornment variables.  To us this means that we will simply load our API keys.  If you want more information, API keys are talked about in a section below.  However, if you want to install it, run the following command 'pip install python-dotenv'

[Python-dotenv Installer](https://pypi.org/project/python-dotenv/) 

### Ipyleaflet Installation
Ipyleaflet is talked about in the dependencies section.  If you want more information on it, reference that.  However, if you want to install it, run the following command 'pip install ipyleaflet'

[Ipyleaflet Installer](https://ipyleaflet.readthedocs.io/en/latest/installation.html) 

### FASTSim Installation
For information of what FASTSim is, then click here to go to the Dependencies report: [FASTSim](./Dependencies.md). If you want to install it, then you are going to need to have the Rust toolchain and the FASTSim Github repo cloned. Once both have been installed, then in the terminal run `sh build_and_test.sh` inside of the FASTSim repo to install FASTSim and test all of its depenedencies.

[FASTSim Github](https://github.com/NREL/fastsim)

[Rust Toolchain](https://rust-lang.org/tools/install/)

[More Information on FASTSim](https://www.nrel.gov/transportation/data-tools.html) 
