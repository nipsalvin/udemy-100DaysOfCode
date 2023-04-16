student_dict = {
    "students": ["Harry", "Ron", "Hermione", "Draco", "Neville"] ,
    "scores":[41, 78, 99, 74, 62]
}
# print(student_dict) 

#Looping through a dictionary using FOR-Loop
# for (key, value) in student_dict.items():
#     print(value)

import pandas
student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

#Looping through a DATAFRAME
for (key, value) in student_data_frame.items():
    print(value)

#Looping through rows of a DATAFRAME
for (index, row) in student_data_frame.iterrows():
    # print(row.scores)
    if row.scores >= 50:
        print (row.students)






