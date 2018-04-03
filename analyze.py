""" convert the daily csv data to yearly seaIceAverages and export as csv """

# imports
import os

import matplotlib.pyplot as plt
import numpy as np
import csv

# define where dataset is located
csvFile = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(
    __file__)), os.pardir)) + '/data/N_seaice_extent_daily_v3_raw.csv'
csvFile2 = os.path.abspath(os.path.join(os.path.dirname(
    os.path.realpath(__file__)), os.pardir)) + '/data/8443970_meantrend.csv'

# read data
with open(csvFile) as data:
    parsedData = csv.reader(data)
    lastYear = 0
    yearSum = 0
    years = []
    seaIceAverages = []
    for row in parsedData:
        if (row[0] == lastYear):  # if we are in the same year, add it to the sum
            yearSum = yearSum + float(row[3])
            lastYear = row[0]
        else:  # if we are in a new year, start a new sum
            seaIceAverages.append(yearSum / 365)
            years.append(lastYear)
            yearSum = 0
            lastYear = row[0]

with open(csvFile2) as data:
    parsedData = csv.reader(data)
    seaLevelAverages = []
    lastYear2 = 0
    yearSum2 = 0
    years2 = []
    for row in parsedData:
        if (row[0] == lastYear2):  # if we are in the same year, add it to the sum
            yearSum2 = yearSum2 + float(row[4])
            lastYear2 = row[0]
        else:  # if we are in a new year, start a new sum
            seaLevelAverages.append(yearSum2 / 12)
            years2.append(lastYear2)
            yearSum2 = 0
            lastYear2 = row[0]

# write new data
with open("output.csv", "w", newline='') as csvFile:
    writer = csv.writer(csvFile, delimiter=',')
    finalData = zip(years[11:], seaIceAverages[11:], seaLevelAverages[78:])
    writer.writerows(finalData)

# plot

plt.scatter(years[11:], seaIceAverages[11:])
plt.scatter(years2[78:], seaLevelAverages[78:])
plt.show()
