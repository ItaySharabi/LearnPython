from tkinter import *
from tkinter import ttk


def on_click():
    print('Button clicked! (Text changed)')
    print(btn.configure().keys())
    # After object creation, you can treat option names as dictionary indexes:
    if 'Click here!' in btn['text']:
        btn['text'] = 'Text changed!'
        btn['padding'] = 10
        img = PhotoImage(file='images/click_here.png')
        btn.configure(image=img)
        btn.pack(pady=20)

    else:
        btn['image'] = ''  # חייבים למחוק את התמונה שהייתה כדי לערוך את הטקסט
        btn['text'] = 'Click here!'
        # btn['image'] = ''  # אם נבצע את השורה הזו אחרי שנערוך את את הטקסט נקבל שגיאה!
        btn['padding'] = 0


root = Tk()  # Initialize root

# Create a button widget
btn = ttk.Button(master=root, text='Click here!', command=on_click, width=50)
btn.pack()  # Attach btn to root
# print(btn.configure().keys())
# print(btn.configure()['takefocus'])
# Display root window
mainloop()
