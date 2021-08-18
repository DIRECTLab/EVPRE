import networkx as nx
import osmnx as ox
import geopandas as gpd
import numpy as np
from ipyleaflet import *
from shapely.geometry import LineString, mapping
from simple_energy_model import ev_energy_model
from fastsim_model import fastsim_energy_model
from weather import get_weather_data


class RouteEstimator:
    def __init__(self, config, graph=None):
        self.starting_coord = config.starting_coord
        self.google_maps_key = config.google_maps_key
        self.weather_key = config.weather_key
        self.distance = config.distance
        self.edge_weight = config.default_edge_weight

        # create an instance of the graph
        if(graph == None):
            self.create_graph()
        else:
            self.graph = graph
            self.nodes, self.edges =  ox.graph_to_gdfs(self.graph)
        
        # create path layer list
        self.path_layer_list = []

        if config.model == "FASTSIM":
            # Fastsim model
            print("JITing model, please wait...")
            self.vehicle = fastsim_energy_model(
                config.fastsim_vehicle_csv_path, config.fastsim_vehicle_csv_index)
        else:
            # default simple energy model vehicle
            self.vehicle = ev_energy_model(
                config.default_ev_model['mass'], config.default_ev_model['air_resistance'], config.default_ev_model['area'])

        # create the map from ipyleaflet
        self.m = Map(center=self.starting_coord,
                     basemap=basemaps.CartoDB.Positron, zoom=15)

    def create_map(self):
        # create the TO marker style
        to_marker_style = AwesomeIcon(
            name='circle', icon_color='white', marker_color='red', spin=False)
        # create the two markers
        from_marker = Marker(location=self.starting_coord)
        to_marker = Marker(location=self.starting_coord, icon=to_marker_style)

        from_marker.observe(lambda event: self.handle_change_location(
            event, to_marker), 'location')
        to_marker.observe(lambda event: self.handle_change_location(
            event, from_marker), 'location')
        self.m.add_layer(from_marker)
        self.m.add_layer(to_marker)
        self.set_nearest_node(from_marker)
        self.set_nearest_node(to_marker)
        return self.m

    def create_graph(self):
        graph = ox.graph_from_point(
            self.starting_coord, self.distance, network_type="drive")
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
        event_owner.nearest_node = ox.get_nearest_node(
            self.graph, event_owner.location)
        marker.neares_node = ox.get_nearest_node(self.graph, marker.location)
        shortest_path = nx.bellman_ford_path(
            self.graph, event_owner.nearest_node, marker.neares_node, weight=self.edge_weight)

        if len(self.path_layer_list) == 1:
            self.m.remove_layer(self.path_layer_list[0])
            self.path_layer_list.pop()

        shortest_path_points = self.nodes.loc[shortest_path]
        path = gpd.GeoDataFrame(
            [LineString(shortest_path_points.geometry.values)], columns=['geometry'])
        path_layer = GeoData(geo_dataframe=path, style={
                             'color': 'black', 'weight': 2})
        self.m.add_layer(path_layer)
        self.path_layer_list.append(path_layer)

    def set_nearest_node(self, marker):
        marker.nearest_node = ox.distance.nearest_nodes(
            self.graph, marker.location[0], marker.location[1])
        return

    def activate_energy_model(self):
        if isinstance(self.vehicle, ev_energy_model):
            self.__activate_simple_energy_model()
        elif isinstance(self.vehicle, fastsim_energy_model):
            self.__activate_fastsim_energy_model()

    def __activate_fastsim_energy_model(self):
        # get a dataframe version of the graph to modify
        graphDF = self.get_dataframe_from_graph()

        # placeholder list for new column on the graph
        energy_consumed = []

        # For each row, grab the required value, compute the energy, and add to the energy list
        for index, row in graphDF[1].iterrows():
            speed_mps = row['speed_kph'] / 3.6
            grade = row['grade']
            length = row['length']
            energy_consumption = self.vehicle.get_consumed_kwh_fastsim(
                speed_mps, grade, length)
            energy_consumed.append(energy_consumption)

        # create a new column on the graphDF
        graphDF[1]['fastsim_model_e'] = energy_consumed

        # convert df back into graph and assign modified graph to self.graph
        self.graph = ox.graph_from_gdfs(graphDF[0], graphDF[1])

        # update the node, edges objects
        self.nodes, self.edges = ox.graph_to_gdfs(self.graph)

        # update the map mode to do shortest path based on the simple energy model
        self.edge_weight = 'fastsim_model_e'

    def __activate_simple_energy_model(self):
        # get a dataframe version of the graph to modify
        graphDF = self.get_dataframe_from_graph()

        # placeholder list for new column on the graph
        energy_consumed = []

        # get the starting wind and wind bearing for the energy consumption model
        current_weather = get_weather_data(
            self.starting_coord[0], self.starting_coord[1], self.weather_key)

        # For each row, grab the required value, compute the energy, and add to the energy list
        for index, row in graphDF[1].iterrows():
            speed = row['speed_kph']
            bearing = row['bearing']
            grade = row['grade']
            length = row['length']
            wind_speed = current_weather['wind_speed']
            wind_heading = current_weather['wind_heading']
            energy_consumption = self.vehicle.energy_consumption(
                grade, speed/3.6, 0, wind_speed, car_heading=bearing, wind_h=wind_heading, length=length)
            energy_consumed.append(energy_consumption)

        # create a new column on the graphDF
        graphDF[1]['simple_model_e'] = energy_consumed

        # convert df back into graph and assign modified graph to self.graph
        self.graph = ox.graph_from_gdfs(graphDF[0], graphDF[1])

        # update the node, edges objects
        self.nodes, self.edges = ox.graph_to_gdfs(self.graph)

        # update the map mode to do shortest path based on the simple energy model
        self.edge_weight = 'simple_model_e'
