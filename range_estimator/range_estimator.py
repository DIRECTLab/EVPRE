import networkx as nx
import osmnx as ox
import geopandas as gpd
import numpy as np
from ipyleaflet import *
from shapely.geometry import LineString, mapping

class RangeEstimator:

    def __init__(self, config):
        self.starting_coord = config.starting_coord
        self.google_maps_key = config.google_maps_key
        self.distance = config.distance

        # create an instance of the graph
        self.create_graph()
        
        # create path layer list
        self.path_layer_list = []
        
        
        #create the map from ipyleaflet
        self.m = Map(center=self.starting_coord, basemap=basemaps.CartoDB.Positron, zoom=15)


    def create_map(self):
        # create the TO marker style
        to_marker_style = AwesomeIcon(name='circle',icon_color='white',marker_color='red',spin=False)
        #create the two markers
        from_marker = Marker(location=self.starting_coord)
        to_marker = Marker(location=self.starting_coord, icon=to_marker_style)
        
        from_marker.observe(lambda event: self.handle_change_location(event, to_marker), 'location')
        to_marker.observe(lambda event: self.handle_change_location(event, from_marker), 'location')
        self.m.add_layer(from_marker)
        self.m.add_layer(to_marker)
        self.set_nearest_node(from_marker)
        self.set_nearest_node(to_marker)
        return self.m


    def create_graph(self):
        graph = ox.graph_from_point(self.starting_coord, self.distance, network_type="drive")
        graph = ox.add_edge_speeds(graph)
        graph = ox.add_edge_bearings(graph)
        graph = ox.add_edge_travel_times(graph)
        graph = ox.add_node_elevations_google(graph, self.google_maps_key)
        graph = ox.add_edge_grades(graph)
        self.graph = graph
        # save a dataframe version of edges and nodes for event handler
        self.nodes, self.edges = ox.graph_to_gdfs(self.graph)

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
            
    def handle_change_location(self, event, marker):
        event_owner = event['owner']
        event_owner.nearest_node = ox.get_nearest_node(self.graph, event_owner.location)
        marker.neares_node = ox.get_nearest_node(self.graph, marker.location)
        shortest_path = nx.bellman_ford_path(self.graph, event_owner.nearest_node, marker.neares_node, weight='length')

        if len(self.path_layer_list) == 1:
            self.m.remove_layer(self.path_layer_list[0])
            self.path_layer_list.pop()

        shortest_path_points = self.nodes.loc[shortest_path]
        path = gpd.GeoDataFrame([LineString(shortest_path_points.geometry.values)], columns=['geometry'])
        path_layer = GeoData(geo_dataframe=path, style={'color':'black', 'weight':2})
        self.m.add_layer(path_layer)
        self.path_layer_list.append(path_layer)
        
    def set_nearest_node(self, marker):
        marker.nearest_node = ox.get_nearest_node(self.graph, marker.location)
        return