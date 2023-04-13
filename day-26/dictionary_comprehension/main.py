import random
names = ['Alex', 'Beth', 'Carol', 'Dave', 'Elanor', 'Freddie']

student_scores = {student:random.randint(1,100) for student in names}
print (student_scores)

passed_students = {student:score for (student, score) in student_scores.items() if score >= 60}
print(passed_students)