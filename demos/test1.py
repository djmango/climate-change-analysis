# modules
import pandas as pd
from sklearn import linear_model
import matplotlib.pyplot as plt
import csv
import os
import numpy

# consts
current_dir = os.path.dirname(os.path.realpath(__file__))
project_dir = os.path.abspath(os.path.join(current_dir, os.pardir))

csv = pd.read_csv(project_dir + '\\data\\N_seaice_extent_daily_v3.csv')
print(list(csv))

# line of best fit
x = csv['Year']
y = csv['Extent']

x = x.values.reshape((len(x), -1))
y = y.values.reshape((len(y), -1))

pred = linear_model.LinearRegression()
pred.fit(x, y)

#visualize results
plt.scatter(x, y)
plt.plot(x, pred.predict(x))
plt.show()