import networkx as nx
import osmnx as ox
import matplotlib.pyplot as plt
from shapely.geometry import LineString, mapping, Point, Polygon
from shapely.ops import unary_union
import geopandas as gpd
import json
from ipyleaflet import *
from route_estimator import ev_energy_model
import numpy as np
from copy import copy
import math

class RangeEstimator:
    def __init__(self, config, graph=None):
        self.model = config.model
        if(graph != None):
            self.graph = graph
            self.starting_coord = config.starting_coord
            self.nodes, self.edges = ox.graph_to_gdfs(self.graph)
        else:
            self.starting_coord = config.starting_coord
            self.google_maps_key = config.google_maps_key
            self.weather_key = config.weather_key
            self.distance = config.distance
            self.edge_weight = config.default_edge_weight

            # create an instance of the graph
            self.create_graph()

        # create path layer list
        self.path_layer_list = []

        # default simple energy model vehicle
        self.vehicle = ev_energy_model(config.vehicle_config['mass'], config.vehicle_config['air_resistance'], config.vehicle_config['area'])

    def create_graph(self):
        graph = ox.graph_from_point(self.starting_coord, self.distance, network_type="drive")
        graph = ox.add_edge_speeds(graph)
        graph = ox.add_edge_bearings(graph)
        graph = ox.add_edge_travel_times(graph)
        graph = self.count_Google_API_calls(graph, self.google_maps_key)
        graph = ox.add_edge_grades(graph)
        self.graph = graph
        # save a dataframe version of edges and nodes for event handler
        self.nodes, self.edges = ox.graph_to_gdfs(self.graph)

        
    # This method is used to estimate the number of Google API calls needed to get elevation data
    def count_Google_API_calls(self, graph, google_API_key):
        num_nodes = len(graph.nodes)
        batch_size = 512
        total_calls = math.ceil(num_nodes / batch_size)
        print(f"Number of Google API calls needed for elevation data: {total_calls}")
        return ox.add_node_elevations_google(graph, google_API_key)


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
            
    def generate_isochrone(self, batterykWh, batterykWhPercentages = None, iso_colors = None):

        if batterykWhPercentages is None:
            if(self.model == "SIMPLE"):
                battery_capacity = batterykWh * 3600000
            else:
                battery_capacity = batterykWh
            levels = [battery_capacity*0.1, battery_capacity*0.2, battery_capacity*0.3, battery_capacity*0.4, battery_capacity*0.5, battery_capacity*0.6, battery_capacity*0.7, battery_capacity*0.8, battery_capacity*0.9, battery_capacity]
        else:
            if(self.model == "SIMPLE"):
                levels = [batterykWh * 3600000 * perc for perc in batterykWhPercentages]
            else:
                levels = [batterykWh * perc for perc in batterykWhPercentages]
            
        
        if iso_colors is None:
            iso_colors = ["#ff0000", "#fe4400", "#f86600", "#ee8200", "#df9b00", "#cdb200", "#b6c700", "#98db00", "#6fed00", "#00ff00"]
        node_colors = {}


        center_node = ox.distance.nearest_nodes(self.graph, self.starting_coord[0], self.starting_coord[1], return_dist=False)
        gdf_nodes = ox.graph_to_gdfs(self.graph, edges=False)
        x, y = gdf_nodes["geometry"].unary_union.centroid.xy
        center_node = ox.distance.nearest_nodes(self.graph, x[0], y[0])

        graphs = []

        for energy, color in zip(sorted(levels, reverse=True), iso_colors):
            subgraph = nx.ego_graph(self.graph, center_node, radius=energy, distance="energy_consumed")
            graphs.append(copy(subgraph))
            for node in subgraph.nodes():
                node_colors[node] = color
        nc = [node_colors[node] if node in node_colors else "#222222" for node in self.graph.nodes()]
        ec = nc.copy()

        isochrone_polys = []
        for energy in sorted(levels, reverse=True):
            if(self.model == "SIMPLE"):
                subgraph = nx.ego_graph(self.graph, center_node, radius=energy, distance="simple_model_e")
            else:
                subgraph = nx.ego_graph(self.graph, center_node, radius=energy, distance="fastsim_model_e")
            node_points = [Point((data["x"], data["y"])) for node, data in subgraph.nodes(data=True)]
            bounding_poly = unary_union(node_points).convex_hull
            isochrone_polys.append(bounding_poly)

        fig, ax = ox.plot_graph(
            self.graph, show=False, close=False, edge_color="#222222", edge_alpha=0.2, node_size=0, bgcolor='white'
        )

        gdf = gpd.GeoDataFrame(
            geometry=isochrone_polys,
            data={"color": iso_colors}
        )

        axes = gdf.plot(
            color=gdf["color"],
            alpha=0.4,
            edgecolor="none",
            zorder=-1,
        )

        # for polygon, fc in zip(isochrone_polys, iso_colors):
        #     patch = PolygonPatch(polygon, fc=fc, ec="none", alpha=0.4, zorder=-1)
        #     ax.add_patch(patch)
        plt.show()