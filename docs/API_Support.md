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
