# Setup
### Installation
The Fastsim model relies on python version 3.7. It is recommended to build and install everything within a conda environment. 
Once inside the conda environment run `pip install -r requirements.txt`. This will install all of the dependancies required for the application.

### Config.py and .env
The Config.py requires the package `python-dotenv`. In the root level of the application a `.env` file will need to be created like this:
```
GOOGLE_MAPS_KEY=[GOOGLE_MAPS_API_KEY]
WEATHER_KEY=[OPEN WEATHER API KEY]
TRAFFIC_KEY=[TOMTOM API KEY]
```
See the documentation on `python-dotenv` for more details. 