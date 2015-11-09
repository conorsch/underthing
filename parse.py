import csv
import numpy as np
import matplotlib.pyplot as plt


filename = 'Data.csv'
sewer_data = []


def read_csv_file():
    sewer_data_condensed = []
    with open(filename, 'rU') as datafile:
        sewer_reader = csv.reader(datafile, delimiter=',')
        for row in sewer_reader:
            sewer_data.append(row)
            dow, tod, fr = row
            sewer_data_condensed.append([ ((float(dow) - 1) * 24) + float(tod), fr ])

    return sewer_data_condensed

sewer_data_condensed = read_csv_file()

times_of_day = np.array([ np.float(d[0]) for d in sewer_data_condensed ])
flow_rates = np.array([ np.float(d[1]) for d in sewer_data_condensed ])

coefficients = np.polyfit(times_of_day, flow_rates, 50)
estimate = np.poly1d(coefficients)

for i in range(0, 10):
    x = np.linspace(0, 24 * 7, 10)
    _ = plt.plot(x, estimate(x))


_ = plt.scatter(times_of_day, flow_rates)

plt.show()

