from dotenv import load_dotenv
import os
class Config:

    def __init__(self):
        load_dotenv()
        self.starting_coord = (41.740563, -111.813910)
        self.google_maps_key = os.getenv("GOOGLE_MAPS_KEY")
        self.distance = 50000
