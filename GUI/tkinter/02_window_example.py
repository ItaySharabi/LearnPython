# from tkinter import *
from tkinter import ttk
from tkinter import Tk

root = Tk()

frm = ttk.Frame(root, padding=10)
frm.grid(rows=3, columns=3)

ttk.Label(master=frm, text='Enter your name: ').grid(row=0, column=0)

ttk.Label(frm, text="Hello World!").grid(row=1, column=1)

ttk.Button(frm, text="Quit", command=root.destroy).grid(row=2, column=2)

root.mainloop()
