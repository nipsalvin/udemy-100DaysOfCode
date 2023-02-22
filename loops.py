# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
height_length = 0
for x in student_heights:
    height_length += 1
# print(height_length)

sum_of_heights = 0
for i in student_heights:
    sum_of_heights += i
# print(sum_of_heights)

avg = round(sum_of_heights/height_length)
print(avg)
