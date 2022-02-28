from tkinter import Tk   # Display object
from tkinter import ttk  # Widget's library
# from tkinter import *  # Alternative way of importing all library files

# Initialize main Tk root window
root = Tk()

# Create a frame widget
frame = ttk.Frame(master=root, padding=10)

# What configurations does has a `Frame` Widget?
print(frame.configure().keys())
frame.configure(height=400, width=400)  # הגדרת פרמטרים של "חלון"
frame.pack()       # נשים לב ששום שינוי לא נעשה לפני שנקרא ל

# Display root window
root.mainloop()
