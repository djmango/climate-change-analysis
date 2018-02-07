import csv
import numpy as np
from sklearn.svm import SVR
import matplotlib.pyplot as plt
import os

# plt.switch_backend('svg')

current_dir = os.path.dirname(os.path.realpath(__file__))
project_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
csvf = project_dir + '\\data\\N_seaice_extent_daily_v3.csv'

dates = []
values = []


def get_data(filename):
    with open(csvf, 'r') as csvfile:
        csvFileReader = csv.reader(csvfile)
        next(csvFileReader)  # skipping column names
        for row in csvFileReader:
            # this is incorrect, 0 is year 1 is month 2 is day
            dates.append(int(row[0]))
            values.append(float(row[3]))
    return


def predict_price(dates, values, x):
    dates = np.reshape(dates, (len(dates), 1))  # converting to matrix of n X 1

    svr_lin = SVR(kernel='linear', C=1e3)
    svr_poly = SVR(kernel='poly', C=1e3, degree=2)
    # defining the support vector regression models
    svr_rbf = SVR(kernel='rbf', C=1e3, gamma=0.1)
    svr_rbf.fit(dates, values)  # fitting the data points in the models
    svr_lin.fit(dates, values)
    svr_poly.fit(dates, values)

    # plotting the initial datapoints
    plt.scatter(dates, values, color='black', label='Data')
    # plotting the line made by the RBF kernel
    plt.plot(dates, svr_rbf.predict(dates), color='red', label='RBF model')
    # plotting the line made by linear kernel
    plt.plot(dates, svr_lin.predict(dates),
             color='green', label='Linear model')
    # plotting the line made by polynomial kernel
    plt.plot(dates, svr_poly.predict(dates),
             color='blue', label='Polynomial model')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('Support Vector Regression')
    plt.legend()
    plt.show()

    return svr_rbf.predict(x)[0], svr_lin.predict(x)[0], svr_poly.predict(x)[0]


get_data('aapl.csv')  # calling get_data method by passing the csv file to it
# print "Dates- ", dates
# print "Prices- ", values

predicted_price = predict_price(dates, values, 29)
