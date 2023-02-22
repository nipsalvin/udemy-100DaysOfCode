# 🚨 Don't change the code below 👇
# unhash this👇
# student_scores = input("Input a list of student scores ").split()
student_scores = [78, 65, 89, 86, 55, 91, 64, 89]
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
highest = 0
ms = 0
for score in student_scores:
    highest = score
    if highest > ms:
        ms = highest
print(ms)


