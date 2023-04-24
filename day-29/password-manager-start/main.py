from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    """
    This takes the data inputted in the entries and saves them to a `data.txt` file
    """
    ### --- Getting the data --- ###
    website_data = website_entry.get()
    email_data = email_entry.get()
    password_data = password_entry.get()
    ### --- --- ###

    with open("data.txt", mode='a') as data_file:
        data_file.write(f'{website_data} | {email_data} | {password_data} \n')

    ### --- Deleting the data --- ###
    website_entry.delete(0, END)
    password_entry.delete(0, END)
    ### --- --- ###


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

website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus() #Starts the GUI with the cursor here by default 

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, 'amwaniki.am@gmail.com')

password_entry = Entry(width=17)
password_entry.grid(row=3, column=1)

generate = Button(text='Generate Password')
generate.grid(row=3,column=2)

add_pass = Button(text='Add Password', width=30, command=save)
add_pass.grid(row=4, column=1, columnspan=2)

window.mainloop()
