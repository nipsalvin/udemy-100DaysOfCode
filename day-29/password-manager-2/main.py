from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []
    #### Using a loop
    # nr_letters = randint(8, 10)
    # nr_symbols = randint(2, 4)
    # nr_numbers = randint(2, 4)
    # for char in range(nr_letters):
    #     password_list.append(choice(letters))

    # for char in range(nr_symbols):
    #     password_list += choice(symbols)

    # for char in range(nr_numbers):
    #     password_list += choice(numbers)

    #### Using List comprehension
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(8, 10))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    ###Creating an empty string then adding values
    # password = ""
    # for char in password_list:
    #     password += char
    #     password_entry.insert(0, f'{password}')
    
    ###Joining the values from password_list
    password = ''.join(password_list)
    password_entry.insert(0, f'{password}')
    pyperclip.copy(password)
    print(f"Your password is: {password}")


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    """
    This takes the data inputted in the entries and saves them to a `data.txt` file
    """
    ### --- Getting the data --- ###
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website:{
            'email': email,
            'password': password
        }
    }
    ### --- --- ###

    if len(website_entry.get()) < 1 or len(password_entry.get()) < 1:
        messagebox.showerror(title='Blank Spaces', message='You cannot have blank spaces')
    else:
        try:
            with open('data.json', 'r') as data_file:
                ##JSON Reading old data##
                data = json.load(data_file)
                ##JSON Updating old data with new data##
                data.update(new_data)
        except FileNotFoundError:
            with open('data.json', 'w') as data_file:
                ##JSON Writing new data##
                json.dump(new_data, data_file, indent=4)
        else:
            with open('data.json', 'w') as data_file:
                ##JSON Writing new data##
                json.dump(data, data_file, indent=4)
        finally:
            ### --- Deleting the data --- ###
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            ### --- --- ###


# ---------------------------- SEARCH BUTTON ------------------------------- #
def find_password():
    with open('data.json', 'r') as data_file:
        data = json.load(data_file)
        website = website_entry.get().title()
        email = email_entry.get()
        password = password_entry.get()
        value = data[website]
        # print(value)
        if value:
            messagebox.showinfo(title=website, message=f'Email: {email}\n Password: {password}')


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

website_entry = Entry(width=16)
website_entry.grid(row=1, column=1)
website_entry.focus() #Starts the GUI with the cursor here by default 

search_entry = Button(text='Search', width=15, command=find_password)
search_entry.grid(row=1,column=2)

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, 'amwaniki.am@gmail.com')

password_entry = Entry(width=16)
password_entry.grid(row=3, column=1)

generate = Button(text='Generate Password', command=generate_password)
generate.grid(row=3,column=2)

add_pass = Button(text='Add Password', width=30, command=save)
add_pass.grid(row=4, column=1, columnspan=2)

window.mainloop()
