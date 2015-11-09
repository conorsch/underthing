import csv
import numpy as np
import matplotlib.pyplot as plt


filename = 'Data.csv'


def read_csv_file(condensed=False):
    sewer_data_condensed = []
    sewer_data = []
    with open(filename, 'rU') as datafile:
        sewer_reader = csv.reader(datafile, delimiter=',')
        for row in sewer_reader:
            sewer_data.append(row)
            dow, tod, fr = row
            sewer_data_condensed.append([ ((float(dow) - 1) * 24) + float(tod), fr ])
    if condensed:
        return sewer_data_condensed
    else:
        return sewer_data


def get_weekly_rhythm():
    sewer_data_condensed = read_csv_file(condensed=True)
    times_of_day = np.array([ np.float(d[0]) for d in sewer_data_condensed ])
    flow_rates = np.array([ np.float(d[1]) for d in sewer_data_condensed ])
    coefficients = np.polyfit(times_of_day, flow_rates, 50)
    estimate = np.poly1d(coefficients)
    for i in range(0, 10):
        x = np.linspace(0, 24 * 7, 10)
        _ = plt.plot(x, estimate(x))
    _ = plt.scatter(times_of_day, flow_rates)
    plt.show()


def get_daily_rhythm():
    sewer_data = read_csv_file()
    times_of_day = np.array([ np.float(d[1]) for d in sewer_data ])
    flow_rates = np.array([ np.float(d[2]) for d in sewer_data ])
    coefficients = np.polyfit(times_of_day, flow_rates, 30)
    estimate = np.poly1d(coefficients)
    for i in range(0, 10):
        x = np.linspace(0, 24, 10000)
        _ = plt.plot(x, estimate(x))
    _ = plt.scatter(times_of_day, flow_rates)
    plt.show()


#get_weekly_rhythm()
get_daily_rhythm()
