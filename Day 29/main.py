import random
import tkinter as tk

FONT = ("Times New Roman", 14, "normal")



def generate_password():

    password.delete(0,"end")
    key = random.randint(1,100000)

    password.insert(0,str(key))

c= 1
def popup():
    pop_up = tk.Toplevel(root)
    pop_up.title("Notification")
    pop_up.geometry("400x100")
    label = tk.Label(pop_up, text="Password Saved Successfully",font=FONT)
    label.pack(side="top")
    close_btn = tk.Button(pop_up, text="Close", command=pop_up.destroy)
    close_btn.pack(pady=10)



def add_password():

    global c

    label = tk.Label(win,text=f"{webname.get()} | {email.get()} | {password.get()}")
    label.grid(row=c,column=0)
    popup()
    c= c+1
    password.delete(0, "end")
    webname.delete(0, "end")
    email.delete(0, "end")


# Create the window
root = tk.Tk()
root.title("Password Manager")
root.config(pady=40,padx=40)

canvas = tk.Canvas(root, height = 260, width = 260)
img = tk.PhotoImage(file="logo.png")
img = img.subsample(2,2)
canvas.create_image(130,130,image=img)
canvas.grid(row = 0, column = 0, columnspan = 3)


# Label 1
Web = tk.Label(root, text = "Website",font=FONT)
Web.grid(row = 1, column = 0)
Web.config(pady=5,padx=5)

# Label 2
user = tk.Label(root, text = "Email/Username",font=FONT)
user.grid(row = 2, column = 0)
user.config(pady=5,padx=5)

# Label 3
passw = tk.Label(root, text = "Password",font = FONT)
passw.grid(row = 3, column = 0)
passw.config(pady=5,padx=5)

# Input 1

webname = tk.Entry(root, font = FONT,width = 44)
webname.grid(row = 1, column = 1,columnspan = 2)


#Input 2

email = tk.Entry(root, font = FONT,width = 44)
email.grid(row = 2, column = 1,columnspan = 2)

#Input 3
password = tk.Entry(root, font = FONT,width = 20)
password.grid(row = 3, column = 1)

#button1
GenPass = tk.Button(root, text = "Generate Password", font = FONT, width = 20, command = generate_password)
GenPass.grid(row = 3, column = 2)

#button2
add = tk.Button(root, text = "Add",font = FONT,width = 40,command=add_password)
add.grid(row = 4, column = 1,columnspan = 2)
# add.config(pady=5,padx=5)

win=tk.Tk()
win.title("data.txt")
win.geometry("400x400")
labels = tk.Label(win, text="Website | Email/Username | Password")
labels.grid(row = 0, column = 0)
win.mainloop()



root.mainloop()





