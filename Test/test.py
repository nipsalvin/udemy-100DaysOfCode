import random
names = ['Alex', 'Beth', 'Carol', 'Dave', 'Elanor', 'Freddie']

student_scores = {student:random.randint(1,100) for student in names}
print (f'Student Scores : {student_scores}')

# passed_students = {{new_key:new_value} for (key:value) in dict.items() if test}
passed_students = {key:value for (key,value) in student_scores.items() if value > 50}
print(f'Passed Students : {passed_students}')