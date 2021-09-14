# Electric Vehicle Range Prediction Project
### Table of Contents

- [EVPRE Configuration and Usage](#EVPRE-Configuration-and-Usage)
- [Dependencies Summary](https://github.com/DIRECTLab/EVPRE/blob/development/docs/Dependencies.md)
---

# Software Description
The Electric Vehicle Range Prediction Project is a piece of software that uses various services and data to make route predictions based on energy consumption.




## Running the Software
Now that all dependencies have been downloaded, simply navigate to where the code is saved, use your favorite shell and run 'jupyter notebook'.  This will open up a web browser with all the code to run.




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

## Installation
To install all of the required packages:
`pip install -r requirements.txt`

To install fastsim:
Navigate to the directory that contains the fastsim source code. Run `pip install .` to install it to your pip.

After everything is installed, run `jupyter-lab` in the root directory of the application. This should open a jupyter notebook. The main examples are in `main.ipynb`.
