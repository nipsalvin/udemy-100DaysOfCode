import pandas

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format: {"A": "Alfa", "B": "Bravo"}
data = pandas.read_csv('nato_phonetic_alphabet.csv')
phonetic_dict ={row.letter:row.code for (index, row) in data.iterrows()}
# print(phonetic_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter your name: \n").upper()
output_list = [phonetic_dict[letter] for letter in word]
print(output_list)
# data_dict = {row.letter:row.code for (index, row) in data.iterrows() if row.letter in word_list}
# print(data_dict)