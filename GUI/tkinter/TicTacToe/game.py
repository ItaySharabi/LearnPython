from tkinter import *
from tkinter import messagebox

'''
@author: Itay Sharabi
This is a TicTacToe - Single Player - python game.
Coding Challenge:
Create A.I. that plays against the user!
'''


def check_win():
    print(f'Checking for a win')
    global count, turn
    if count >= 9:
        messagebox.showinfo("Game is over", "No more possible moves...\nRestarting...")
        restart(window)
    # Add all winning situation conditions here:
    # ...


def on_click(btn):
    global count, turn
    if btn['text'] == " ":
        if turn:  # if turn == True -> it is Player 1's turn ('X')
            btn['text'] = 'X'
        else:
            btn['text'] = 'O'
        count += 1
        turn = not turn
        check_win()


def restart(window):
    global turn, count
    create_buttons(game_frame)
    turn = True  # if turn == True, then it is Player 1's turn
    count = 0  # count number of moves (Maximum 9)


def create_buttons(window):
    # יצירת כפתורים:
    btn1 = Button(window, font=("Impact", 20), text=" ", height=5, width=14, bg="light grey",
                  command=lambda: on_click(btn1))
    btn2 = Button(window, font=("Impact", 20), text=" ", height=5, width=14, bg="black", fg="white",
                  command=lambda: on_click(btn2))
    btn3 = Button(window, font=("Impact", 20), text=" ", height=5, width=14, bg="light grey",
                  command=lambda: on_click(btn3))

    btn4 = Button(window, font=("Impact", 20), text=" ", height=5, width=14, bg="black", fg="white",
                  command=lambda: on_click(btn4))
    btn5 = Button(window, font=("Impact", 20), text=" ", height=5, width=14, bg="light grey",
                  command=lambda: on_click(btn5))
    btn6 = Button(window, font=("Impact", 20), text=" ", height=5, width=14, bg="black", fg="white",
                  command=lambda: on_click(btn6))

    btn7 = Button(window, font=("Impact", 20), text=" ", height=5, width=14, bg="light grey",
                  command=lambda: on_click(btn7))
    btn8 = Button(window, font=("Impact", 20), text=" ", height=5, width=14, bg="black", fg="white",
                  command=lambda: on_click(btn8))
    btn9 = Button(window, font=("Impact", 20), text=" ", height=5, width=14, bg="light grey",
                  command=lambda: on_click(btn9))

    btn1.grid(row=0, column=0)
    btn2.grid(row=0, column=1)
    btn3.grid(row=0, column=2)

    btn4.grid(row=1, column=0)
    btn5.grid(row=1, column=1)
    btn6.grid(row=1, column=2)

    btn7.grid(row=2, column=0)
    btn8.grid(row=2, column=1)
    btn9.grid(row=2, column=2)


# כאן מתחיל הקוד
if __name__ == '__main__':
    window = Tk()

    # נגדיר את גודל החלון 576 על 588 ונמקם אותו 470 פיקסלים ימינה ו-100 למטה
    window.geometry('576x588+470+70')

    # יצירת תפריט:
    menu = Menu(master=window)  # נשייך תפריט לחלון שלנו
    window.config(menu=menu)  # *נשייך* לחלון שלנו את התפריט במקום למקם אותו, החלון ממקם בעצמו את התפריט
    menu.add_command(label="Restart game", command=lambda: restart(window))  # נוסיף פעולה
    #
    # # יצירת פריים של מידע על המשחק
    # # txt_frame = Frame(master=window)
    # label = Label(master=window, padx=10, font=("Great Vibes", 40, "italic"), text="X Turn")
    # label.pack(side=BOTTOM)
    # # txt_frame.pack(side=TOP)

    # יצירת פריים  המשחק
    game_frame = Frame(master=window)
    game_frame.pack(side=TOP)

    restart(game_frame)  # הכנת הכפתורים למשחק והגדרת המשתנים

    window.mainloop()  # הרצת החלון
