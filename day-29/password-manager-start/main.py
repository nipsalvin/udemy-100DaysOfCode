from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file ='logo.png')
canvas.create_image(100, 100, image = lock_img)
canvas.grid(row=0, column=1)

website = Label(text='Website:')
website.grid(row=1, column=0)

password = Label(text='Password')
password.grid(row=3, column=0)

email = Label(text='Email/UserName')
email.grid(row=2, column=0)

website_input = Entry(width=35)
website_input.grid(row=1, column=1, columnspan=2)

email_input = Entry(width=35)
email_input.grid(row=2, column=1, columnspan=2)

password_input = Entry(width=17)
password_input.grid(row=3, column=1)

generate = Button(text='Generate Password')
generate.grid(row=3,column=2)

add_pass = Button(text='Add Password', width=30)
add_pass.grid(row=4, column=1, columnspan=2)

window.mainloop()
