from tkinter import *
import random
import pandas

BACKGROUND_COLOR = "#B1DDC6"

data = pandas.read_csv('./data/french_words.csv')
to_learn = data.to_dict(orient='records')

# ---------------------------- SEARCH BUTTON ------------------------------- #

def next_word():
    current_card = random.choice(to_learn)
    # print(data)
    canvas.itemconfig(card_title, text='French')
    canvas.itemconfig(card_word, text=current_card['French'])

# -------------------------------------------------------------------------- #
window = Tk()
window.title('Flashy')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)
back_img = PhotoImage(file='./images/card_back.png')
front_img = PhotoImage(file='./images/card_front.png')

canvas.create_image(400, 263, image = front_img) #set image at center of canvas (1/2X, 1/2Y)
canvas.config(bg= BACKGROUND_COLOR, highlightthickness=0)
card_title = canvas.create_text(400, 100, text='', font=('ariel', 20, 'italic'))
card_word = canvas.create_text(400, 263, text='', font=('TimesNewRoman', 30, 'bold'))
canvas.grid(row=0, column=0, columnspan=2)

wrong_img = PhotoImage(file='./images/wrong.png')
wrong_button = Button(image=wrong_img, highlightthickness=0, command=next_word)
wrong_button.grid(row=1, column=0)

right_img = PhotoImage(file='./images/right.png')
right_button = Button(image=right_img, highlightthickness=0, command=next_word)
right_button.grid(row=1, column=1)


next_word()


window.mainloop()
