# Setup
## Installation
The Fastsim model relies on python version 3.7. It is recommended to build and install everything within a conda environment. 
Once inside the conda environment run `pip install -r requirements.txt`. This will install all of the dependancies required for the application.

## Config.py and .env
The Config.py requires the package `python-dotenv`. In the root level of the application a `.env` file will need to be created with the following variables:

```
GOOGLE_MAPS_KEY=[GOOGLE MAPS ELEVATION API KEY]
WEATHER_KEY=[OPEN WEATHER API KEY]
TRAFFIC_KEY=[TOMTOM API KEY]
```
See the documentation on `python-dotenv` for more details. 

# Prodecdure

## Jupyter Notebook

A [sample Jupyter notebook (main.ipynb)](main.ipynb) is included to show example usage of the EVPRE software.

## Configuration

To configure the EVPRE software, modify [config.py](config.py) with the relevant vehicle and environment data.

See the [models README.md](route_estimator/models/README.md) for more information on each model and its parameters.

## EVPRE Usage

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