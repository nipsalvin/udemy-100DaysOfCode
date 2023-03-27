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
# print(data)
# print(data['temp'])

"""Converting to dictionary"""
data_dict = data.to_dict()
print(data_dict['day'][0])

"""Converting data to list"""
temp_list = data['temp'].to_list()
print(sum(temp_list))

"""Finding average"""
average_temp = data['temp'].mean()
print(average_temp)

"""Finding max value"""
max_temp = data['temp'].max()
print(max_temp)

"""Method 2 of getting a row"""
cond = data.condition
print(f'The rows are\n {cond}')
temp = data.temp
print(f'The temps are\n{temp}')

"""Getting data from a row"""
data_row = data[data.day == 'Monday']
print(data_row)

max_temp_row = data[data.temp == data.temp.max()]
print(f'Max Temp row is \n{max_temp_row}')
