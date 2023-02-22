student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇
# 'student' gets dictionary key (names)
for student in student_scores:
    # score gets value (marks)
    score = student_scores[student]
    # print (score)
    if score > 90:
        score = "Outstanding"
    elif score > 80 and score <= 90:
        score = "Exceeds Expectations"
    elif score > 70 and score <= 80:
        score = "Acceptable"
    else:
        score = "Fail"
    student_grades[student] = score   
    

# 🚨 Don't change the code below 👇
print(student_grades)