""" convert the daily csv data to yearly averages and export as csv """

# imports
import os

import matplotlib.pyplot as plt
import numpy as np
import csv

# define where dataset is located
csvFile = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(
    __file__)), os.pardir)) + '/data/N_seaice_extent_daily_v3_raw.csv'

# read data
with open(csvFile) as data:
    parsedData = csv.reader(data)
    lastYear = 0
    yearSum = 0
    years = []
    averages = []
    i = 0
    for row in parsedData:
        i = i + 1
        if (row[0] == lastYear): # if we are in the same year, add it to the sum
            yearSum = yearSum + float(row[3])
            lastYear = row[0]
        else: # if we are in a new year, start a new sum
            averages.append(yearSum / 365)
            years.append(lastYear)
            yearSum = 0
            lastYear = row[0]

# write new data
with open("output.csv", "w", newline='') as csvFile:
        writer = csv.writer(csvFile, delimiter=',')
        finalData = zip(years[11:], averages[11:])
        writer.writerows(finalData)

# plot
plt.scatter(years[11:], averages[11:])
plt.show()
