# imports
import os

import matplotlib.pyplot as plt
import mpl_toolkits
import numpy as np
import pandas as pd
import seaborn as sns

# define where dataset is located
csvFile = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(
    __file__)), os.pardir)) + '/data/N_seaice_extent_daily_v3_small.csv'

# read data
data = pd.read_csv(csvFile)

# plot
plt.scatter(data["Year"], data["Extent"])
plt.title('Extent of sea ice')
plt.xlabel('Year')
plt.ylabel('Extent')
sns.despine

plt.show()