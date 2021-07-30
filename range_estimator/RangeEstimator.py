import networkx as nx
import osmnx as ox
import geopandas as gpd
import numpy as np
import folium


class RangeEstimator:

    def __init__(self, config):
        self.starting_coord = config.starting_coord
        self.google_maps_key = config.google_maps_key


    def display_map(self):
        map = folium.Map(location=self.starting_coord)
        map.add_child(folium.ClickForMarker(popup="Waypoint"))
        map.save("range_map.html")



