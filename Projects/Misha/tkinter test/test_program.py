from tkinter import *
from tkinter import ttk

def calculate(*args):
    try:
        value = float(feet.get())
        meters.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        pass

# root of the window
root = Tk()

# title of the window
root.title("Feet to Meters")

# frame inside the window
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
# these are needed for resizing
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# entry widget
# feet is a variable to store information
feet = StringVar()
# mainframe - where to put widget, width - how long is this entry, feet - store variable
feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
# where to put this entry
feet_entry.grid(column=2, row=1, sticky=(W, E))

# other widgets
meters = StringVar()

ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))

ttk.Button(mainframe, text="Calculate").grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="is equivalent").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)   


# adds padding for every child (widget)

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

# The second part tells Tk to put the focus on our entry widget. 
# That way, the cursor will start in that field,
# so users don't have to click on it before starting to type.
feet_entry.focus()

# The third line tells Tk that if a user presses the Return key (Enter on Windows),
# it should call our calculate routine, the same as if they pressed the Calculate button.
root.bind("<Return>", calculate)

# beginning of the program
root.mainloop()