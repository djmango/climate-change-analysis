""" make a prediction and export to csv """

# imports
import os

import matplotlib.pyplot as plt
import numpy as np
import csv

# read data
data = pd.read_csv(csvFile)

# define where dataset is located
csvFile = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(
    __file__)), os.pardir)) + '/data/N_seaice_extent_daily_v3_raw.csv'

def predict(year):