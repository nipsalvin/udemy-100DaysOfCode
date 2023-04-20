import tkinter

def button_clicked():
    """
    This function is for changing the text in the label. You can use either 
    `my_label['text'] = 'I got clicked'` or `my_label.config(text='I got clicked')`
    """
    my_label['text'] = 'I got clicked'
    my_label.config(text='I got clicked')
    new_text =input.get()
    my_label.config(text = new_text)

window = tkinter.Tk()
window.title('My First GUI Program')
window.minsize(width=500, height=300)

        # Label
my_label = tkinter.Label(text="This is a Label", font=("Times New Roman", 24, 'bold'))
# my_label.pack()
# pack() function Places object on the screen and centers it unless side is specified eg my_label.pack(side='left')
my_label.grid(row=0, column=0)

my_label['text'] = 'This is a dictionary label'
my_label.config(text='This is a config label')
my_label.config(padx=20, pady=20)

        # Button
button = tkinter.Button(text='Click Me', command=button_clicked)
# button.pack()
button.grid(row=1, column=1)

        # New Button
button_2 = tkinter.Button(text='New Button')
button_2.grid(row=0, column=2)

        # Entry(input)
input = tkinter.Entry(width=10)
# input.pack()
input.grid(row=3, column=3)



window.mainloop()
"""window.mainloop() keeps the window open using a loop"""