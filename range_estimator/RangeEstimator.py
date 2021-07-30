import networkx as nx
import osmnx as ox
import geopandas as gpd
import numpy as np
import folium


class RangeEstimator:

    def __init__(self, config):
        self.starting_coord = config.starting_coord
        self.google_maps_key = config.google_maps_key
        self.distance = config.distance

        self.create_graph()


    def display_map(self):
        map = folium.Map(location=self.starting_coord)
        map.add_child(folium.ClickForMarker(popup="Waypoint"))
        map.save("range_map.html")


    def create_graph(self):
        graph = ox.graph_from_point(self.starting_coord, self.distance, network_type="drive")
        graph = ox.add_edge_speeds(graph)
        graph = ox.add_edge_bearings(graph)
        graph = ox.add_edge_travel_times(graph)
        graph = ox.add_node_elevations_google(graph, self.google_maps_key)
        graph = ox.add_edge_grades(graph)
        self.graph = graph

    def get_graph(self):
        try:
            return self.graph
        except:
            print("Graph has not been created")

    def get_dataframe_from_graph(self):
        try:
            return ox.graph_to_gdfs(self.graph)
        except:
            print("Graph has not been created")