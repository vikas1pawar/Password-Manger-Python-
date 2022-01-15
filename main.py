import json
from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website_info = website_input.get()
    email_info = email_input.get()
    password_info = password_input.get()
    new_data = {
        website_info: {
            "email": email_info,
            "password": password_info,
        }
    }
    if len(website_info) == 0 or len(password_info) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        # is_ok = messagebox.askokcancel(title=website_info,
        # message=f"These details entered: \nEmail: {email_info}\n Password:{password_info}\n Is it ok to save?")
        # if is_ok:
        try:
            with open("data.json", "r") as data_file:
                # data_file.write(f"{website_info} | {email_info} | {password_info} \n")
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)
# -------------------SHOW DETAILS-----------------------
def find_password():
    website_name = website_input.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="File not find!")
    else:
        if website_name in data:
            email = data[website_name]['email']
            password = data[website_name]['password']
            messagebox.showinfo(title=f"{website_name}", message=f"Email: {email} \nPassword: {password}")
        else:
            messagebox.showinfo(title="error", message=f"No details for {website_name} exists")
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50,)


canvas = Canvas(width=200, height=200, highlightthickness=0)
tomato_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=tomato_img)
canvas.grid(column=1, row=0)

website = Label(text="Website:")
website.grid(column=0, row=1)

website_input = Entry(width=37)
website_input.focus()
website_input.grid(column=1, row=1, columnspan=2)

search = Button(text="Search", width=14, command=find_password)
search.grid(column=2, row=1)

email = Label(text="Email/Username:")
email.grid(column=0, row=2)

email_input = Entry(width=37)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, "vikas@gmail.com")

password = Label(text="Password:")
password.grid(column=0, row=3)

password_input = Entry(width=37)
password_input.grid(column=1, row=3, columnspan=2)

generate_password = Button(text="Generate Password", command=generate_password)
generate_password.grid(column=2, row=3)

add_button = Button(text="Add", width=32, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()

