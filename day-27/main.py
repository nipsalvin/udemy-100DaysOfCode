import tkinter

window = tkinter.Tk()
window.title('My First GUI Program')
window.minsize(width=500, height=300)

        # Label
my_label = tkinter.Label(text="This is a Label", font=("Times New Roman", 24, 'bold'))
my_label.pack()
# pack() function Places object on the screen and centers it

my_label['text'] = 'This is a dictionary label'
my_label.config(text='This is a config label')

        # Button
def button_clicked():
    my_label['text'] = 'I got clicked'
    my_label.config(text='I got clicked')
    new_text =input.get()
    my_label.config(text = new_text)

button = tkinter.Button(text='Click Me', command=button_clicked)
button.pack()

        # Entry(input)
input = tkinter.Entry(width=10)
input.pack()



window.mainloop()
"""window.mainloop() keeps the window open using a loop"""