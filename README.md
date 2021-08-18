# Electric Vehicle Range Prediction Project
### Table of Contents
- [Desciption](#Software-Desciption)
- [Dependencies](#Dependencies)
- [Setup](#Setup)
- [APIs](#apis-and-libraries)
- [EVPRE Configuration and Usage](#EVPRE-Configuration-and-Usage)
---

# Software Desciption
The Electric Vehicle Range Prediction Project is a piece of software that uses various services and data to make route predicitons.  These predictions are found using a machine learning algorithm that takes geospatial data and compiles it together to make route plans.


# Dependencies

### Numpy
NumPy is a python package for scientific computing.  NumPy provides many fast operations on arrays.  These operations include: mathematical manipulation, logical manipulation, shape manipulation, fast sorting, fast array selection, array insertion, array deletion, basic linear algebra, random population, and more.

*Need Desciption of what it does exactly in the software*

[More information on NumPy : https://numpy.org/doc/stable/user/whatisnumpy.html]

### Shapely
Shapely is a Python package that provides manipulation of geometric data.  Shapely has the ability to manipulate and shape geometric data in many ways.  Those ways being: Geometric operations, geometric manipulation, geometric formulas, etc.

*Need Desciption of what it does exactly in the software*

[More information on Shapely : https://shapely.readthedocs.io/en/stable/manual.html]

### Geopandas
Geopandas uses both pandas and shapely that provides a database for geospatial data, more options for geospatial data, and overall higher level performance.  Geopandas is an essential depenency for the map and visualization portion of this software.

*Need Desciption of what it does exactly in the software*

[More information on Geopandas : https://geopandas.org/about.html]

### Networkx
Networkx is a package in python that provides the ability to organize and structure complex networks.  Networkx provides the ability to organize and structure graphs, diagraphs, and multigraphs.  Additionally, it provides many different built in operations and algorithms.  This is essential for map and route planning due to how it provides essential functions and the ability to add and organize complex data on edges and nodes.

*Need Desciption of what it does exactly in the software*

[More information on NumPy : https://numpy.org/doc/stable/user/whatisnumpy.html]

### Osmnx
Osmnx is Python Package that provides the ability to downloasd geospatial data from OpenStreetMaps.  This is essential, due to OpenStreetMaps being the primary map and route provider.

*Need Desciption of what it does exactly in the software*

[More information on Osmnx : https://osmnx.readthedocs.io/en/stable/]

### Matplotlib
Matplotlib is a Python Library that helps create visualization for data.  It is a very powerful tool that can help draw out complex networks, graphs, charts and more.  It is essential for our software because it makes drawing a visual map simple and easy.

*Need Desciption of what it does exactly in the software*

[More information on Matplotlib : https://matplotlib.org/]

### Ipyleaflet
Ipleaflet is the primary map builder in the software.  Ipyleaflet is an interacive map builder and editor on jupyter notebook.  This gives the software the ability to make and edit maps with ease.

*Need Desciption of what it does exactly in the software*

[More information on Ipyleaflet : https://ipyleaflet.readthedocs.io/en/latest/#]

### Descrates
Descrates is an image data and function plotter.

*Need Desciption of what it does exactly in the software*

[More information on NumPy : https://pypi.org/project/descartes/]

###FastSim
FastSim is a simulation program that allows users to run simulations on vehicles and ranges.  There are many different variables to adjust and use to gather data.  It is extremely fast and accurate making it a very powerful tool for our software.

*Need Desciption of what it does exactly in the software*

[More information on NumPy : https://www.nrel.gov/transportation/fastsim.html]

---

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


## Running the Software
Now that all dependencies have been downloaded, simply navigate to where the code is saved, use your favorite shell and run 'jupyter notebook'.  This will open up a web browser with all the code to run.



# APIs and Libraries

In this section we'll go over some of the APIs that are used in various files throughout the project.

## Google Maps
Google Maps


## Folium
Folium is one of the most important APIs for map visualization. Folium is able to take points in the format of `(latitude,longitude)` and plot them on a map displayed in HTML. It is also possible to take two points and plot a line between them, or multiple points and plot what is called a PolyLine. It is also possible to add a marker to a set of coordinates, almost like a pin. Users are able to put custom text in markers as well that will show when clicked.

Folium maps can be generated using JavaScript or Python, and both options will provide an HTML file of a generated map as output.

The most current files in this project which use Folium are the ones which generate maps of the Electric Vehicle Test runs performed with three different vehicles. They can be found [here](data/data_visualization). `print_maps.py` is the file which runs Folium to generate the maps, and the maps themselves are in the `maps` directory found in that same location.

For more information about Folium and its use cases, check out these websites!

- [Folium Documentation (Python)](https://python-visualization.github.io/folium/index.html)
- [Folium Quickstart (from the Python documentation)](https://python-visualization.github.io/folium/quickstart.html)
- [Folium GitHub (with examples and more)](https://github.com/python-visualization/folium)

## OpenStreetMap

OpenStreetMap (OSM) is an API which allows map data to be both created by users as well as downloaded and used by users.

One of the most important uses of OpenStreetMap in this project is the ability to select a bounding box of some type, whether it be four coordinate pairs, or a single pair of coordinates and a radius, etc. and get the entire map as nodes and connecting paths between those nodes. Basically, when you get the map in this way, you are able to use it like a graph which has nodes and edges. In order to do this, a helpful Python package can be used called OSMnx. In testing, we used this package in a Jupyter Notebook in order to get data from OpenStreetMap and display a visual of the graph created from the data. To see this in action, log into the server and look at the `directions-with-osm-networkx` directory!

For our program, we take the data collected from the electric vehicle runs, and apply it to a machine learning algorithm which will allow us to generate edge-weights for each edge in one of these map graphs. In this way, we will be able to calculate our own routes from point A to point B without having to use existing APIs with predetermined route calculation such as "fastest route" or "shortest route." We might be able to generate the best route that passes through most electric vehicle charging stations, or the best route based on elevation gain / loss, etc. This flexibility will also allow us to generate multiple routes for one journey depending on how much leeway is allowed when sticking to a set of parameters that determine a "best route."

For more information, visit these sites!
- [OpenStreetMap API Wiki](https://wiki.openstreetmap.org/wiki/API_v0.6)
- [Interactive Map Example (using OSM and networkx)](https://medium.com/analytics-vidhya/interative-map-with-osm-directions-and-networkx-582c4f3435bc)
- [OSMnx User Reference Documentation](https://osmnx.readthedocs.io/en/stable/osmnx.html)


## OpenWeatherMap
OpenWeatherMap (OWM) is similar to OSM.  OWM provides current weather conditions and returns them in a nicely formated JSON file.  The API call that we use with OWM is based off coordinates.  The data in the JSON file is then extracted out and is given to the machine learning algorithm.

Below is a quick guide to the types of information our API provides:

	Functional Road Class. This indicates the road type:
		- temperature : Provides the current temperature in celsius
		- humidity : Provides the average humidity
		- visibility : provides visibility per meter
		- windSpeed : Returns the wind speed in meters/second

All the data provided above is then passed to the machine learning algorithm, which then calculates the best possible route based on the data.

- [OpenWeatherMap - Lite Documentation: https://openweathermap.org/current#data]
- [How Visibility is Measured: https://www.skybrary.aero/index.php/Visibility]

## TomTom Traffic API
Tom Tom is an open source company that provides many different services.  The service our program uses is for Traffic.  The major two things TomTom provides for us are Traffic Incident data and Traffic Flow data.

Below is a quick guide to the types of information our API provides:

	Functional Road Class. This indicates the road type:
	  - FRC0: Motorway, freeway or other major road
	  - FRC1: Major road, less important than a motorway
	  - FRC2: Other major road
	  - FRC3: Secondary road
	  - FRC4: Local connecting road
	  - FRC5: Local road of high importance
	  - FRC6: Local road
	
	  - currentSpeed : The current average speed at the selected point, in the unit requested.
	  - freeFlowSpeed : The free flow speed expected under ideal conditions, expressed in the unit requested.
	  - currentTravelTime : Current travel time in seconds based on fused real-time measurements between the defined locations in the specified direction.
	  - freeFlowTravelTim : The travel time in seconds which would be expected under ideal free flow conditions.
      - roadClosure : This indicates if the road is closed to traffic or not.
	  - coordinates : This includes the coordinates describing the shape of the segment.  Coordinates are shifted from the road depending on the zoom level to support high quality visualization in every scale.
	  
TomTom's Traffic API helps provide data that is then used with the route calculation algorithm.

- [TomTom Website - Documentation: https://developer.tomtom.com/traffic-api]

## Seaborn

Seaborn is a data visualization library used in Python which also can be accessed through an API. Datasets are able to be entered and then displayed in various different ways, such as in scatter plots, heatmaps, histograms, and more!

At the moment, our project uses Seaborn to visualize the correlation between different data items that can be tracked using an OBD tool connected to an Electric Vehicle. This can be seen running in a Jupyter Notebook [here](Jupyter_Notebooks). The file `View Database.ipynb` contains code which will pull vehicle data from the database, make a correlation matrix, and display that correlation matrix as a heatmap using Seaborn.

The website has extremely useful examples and a gallery of the available visualization options.

- [Seaborn Website / Documentation](https://seaborn.pydata.org/)


# EVPRE Configuration and Usage

### Config.py and .env
The Config.py requires the package `python-dotenv`. In the root level of the application a `.env` file will need to be created like this:
```
GOOGLE_MAPS_KEY=[GOOGLE MAPS ELEVATION API KEY]
WEATHER_KEY=[OPEN WEATHER API KEY]
TRAFFIC_KEY=[TOMTOM API KEY]
```
See the documentation on `python-dotenv` for more details. 

### Jupyter Notebook

A [sample Jupyter notebook (main.ipynb)](main.ipynb) is included to show example usage of the EVPRE software.

### EVPRE Configuration

To configure the EVPRE software, modify [config.py](config.py) with the relevant vehicle and environment data.

See the [models README.md](route_estimator/models/README.md) for more information on each model and its parameters.

### EVPRE Usage

For example, to utilize the simple energy model,

```
route_estimator_simple_model = RouteEstimator(Config())
route_estimator_simple_model.activate_energy_model()
route_map_simple_e = route_estimator_simple_model.create_map()
route_map_simple_e
```

Creates a map where a user can find the most efficient route between two markers.

To generate an isochrone with the given parameters,

```
range_estimator_simple_model = RangeEstimator(Config(), route_estimator_simple_model.get_graph())
range_estimator_simple_model.generate_isochrone()
```

## Energy and Vehicle Model Information
See the [models README.md](route_estimator/models/README.md)