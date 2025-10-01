#!/usr/bin/env python
# coding: utf-8

# # Route Estimator
# This software is to help predict the most energy optimized path between two destinations. The default method for computing shortest path can be changed in the `config.py`. The current example edge weight is based on length to show functionality of the markers. There are two provided models that can be applied to the graph to compute an energy consumption estimate. The weight mode can then be changed accordingly.

# In[1]:


from route_estimator import RouteEstimator, models, weather, traffic
from range_estimator import RangeEstimator
from config import Config


#  To get started you will need an instance of the RouteEstimator object created with the config file. You will need to setup the config file to include api keys.

# In[2]:


route_estimator_length = RouteEstimator(Config())


# ## Example of the Default Map

# In[3]:


route_map = route_estimator_length.create_map()
route_map


#  ## Example of Simple Energy Model
#  Requires: Google Maps API Key, Open Weather API Key

# In[4]:


simple_model_config = Config()
route_estimator_simple_model = RouteEstimator(simple_model_config, graph=route_estimator_length.get_graph())
route_estimator_simple_model.activate_energy_model()
route_map_simple_e = route_estimator_simple_model.create_map()
route_map_simple_e


# ## Example of Isochrone

# In[5]:


range_estimator_simple_model = RangeEstimator(simple_model_config, route_estimator_simple_model.get_graph())
range_estimator_simple_model.generate_isochrone(simple_model_config.vehicle_config["kwh"])


#  ## Example of FASTSim Energy Model
#  Requires: Google Maps API Key, Open Weather API Key
# 
#  Note: FASTSim calculations may take a few minutes

# In[6]:
fastsim_config = Config("FASTSIM")
route_estimator_fastsim_model = RouteEstimator(fastsim_config, graph=route_estimator_length.get_graph())
route_estimator_fastsim_model.activate_energy_model()
route_map_fastsim_e = route_estimator_fastsim_model.create_map()
route_map_fastsim_e

# In[ ]:




