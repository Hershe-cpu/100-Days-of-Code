import json
from json import JSONDecodeError
from random import randint,choice,shuffle
import tkinter as tk
from tkinter import messagebox
import pyperclip as pipy


FONT = ("Times New Roman", 12, "normal")


def search():
    search_button.config(fg="white",bg="blue")


    if website_entry.get() == "":
        messagebox.showinfo("Error", "Website Name cannot be empty")
        search_button.config(fg="black", bg="white")

    else:
        try:
            with open("data.json", "r") as file:
                data = json.load(file)
                email = data[website_entry.get()]["email"]
                password = data[website_entry.get()]["password"]
        except KeyError:
            messagebox.showinfo("Error", "Website Details does not exist")
            search_button.config(fg="black", bg="white")
        except FileNotFoundError:
            messagebox.showinfo("Error", "No data file found")
            search_button.config(fg="black", bg="white")
        except JSONDecodeError:
            messagebox.showinfo("Error", "File is empty")
            search_button.config(fg="black", bg="white")

        else:
            messagebox.showinfo("Password Info",f"{website_entry.get()}\n Email: {email} \n Password: {password} ")
            search_button.config(fg="black", bg="white")


def generate_password():
    password_entry.delete(0, "end")
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pipy.copy(password)


def add_data():
    website = website_entry.get()
    new_dict = {
        website: {
            "email": email_entry.get(),
            "password": password_entry.get()
        }
    }
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
            data.update(new_dict)

    except FileNotFoundError:
        with open("data.json", "w") as file:
            json.dump(new_dict,file, indent = 4)
    except JSONDecodeError:
        with open("data.json", "w") as file:
            json.dump(new_dict,file, indent = 4)
    else:
        with open("data.json", "w") as file:
            json.dump(data, file, indent = 4)


def reset_entry_widgets():
    password_entry.delete(0, "end")
    website_entry.delete(0, "end")
    email_entry.delete(0, "end")
    email_entry.insert(0,"raghavharshita999@gmail.com")


def add_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:

        messagebox.showinfo(title="Ooops", message="Please make sure you haven't left any parts")
    else:

        is_ok = messagebox.askokcancel(title=website,message= f"These are the details entered \nWebsite Name: {website}\nEmail Address: {email}\nPassword: {password} ")
        if is_ok:
            add_data()

            # display_data()
            reset_entry_widgets()


# Create the window
root = tk.Tk()
root.title("Password Manager")
root.config(pady=20,padx=20)
# Setting up the logo
canvas = tk.Canvas(root, height = 200, width = 200)
img = tk.PhotoImage(file="logo.png")
img = img.subsample(3)
canvas.create_image(100,100,image=img)
canvas.grid(row = 0, column = 0, columnspan = 3)
# Label 1
website_label = tk.Label(root, text ="Website", font=FONT)
website_label.grid(row = 1, column = 0)
website_label.config(pady=5, padx=5)
# Label 2
email_label = tk.Label(root, text ="Email/Username", font=FONT)
email_label.grid(row = 2, column = 0)
email_label.config(pady=5, padx=5)
# Label 3
password_label = tk.Label(root, text ="Password", font = FONT)
password_label.grid(row = 3, column = 0)
password_label.config(pady=5, padx=5)
# Input 1
website_entry = tk.Entry(root, font = FONT, width = 25)
website_entry.grid(row = 1, column = 1)
website_entry.focus()
#Input 2
email_entry = tk.Entry(root, font = FONT, width = 44)
email_entry.insert(0,"raghavharshita999@gmail.com")
email_entry.grid(row = 2, column = 1, columnspan = 2)
#Input 3
password_entry = tk.Entry(root, font = FONT, width = 25)
password_entry.grid(row = 3, column = 1)
#button1
generate_pass_button = tk.Button(root, text = "Generate Password", font = FONT, width = 15, command = generate_password)
generate_pass_button.grid(row = 3, column = 2)
#button2
add_button = tk.Button(root, text ="Add", font = FONT, width = 40, command=add_password)
add_button.grid(row = 4, column = 1, columnspan = 2)
#button3
search_button = tk.Button(root,text="Search",font=FONT,width=15,command=search)
search_button.grid(row = 1, column = 2)


root.mainloop()



