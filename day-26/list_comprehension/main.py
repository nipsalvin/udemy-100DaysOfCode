# TODO: Write a code to compare numbers from file1.txt and file2.txt and print out numbers that are commont in both
with open("file1.txt") as file1:
    data_1 = file1.readlines()
with open("file2.txt") as file2:
    data_2 = file2.readlines()

result = []
result = [int(num) for num in data_1 if num in  data_2]

# Write your code above 👆

print(result)


