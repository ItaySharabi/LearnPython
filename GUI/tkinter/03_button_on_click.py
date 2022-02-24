from tkinter import *
from tkinter import ttk


def on_click():
    print('Button clicked! (Text changed)')
    # After object creation, you can treat option names as dictionary indexes:
    if 'Click here!' in btn['text']:
        btn['text'] = 'Text changed!'
    else:
        btn['text'] = 'Click here!'


root = Tk()  # Initialize root

# Create a button widget
btn = ttk.Button(master=root, text='Click here!', command=on_click, width=50)
btn.pack()  # Attach btn to root
print(btn.configure().keys())
print(btn.configure()['takefocus'])
# Display root window
mainloop()
