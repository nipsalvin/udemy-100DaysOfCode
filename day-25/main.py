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
# print(data_dict['day'][0])

"""Converting data to list"""
temp_list = data['temp'].to_list()
# print(sum(temp_list))

"""Finding average"""
average_temp = data['temp'].mean()
# print(average_temp)

"""Finding max value"""
max_temp = data['temp'].max()
# print(max_temp)

"""Method 2 of getting a row"""
cond = data.condition
# print(f'The rows are\n {cond}')
temp = data.temp
# print(f'The temps are\n{temp}')
monday = data[data.day == 'Monday']
# print(monday.condition)
data['fahrenheit'] = (monday.temp * 1.8) + 32
monday_fahrenheit = int((monday.temp * 1.8) + 32)
# print(monday_fahrenheit)

"""Getting data from a row"""
data_row = data[data.day == 'Monday']
# print(data_row)

max_temp_row = data[data.temp == data.temp.max()]
# print(f'Max Temp row is \n{max_temp_row}')

"""Creating new dataframe (Table)"""
data_dict_2 = {
    "students": ["Amy", "James", "Angela"],
    "scores": [17, 56, 65]
}

data_2 = pandas.DataFrame(data_dict_2)
# print(data_dict_2)
data_2.to_csv("new_data.csv")
data_3 = pandas.read_csv("new_data.csv")
print(data_3)

