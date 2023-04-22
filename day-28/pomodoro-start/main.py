from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN =5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer(): 
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text = '00:00')
    title_label.config(text='Timer', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, 'bold'))
    check_box.config(text='')
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    work_secs = WORK_MIN * 60
    short_break_secs = SHORT_BREAK_MIN * 60
    long_break_secs = LONG_BREAK_MIN * 60
    
    reps += 1
    if reps % 8 == 0:
        count_down(long_break_secs)
        title_label.config(text= 'Long Break', fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_secs)
        title_label.config(text= 'Short Break', fg=PINK)
    else:
        count_down(work_secs)
        title_label.config(text= 'Working', fg=GREEN)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f'0{count_sec}'
    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
    # print(count)
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ''
        work_sess = math.floor(reps/2)
        for _ in range(work_sess):
            marks += '✓'
        check_box.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)

title_label = Label(text='Timer', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, 'bold'))
title_label.grid(row=0, column=1)

canvas = Canvas(width=220, height=240, bg=YELLOW, highlightthickness= 0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(103, 112, image = tomato_img)
timer_text = canvas.create_text(103, 130,text='00:00' ,fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(row=1, column=1)

start = Button(text='Start', command=start_timer)
start.grid(row=2, column=0)

reset = Button(text='Reset', command=reset_timer)
reset.grid(row=2, column=2)

check_box = Label(fg=GREEN, bg=YELLOW)
check_box.grid(row=3, column=1)


window.mainloop()


