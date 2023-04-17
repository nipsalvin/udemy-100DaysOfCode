import tkinter

window = tkinter.Tk()
window.title('My First GUI Program')
window.minsize(width=500, height=300)

# Label
my_label = tkinter.Label(text="This is a Label", font=("Times New Roman", 24, 'bold'))
my_label.pack(side='left')
# pack() function Places object on the screen and centers it



import turtle

tim = turtle.Turtle()
tim.write("Test")


window.mainloop()
"""window.mainloop() keeps the window open using a loop"""