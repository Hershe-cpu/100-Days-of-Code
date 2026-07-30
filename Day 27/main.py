import tkinter as tk
from tkinter import ttk

from pandas.core.computation import align

root = tk.Tk()
root.title("Unit Converter")
root.configure(background="white")
root.config(pady=30,padx=30)
root.maxsize(800,600)
root.minsize(400,300)

def convert():
    n= entry.get()
    n= float(n)
    km= n*1.609
    res["text"] = km

def remove():
    entry.delete(0, "end")
    res["text"] = ""

#label
label1 = tk.Label(root, text="Unit Converter")
label1.grid(row=0, column=1)
label1.config(pady=30,padx=30)
label1.configure(background="white")
label1.config(font=("Arial", 16,"bold"))

#entry
entry = ttk.Entry(root, width=10)
# entry.insert(tk.END,"Enter Distance")
entry.grid(row=1, column=1)
entry.focus()
entry.config(font=("Arial", 14))

label3 = tk.Label(root, text="Miles")
label3.grid(row=1, column=2)
label3.config(font=("Arial", 14),background="white")


#label2
label2 = tk.Label(root, text="is equal to")
label2.grid(row=2, column=0)
label2.config(font=("Arial", 14),background="white")

label4 = tk.Label(root, text="Km")
label4.grid(row=2, column=2)
label4.config(font=("Arial", 14),background="white")

res = tk.Label(root, text="0")
res.grid(row=2, column=1)
res.config(font=("Arial", 14),background="white")

button = tk.Button(root, text="Calculate", command=convert)
button.grid(row=3, column=1)
button.config(font=("Arial", 14),background="white")

clear = tk.Button(root, text="Clear", command=remove)
clear.grid(row=4, column=1)

























root.mainloop()