from dotenv import load_dotenv
import pathlib
import os

SIMPLEMODEL = "SIMPLE"
FASTSIMMODEL = "FASTSIM"


class Config:

    def __init__(self, model=SIMPLEMODEL):
        load_dotenv()

        # Model selection--------------------------------------
        if model == SIMPLEMODEL or model == FASTSIMMODEL:
            self.model = model
        else:
            print("Invalid model selected, defaulting to simple model")
            self.model = SIMPLEMODEL

        # Map and Graph Configuration------------------------
        self.starting_coord = (41.740563, -111.813910)
        self.distance = 250000
        self.default_edge_weight = "length"

        # API keys--------------------------------------------
        self.google_maps_key = os.getenv("GOOGLE_MAPS_KEY")
        self.weather_key = os.getenv("WEATHER_KEY")
        self.traffic_key = os.getenv("TRAFFIC_KEY")

        # Simple energy model configuration--------------------
        # see simple_energy_model.py for details

        # default is based on ford focus
        self.default_ev_model = {"mass": 1337,
                                 "air_resistance": 0.28,
                                 "area": 1.825 * 1.469}

        # FASTSim energy model configuration-------------------
        # see fastsim_model.py for details

        # The location for the CSV that holds the fastsim vehicle data
        self.fastsim_vehicle_csv_path = str(
            list(pathlib.Path(os.getcwd()).rglob('*fastsim_focus.csv'))[0])

        # The index of the vehicle in the CSV, 1 indexed
        self.fastsim_vehicle_csv_index = 1
