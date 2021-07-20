import csv

data = []
with open("tz_opendata_z01012021_po01072021.csv", encoding='utf-8') as csvfile:
    spamreader = csv.reader(csvfile)
    for row in spamreader:
        print(row)