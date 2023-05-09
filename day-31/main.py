from tkinter import *
import random
import pandas

BACKGROUND_COLOR = "#B1DDC6"

to_learn = {}
try:
    data = pandas.read_csv('./data/words_to_learn.csv')
except FileNotFoundError:
    original_data = pandas.read_csv('./data/french_words.csv')
    to_learn = original_data.to_dict(orient='records')
else:
    to_learn = data.to_dict(orient='records')
"""Method 2"""
# try:
#     data = pandas.read_csv('./data/words_to_learn.csv')
# except FileNotFoundError:
#     data = pandas.read_csv('./data/french_words.csv')
    
# to_learn = data.to_dict(orient='records')
"""End of method 2"""


current_card = {}

# ---------------------------- PICK A CARD ------------------------------- #

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    # print(data)
    canvas.itemconfig(card_title, text='French', fill='black')
    canvas.itemconfig(card_word, text=current_card['French'],fill='black')
    canvas.itemconfig(card_background, image=front_img)
    flip_timer=window.after(3000, flip_card)

# ------------------------------------------------------------------------ #

# ---------------------------- PICK A CARD ------------------------------- #

def flip_card():
    canvas.itemconfig(card_title, text='English', fill='White')
    canvas.itemconfig(card_word, text=current_card['English'], fill='White')
    canvas.itemconfig(card_background, image=back_img)

# ------------------------------------------------------------------------ #

# ---------------------------- POPULATE CSV------------------------------- #

def is_known():
    to_learn.remove(current_card)
    data_frame = pandas.DataFrame(to_learn)
    data_frame.to_csv('./data/words_to_learn.csv', index=False)
    next_card()


# ------------------------------------------------------------------------ #
window = Tk()
window.title('Flashy')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

canvas = Canvas(width=800, height=526)
front_img = PhotoImage(file='./images/card_front.png')
back_img = PhotoImage(file='./images/card_back.png')

card_background= canvas.create_image(400, 263, image = front_img) #set image at center of canvas (1/2X, 1/2Y)
canvas.config(bg= BACKGROUND_COLOR, highlightthickness=0)
card_title = canvas.create_text(400, 100, text='', font=('ariel', 20, 'italic'))
card_word = canvas.create_text(400, 263, text='', font=('TimesNewRoman', 30, 'bold'))
canvas.grid(row=0, column=0, columnspan=2)

wrong_img = PhotoImage(file='./images/wrong.png')
wrong_button = Button(image=wrong_img, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

right_img = PhotoImage(file='./images/right.png')
right_button = Button(image=right_img, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=1)


next_card()

window.mainloop()
