# Import all the necessary libraries
from tkinter import *

# Define the tkinter instance
win = Tk()
win.title("Rounded Button")

# Define the size of the tkinter frame
win.geometry("1280x790")


# Define the working of the button

def my_command():
    if 'show image' in button['text']:
        text.config(text="Click to hide image!")
        button.config(image=click_btn, text='')
    else:
        button.config(image='', text='Click to show image!')
        text.config(text="Click to show image!")


# Create the image using PhotoImage widget
click_btn = PhotoImage(file='images/click_here.png')

# Let us create a button and pass the image
button = Button(master=win, image=click_btn, command=my_command,
                borderwidth=5)
# Pad the button 20 pixels from top/bottom/left and right
# שחקו עם הערכים כדי ללמוד מה הם עושים בתצוגה
button.pack(pady=20)

text = Label(win, text="Click to hide image!")
# מדוע לא חייבים לציין pady?
text.pack(pady=10)
win.mainloop()
