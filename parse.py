import csv
import numpy as np
import matplotlib.pyplot as plt


filename = 'Data.csv'
sewer_data = []


sewer_data_condensed = []

with open(filename, 'rU') as datafile:
    sewer_reader = csv.reader(datafile, delimiter=',')
    for row in sewer_reader:
        sewer_data.append(row)
        dow, tod, fr = row
        sewer_data_condensed.append([ ((float(dow) - 1) * 24) + float(tod), fr ])


times_of_day = np.array([ np.float(d[0]) for d in sewer_data_condensed ])
flow_rates = np.array([ np.float(d[1]) for d in sewer_data_condensed ])

coefficients = np.polyfit(times_of_day, flow_rates, 10)
estimate = np.poly1d(coefficients)

x = np.linspace(0, 24, 1000)
_ = plt.plot(times_of_day, flow_rates, x, estimate(x))
plt.show()



