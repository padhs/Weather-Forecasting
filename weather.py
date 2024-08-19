# Time Series analysis of weather dataset from whylogs

import pandas as pd
import numpy as np


# Read dataset: we'll use in-domain baseline
path = './whylogs_data/weather_forecast/baseline_dataset_in_domain.csv'
df = pd.read_csv(path)


def evaluations(data_frame):
    # Head:
    print(data_frame.head(10))
    # Info:
    print(data_frame.info())
    # Shape:
    print(data_frame.shape)


evaluations(df)
