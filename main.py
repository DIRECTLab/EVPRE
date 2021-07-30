import sys
sys.path.append("range_estimator")
from RangeEstimator import RangeEstimator
from config import Config

range_estimator = RangeEstimator(Config())
range_estimator.display_map()