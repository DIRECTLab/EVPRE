from dotenv import load_dotenv
import os
class Config:

    def __init__(self):
        load_dotenv()
        # Map and Graph Configuration
        self.starting_coord = (41.740563, -111.813910)
        self.distance = 50000
        self.default_edge_weight = "length"
        # API keys
        self.google_maps_key = os.getenv("GOOGLE_MAPS_KEY")
        self.weather_key = os.getenv("WEATHER_KEY")
        self.traffic_key = os.getenv("TRAFFIC_KEY")
