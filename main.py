from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def password_generator():
    # Password Generator Project

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    #password_list = []

    # for char in range(nr_letters):
    #     password_list.append(random.choice(letters))

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]

    # for char in range(nr_symbols):
    #     password_list += random.choice(symbols)
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]

    # for char in range(nr_numbers):
    #     password_list += random.choice(numbers)
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list=password_numbers + password_symbols + password_letters

    random.shuffle(password_list)

    password = "".join(password_list)

    pEntry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def add_to_file():
    with open("data.txt", mode="a") as file:

        website = wsEntry.get()
        email = euEntry.get()
        password = pEntry.get()

        if len(website) == 0 or len(password) == 0:
            messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")

        else:

            is_okay = messagebox.askokcancel(title=website, message=f"These are the details entered: "
                                                          f"\nEmail:{email}\nPassword:{password}\n Is it ok to save?")
            if is_okay:
                file.write(f"{website} | {email} | {password}\n")

                wsEntry.delete(0, END)
                pEntry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0)

wsLabel = Label(text="Website:")
wsLabel.grid(column=0, row=1)
euLabel = Label(text="Email/Username:")
euLabel.grid(column=0, row=2)
pLabel = Label(text="Password:")
pLabel.grid(column=0, row=3)

wsEntry = Entry(width=35)
wsEntry.grid(column=1, row=1, columnspan=2)
wsEntry.focus()
euEntry = Entry(width=35)
euEntry.grid(column=1, row=2, columnspan=2)
euEntry.insert(0, "deniz.uzen@icloud.com")
pEntry = Entry(width=21)
pEntry.grid(column=1, row=3)

gpButton = Button(text="Generate Password", command=password_generator)
gpButton.grid(column=2, row=3)
addButton = Button(text="Add", width=36, command=add_to_file)
addButton.grid(column=1, row= 4, columnspan=2)


window.mainloop()