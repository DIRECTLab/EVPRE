from dotenv import load_dotenv
import pathlib
import os

SIMPLEMODEL = "SIMPLE"
FASTSIMMODEL = "FASTSIM"

# The index of the vehicle in the fastsim_vehicles.csv, 1 indexed
# 1: 2012 Ford Focus Electric
# 2: 2016 CHEVROLET Spark EV
# 3: 2016 Leaf 24 kWh
# 4: 2016 Nissan Leaf 30 kWh

FORDFOCUSELECTRIC2012 = {
    "fastsimIndex": 1,
    "kwh": 23,
    "mass": 1337,
    "air_resistance": 0.28,
    "area": 2.24
}

CHEVSPARK2016 = {
    "fastsimIndex": 2,
    "kwh": 21,
    "mass": 1028,
    "air_resistance": 0.32,
    "area": 1.96
}

NISSANLEAF24KWH2016 = {
    "fastsimIndex": 3,
    "kwh": 24,
    "mass": 1477,
    "air_resistance": 0.28,
    "area": 2.28
}

NISSANLEAF30KWH2016 = {
    "fastsimIndex": 4,
    "kwh": 30,
    "mass": 1516,
    "air_resistance": 0.28,
    "area": 2.28
}


class Config:

    def __init__(self, model=SIMPLEMODEL, vehicle_config_dict=FORDFOCUSELECTRIC2012):
        load_dotenv()
        self.vehicle_config = vehicle_config_dict

        # Model selection--------------------------------------
        if model == SIMPLEMODEL or model == FASTSIMMODEL:
            self.model = model
        else:
            print("Invalid model selected, defaulting to simple model")
            self.model = SIMPLEMODEL

        # Map and Graph Configuration------------------------
        self.starting_coord = (41.740563, -111.813910)
        # May need to increase for full range estimate
        self.distance = 20000
        self.default_edge_weight = "length"

        # API keys--------------------------------------------
        self.google_maps_key = os.getenv("GOOGLE_MAPS_KEY")
        self.weather_key = os.getenv("WEATHER_KEY")
        self.traffic_key = os.getenv("TRAFFIC_KEY")

        # Simple energy model configuration--------------------
        # see simple_energy_model.py for details

        # default is based on ford focus
        # self.default_ev_model = {"mass": 1337,
        #                          "air_resistance": 0.28,
        #                          "area": 1.825 * 1.469}

        # FASTSim energy model configuration-------------------
        # see fastsim_vehicles.py for details

        # The location for the CSV that holds the fastsim vehicle data
        self.fastsim_vehicle_csv_path = str(
            list(pathlib.Path(os.getcwd()).rglob('*fastsim_vehicles.csv'))[0])

        self.fastsim_vehicle_csv_index = vehicle_config_dict["fastsimIndex"]
