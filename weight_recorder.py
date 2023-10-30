import datetime
import tkinter as tk
from tkinter import ttk

datafile = "/Users/allankant/Documents/Code/project_alpha/weight_data.txt"

root = tk.Tk()
root.title("Weight Recorder")
root.geometry("600x100")

label = tk.Label(root, text= "Enter weight here: ")
label.pack()

entryfield = tk.Entry(root)
entryfield.config({"background": "Grey"})
entryfield.pack()

button = tk.Button(root, text= "Save")
button.pack()

# Date and Weight Table
table = ttk.Treeview(root, columns=("#","Date", "Weight"))
table.heading("#0", text="#")
table.heading("#1", text="Date")
table.heading("#2", text="Weight")

def on_button_click():
    try:
        weight = float(entryfield.get())
    except ValueError:
        label.config(text="Try Again - Enter a Number)")
    else:
        if weight > 50 and weight <90:
            label.config(text="Weight Saved")
            button.config(text= "Saved")
            with open(datafile, "a") as file:
                file.write(f"\n{datetime.date.today()},{float(weight)}")
            table.pack()
        else:
            label.config(text="Try Again - between 50 and 90 please)")

#Read the history from the file into a list where each element contains a separate date and weight sub-element
with open(datafile, "r") as file:
    rawhistory = file.readlines()

history = []
for x in rawhistory:
    if x != '\n':
        weightentry = x.split(",")
        weightentry[1] = float(weightentry[1])
        history.append(weightentry)
print(history)

rownum = 1
for x in history:
    table.insert("", "end", values = (f"{rownum}", x[0], x[1]))
    rownum += 1

button.config(command= on_button_click)

root.mainloop()