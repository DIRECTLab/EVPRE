from route_estimator import RouteEstimator, models, weather, traffic
from range_estimator import RangeEstimator
from config import Config

route_estimator_length = RouteEstimator(Config())

route_map = route_estimator_length.create_map()
route_map