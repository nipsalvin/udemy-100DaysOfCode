from tkinter import *

def miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.60934
    result.config(text=f'{km}')

window = Tk()
window.title('Miles to Km Converter')
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

is_equal = Label(text="is equal to")
is_equal.grid(row=1, column=0)

miles_input = Entry(width=10)
miles_input.grid(row=0, column=1)

result = Label(text=0)
result.grid(row=1, column=1)

submit = Button(text='Calculate', command=miles_to_km)
submit.grid(row=2, column=1)

miles = Label(text="Miles")
miles.grid(row=0, column=3)

km = Label(text="Km")
km.grid(row=1, column=3)


window.mainloop()

