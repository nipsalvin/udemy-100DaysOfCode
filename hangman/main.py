import random
import hangman_art
import hangman_words

#Update the word list to use the 'word_list' from hangman_words.py
#Delete this line: word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

#Import the logo from hangman_art.py and print it at the start of the game.
print(hangman_art.logo)
print(hangman_art.stages[0])

#Testing code
#print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"
print(display)
while not end_of_game:
    
    guess = input("Guess a letter: ").lower()

    #If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
        print(f'You have already guessed {guess}')
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"position: {position}\n letter: {letter}\n guess: {guess})
        if letter == guess:
            display[position] = letter
    #Check if user is wrong.
    if guess not in chosen_word:
        #If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        print(f'You chose {guess} and it is not in the chosen word')
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
            print(f"The word was {chosen_word}")
    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #Import the stages from hangman_art.py and make this error go away.
    print(hangman_art.stages[lives])
