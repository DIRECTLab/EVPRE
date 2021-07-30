import sys
sys.path.append("range_estimator")
from RangeEstimator import RangeEstimator
from config import Config

range_estimator = RangeEstimator(Config())
graph = range_estimator.get_dataframe_from_graph()
print(graph[1].head())