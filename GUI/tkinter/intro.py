from tkinter import Tk   # Root display object
from tkinter import ttk  # Widget's library
# from tkinter import *  # Alternative way of importing all library files

# Initialize main Tk root window
root = Tk()

# Create a frame widget
frame = ttk.Frame(master=root, padding=10)

# What configurations does has a `Frame` Widget?
print(frame.configure().keys())
frame.configure(height=400, width=400)  # dict_keys(['borderwidth', 'padding', ...])
# frame.pack()       # No changes are made before we call pack()

# Display root window
root.mainloop()
