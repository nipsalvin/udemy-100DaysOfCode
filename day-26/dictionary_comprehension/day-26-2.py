# TODO: Create a dictionary with word as key and length as value {word:len}
"""Method 1"""
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆
# Write your code below:
word_list = sentence.split()
result = {word:len(word) for word in word_list}
print(result)


"""Method 2"""
sentence2 = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆
# Write your code below:
result = {word:len(word) for word in sentence2.split()}
print(result)