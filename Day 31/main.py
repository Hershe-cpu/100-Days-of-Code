
from random import choice
import tkinter as tk
from tkinter import Tk
import pandas as pd



# CONSTANTS

BACKGROUND = "#A6D8BF"
HEAD=("Arial",40,"italic")
TEXT = ("Arial",60,"bold")
current_card={}
data_dict={}
option="right"

try:
    data = pd.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/german_words.csv")
    data_dict = original_data.to_dict(orient="records")
except ValueError:
    original_data = pd.read_csv("data/german_words.csv")
    data_dict = original_data.to_dict(orient="records")
else:
    data_dict = (data.to_dict(orient="records"))



def show_answer():
    global current_card
    canvas.itemconfig(title,text="English",fill="white")
    canvas.itemconfig(word, text=f"{current_card['English']}",fill="white")
    canvas.itemconfig(image, image=back_img)


def display_word():
    global current_card,timer_id
    root.after_cancel(timer_id)
    if not data_dict:
        canvas.itemconfig(title,text="Congrats",fill="black")
        canvas.itemconfig(word, text="All Words Done!",fill="black")
        canvas.itemconfig(image, image=front_img)
        current_card    ={}
        return

    current_card = choice(data_dict)
    canvas.itemconfig(title, text="German",fill="black")
    canvas.itemconfig(word,text=f"{current_card['German']}",fill="black")
    canvas.itemconfig(image,image=front_img)
    timer_id = root.after(3000,show_answer)

def if_right():
    global current_card,option
    if current_card in data_dict:
        data_dict.remove(current_card)
    learn_data = pd.DataFrame(data_dict)
    learn_data.to_csv("./data/words_to_learn.csv",index=False)
    display_word()


def if_wrong():
    display_word()

def quit_game():
    exit()


# WINDOW SETUP
root = Tk()
root.title("FlashCard")
root.geometry("900x780")
root.config(bg=BACKGROUND,padx=50,pady=50)



timer_id=root.after(3000,show_answer)

canvas = tk.Canvas(root,
                   height=526,
                   width=800,
                   bg=BACKGROUND,
                   highlightthickness=0
                   )
front_img = tk.PhotoImage(file="./images/card_front.png",format="png")
back_img = tk.PhotoImage(file="./images/card_back.png",format="png")
image =canvas.create_image(400, 263)
title =canvas.create_text(400,150,font=HEAD,fill="Black")
word = canvas.create_text(400,275,font=TEXT,fill="black")
canvas.config(bg=BACKGROUND,highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2, sticky="nsew")


#Button

right_img = tk.PhotoImage(file="./images/right.png",format="png")
right_button = tk.Button(root,image=right_img,bg=BACKGROUND,command=if_right,bd=0,highlightthickness=0)
right_button.grid(row=1,column=0,padx=10,pady=10)
wrong_img = tk.PhotoImage(file="./images/wrong.png",format="png")
wrong_button = tk.Button(root,image=wrong_img,bg=BACKGROUND,command=if_wrong,bd=0,highlightthickness=0)
wrong_button.grid(row=1,column=1,padx=10,pady=10)
exit_button=tk.Button(root,text="Quit",bg=BACKGROUND,command=quit_game,font=("Arial",20,"normal"))
exit_button.grid(row=2,columnspan=2,padx=10,pady=10)
display_word()
root.mainloop()