from tkinter import *


# משחק איקס עיגול

def on_click(btn):
    print(f'A button was clicked')


# פונקציות המשחק יכתבו כאן

window = Tk()  # נייצר חלון

window.geometry('576x536+520+100')

btn1 = Button(master=window, command=lambda: on_click(btn1), bg="light grey", height=2, width=7, fg="black",
              font=("Impact", 40), text="Hello")
btn2 = Button(master=window, command=on_click, bg="black", fg="white", height=2, width=7, font=("Impact", 40),
              text="Hello")
btn3 = Button(master=window, command=on_click, bg="light grey", fg="black", height=2, width=7, font=("Impact", 40),
              text="Hello")

btn4 = Button(master=window, bg="black", height=2, width=7, fg="white", font=("Impact", 40), text="Hello")
btn5 = Button(master=window, bg="light gray", fg="black", height=2, width=7, font=("Impact", 40), text="Hello")
btn6 = Button(master=window, bg="black", fg="white", height=2, width=7, font=("Impact", 40), text="Hello")

btn7 = Button(master=window, bg="light grey", height=2, width=7, fg="black", font=("Impact", 40), text="Hello")
btn8 = Button(master=window, bg="black", fg="white", height=2, width=7, font=("Impact", 40), text="Hello")
btn9 = Button(master=window, bg="light grey", fg="black", height=2, width=7, font=("Impact", 40), text="Hello")

btn1.grid(row=0, column=0)
btn2.grid(row=0, column=1)
btn3.grid(row=0, column=2)

btn4.grid(row=1, column=0)
btn5.grid(row=1, column=1)
btn6.grid(row=1, column=2)

btn7.grid(row=2, column=0)
btn8.grid(row=2, column=1)
btn9.grid(row=2, column=2)

window.mainloop()
