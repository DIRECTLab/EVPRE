# Setup
The various pieces of software that the Electric Vehicle Range Prediction Project uses are in python.  In order to run this, the machine running it must have python version 3.7.  In the next few sections we will be going over all dependencies that the software requires and how to install them.

## Auto-Installation
The Fastsim model relies on python version 3.7. It is recommended to build and install everything within a conda environment.
Once inside the conda environment run `pip install -r requirements.txt`. This will install all of the dependancies required for the application.

## Manual-Installation

### Jupyter Notebook Installation
Jupyter Notebook provides majority of the services that the software requires to run.  Jupyter Notebook has specially made map visualization that makes our software easy to use.  To get Jupyter Notebook, simply follow the install link down below.

[Installation : https://jupyter.org/install.html]

### Python Installation
The backbone of the project is built on Python, so it is crucial that all users wanting to run this must have it.  Python packages and instructions to install it can be found here in a link below.  Additionally, for Windows users, you must set up environment variables in order for this to work.  An additional guide can be found below in a link as well.

[Installing Python: https://www.python.org/downloads/]
[Setting Up Enviorment Variables on Windows : https://www.tutorialspoint.com/python/python_environment.htm]

### Pip Installation
In order to install dependencies, we must install pip.  pip is the standard package manager for Python. It allows you to install and manage additional packages that are not part of the Python standard library.  Instructions on how to install and set up pip can be found in a link below.

[Installing pip : https://pip.pypa.io/en/stable/installation/]
[More information on pip : https://realpython.com/what-is-pip/]

### GDAL Installation
Now that pip is installed, we must install GDAL.  GDAL is a python library that provides a way to install vector and geospatial packages and library.  Almost every package from here on out will be under this categrory, so it is essential to install.  To install, download the proper gdal package from the link down below.  Then navigate to the directory you downloaded it to and run the following command: 'pip install <path-to-file> 1.8.20-cp39-p39-win_amd64.whl'

[Installation  : https://www.lfd.uci.edu/~gohlke/pythonlibs/#gdal]
[More information on GDAL : https://gdal.org/]

### Fiona Installation
Fiona is GDAL's vector API for Python programmers.  Fiona is essentially an extension to GDAL, so it is also required to install the rest of the dependancies.  To install simply download the proper fiona package.  Once downloaded navigate to the folder you downloaded it to and run the following command 'pip install <path_to_download> Fiona-1.8.20-cp39-cp39-win_amd64.whl'

[Installation  : https://www.lfd.uci.edu/~gohlke/pythonlibs/#fiona]
[More information on Fiona : https://pypi.org/project/Fiona/#:~:text=Fiona%20is%20GDAL's%20neat,vector%20API%20for%20Python%20programmers.&text=It%20focuses%20on%20reading%20and,of%20classes%20specific%20to%20OGR.]

### OSMNX Installation
Osmnx is talked about in the dependencies section.  If you want more information on it, reference that.  However, if you want to install it, run the following command 'pip install osmnx'

[Installation : https://osmnx.readthedocs.io/en/stable/]

### Geopandas Installation
Geopandas is talked about in the dependencies section.  If you want more information on it, reference that.  However, if you want to install it, run the following command 'pip install geopandas'

[Installation : https://geopandas.org/getting_started/install.html]

### python-dotenv Installation
Python-Dotenv is used to load enviornment variables.  To us this means that we will simply load our API keys.  If you want more information, API keys are talked about in a section below.  However, if you want to install it, run the following command 'pip install python-dotenv'

[Installation : https://pypi.org/project/python-dotenv/]

### Ipyleaflet Installation
Ipyleaflet is talked about in the dependencies section.  If you want more information on it, reference that.  However, if you want to install it, run the following command 'pip install ipyleaflet'

[Installation : https://ipyleaflet.readthedocs.io/en/latest/installation.html]

### Fastism Installation
Fastism is talked about in the dependencies section.  If you want more information on it, reference that.  However, if you want to install it, download it from the
link down below.  Once downloaded, navigate to the directory and install it with the following command 'pip install <directory-to-fastsim> fastsim-2021a'

[Installation : https://ipyleaflet.readthedocs.io/en/latest/installation.html]
[More Information : https://www.nrel.gov/transportation/data-tools.html]
