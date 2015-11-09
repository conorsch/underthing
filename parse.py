import csv

filename = 'Data.csv'

with open(filename, 'rU') as datafile:
    sewer_reader = csv.reader(datafile, delimiter=',')
    for row in sewer_reader:
        print(', '.join(row))
