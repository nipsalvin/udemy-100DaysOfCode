from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)

title = Label(text='Timer', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, 'bold'))
title.grid(row=0, column=1)

canvas = Canvas(width=220, height=240, bg=YELLOW, highlightthickness= 0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(103, 112, image = tomato_img)
canvas.create_text(103, 130,text='00:00' ,fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(row=1, column=1)

start = Button(text='Start')
start.grid(row=2, column=0)

reset = Button(text='Reset')
reset.grid(row=2, column=2)

check_box = Label(text='✓', fg=GREEN, bg=YELLOW)
check_box.grid(row=3, column=1)


window.mainloop()


