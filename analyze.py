""" analyze the data and export as csv, then graph """

# imports
import os

import matplotlib.pyplot as plt
import numpy as np
import csv

# define where dataset is located
csvFile = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(
    __file__)), os.pardir)) + '/climate-change-neural-network/data/N_seaice_extent_daily_v3_raw.csv'
csvFile2 = os.path.abspath(os.path.join(os.path.dirname(
    os.path.realpath(__file__)), os.pardir)) + '/climate-change-neural-network/data/8443970_meantrend.csv'

# decide if averaging or not
averaging = False

# read data
with open(csvFile) as data:
    parsedData = csv.reader(data)
    seaIceAverages = []
    seaIceAverageDifferences = []
    if averaging == True:
        lastYear = 0
        yearSum = 0
        years = []
        for row in parsedData:
            if (row[0] == lastYear):  # if we are in the same year, add it to the sum
                yearSum = yearSum + float(row[3])
                lastYear = row[0]
            else:  # if we are in a new year, start a new sum
                seaIceAverages.append(yearSum / 365)
                # find difference between last year and this
                if not seaIceAverages[len(seaIceAverages) - 1]:
                    seaIceAverageDifferences.append(yearSum / 365)
                else:
                    seaIceAverageDifferences.append((yearSum / 365) - seaIceAverages[len(seaIceAverages) - 2])
                years.append(lastYear)
                yearSum = 0
                lastYear = row[0]
    else: # not averaging the data by year
        lastMonth = 0
        monthSum = 0
        for row in parsedData:
            if row[1] == lastMonth:
                monthSum = monthSum + float(row[3])
                lastMonth = row[1]
            else:
                seaIceAverages.append(monthSum / 31)
                # find difference between last year and this
                if not seaIceAverages[len(seaIceAverages) - 1]:
                    seaIceAverageDifferences.append(monthSum / 31)
                else:
                    seaIceAverageDifferences.append((monthSum / 31) - seaIceAverages[len(seaIceAverages) - 2])
                monthSum = 0
                lastMonth = row[1]

with open(csvFile2) as data:
    parsedData = csv.reader(data)
    seaLevelAverageDifferences = []
    lastYear2 = 0
    yearSum2 = 0
    years2 = []
    if averaging == True:
        for row in parsedData:
            if (int(row[0]) < 1977): # skip old data
                pass
            elif (row[0] == lastYear2):  # if we are in the same year, add it to the sum
                yearSum2 = yearSum2 + float(row[4])
                lastYear2 = row[0]
            else:  # if we are in a new year, start a new sum
                seaLevelAverageDifferences.append(yearSum2 / 12)
                years2.append(lastYear2)
                yearSum2 = 0
                lastYear2 = row[0]
    else:
        for row in parsedData:
            if (int(row[0]) < 1979):  # skip old data
                pass
            else:
                seaLevelAverageDifferences.append(float(row[4]))

# write new data
with open("output.csv", "w", newline='') as csvFile:
    writer = csv.writer(csvFile, delimiter=',')
    if averaging == True:
        finalData = zip(years[11:], seaIceAverageDifferences[12:], seaLevelAverageDifferences[78:])
    else:
        finalData = zip(seaIceAverageDifferences, seaLevelAverageDifferences)
    writer.writerows(finalData)

# plot
if averaging == True:
    plt.scatter(years[12:], seaIceAverageDifferences[12:])
    plt.scatter(years2[78:], seaLevelAverageDifferences[78:])
    plt.show()
