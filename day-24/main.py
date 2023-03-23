# with open("my_file.txt") as my_file:
#     content = my_file.read()
#     print(content)

with open("my_file_2.txt", mode='a') as file:
    file.write("This is a new text")
    content = file.read()
    print(content)

