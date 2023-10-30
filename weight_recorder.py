import datetime
import tkinter as tk

datafile = "/Users/allankant/Documents/Code/project_alpha/weight_data.txt"

root = tk.Tk()
root.title("Weight Recorder")
root.geometry("300x100")

label = tk.Label(root, text= "Enter weight here: ")
label.pack()

entryfield = tk.Entry(root)
entryfield.config({"background": "Grey"})
entryfield.pack()

button = tk.Button(root, text= "Save")
button.pack()

# table = tk.ttk.Treeview(root, columns=("Column1", "Column2", "Column3"))


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
        else:
            label.config(text="Try Again - between 50 and 90 please)")


button.config(command= on_button_click)

root.mainloop()