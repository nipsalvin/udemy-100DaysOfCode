# TODO 1: Open weather_data.csv and contents to an empty list

# data = []

# with open("./weather_data.csv") as data_file:
#     tempurature = data_file.readlines()
#     for temps in tempurature:
#         final_temp = temps.split()
#         data.append(final_temp)
#     print (data)

import csv

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    tempurature = []
    for row in data:
        # print(row)
        if row[1] != 'temp':
            tempurature.append(int(row[1]))
    # print(tempurature)


import pandas

data = pandas.read_csv("weather_data.csv")
print(data)
print(data['temp'])