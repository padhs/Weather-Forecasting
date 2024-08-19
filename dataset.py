# Dataset downloaded from whylogs

from whylogs.datasets import Weather

# Load dataset
dataset_in = Weather(version='in_domain')  # same climate
dataset_out = Weather(version='out_domain')  # Different climates
