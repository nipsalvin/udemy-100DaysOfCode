#TODO 1: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
PLACEHOLDER = '[name]'

with open("./Input/Names/invited_names.txt", mode= "r") as names_file:
    names = names_file.readlines()
        # print(name)
with open("./Input/Letters/starting_letter.txt", mode='r') as draft:
    letter_content = draft.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_content.replace(PLACEHOLDER, stripped_name)
        # print(new_letter)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode='w') as complete_letter:
            complete_letter.write(new_letter)