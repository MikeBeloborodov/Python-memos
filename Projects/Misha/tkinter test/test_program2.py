from tkinter import *
from tkinter import ttk

def change_text():
    text.set("Changed!")

root = Tk()
root.title("Test program")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

text = StringVar()
text.set("First Lable")

ttk.Label(mainframe, textvariable=text).grid(column=1, row=1, sticky="w")
ttk.Label(mainframe, text="Second Label").grid(column=1, row=2, sticky="w")
ttk.Label(mainframe, text="Third Label").grid(column=1, row=3, sticky="w")
ttk.Label(mainframe, text="Fourth Label").grid(column=2, row=1, sticky="w")
ttk.Label(mainframe, text="Fifth Label").grid(column=2, row=2, sticky="w")
ttk.Label(mainframe, text="Sixth Label").grid(column=2, row=3, sticky="w")

ttk.Button(mainframe, text="Press here", command=change_text).grid(column=2, row=4)

for child in mainframe.winfo_children():
    child.grid_configure(padx=10, pady=10)


root.mainloop()