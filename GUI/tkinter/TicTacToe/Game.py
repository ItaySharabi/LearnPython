from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Tic Tac Toe")
window.geometry("420x486+500+120")

turn = True
count = 0
winner = False

def func_restart():
    global b1,b2,b3,b4,b5,b6,b7,b8,b9 ,count , winner
    count=0
    winner =False
    # יצירת כפתור
    b1 = Button(window, text=" ", font=("Impact", 20), height=4, width=10, bg="dark blue", command=lambda: click(b1))
    b2 = Button(window, text=" ", font=("Impact", 20), height=4, width=10, bg="blue", command=lambda: click(b2))
    b3 = Button(window, text=" ", font=("Impact", 20), height=4, width=10, bg="dark blue", command=lambda: click(b3))

    b4 = Button(window, text=" ", font=("Impact", 20), height=4, width=10, bg="blue", command=lambda: click(b4))
    b5 = Button(window, text=" ", font=("Impact", 20), height=4, width=10, bg="dark blue", command=lambda: click(b5))
    b6 = Button(window, text=" ", font=("Impact", 20), height=4, width=10, bg="blue", command=lambda: click(b6))

    b7 = Button(window, text=" ", font=("Impact", 20), height=4, width=10, bg="dark blue", command=lambda: click(b7))
    b8 = Button(window, text=" ", font=("Impact", 20), height=4, width=10, bg="blue", command=lambda: click(b8))
    b9 = Button(window, text=" ", font=("Impact", 20), height=4, width=10, bg="dark blue", command=lambda: click(b9))

    # מיקום של הכפתור
    b1.grid(row=0, column=0)
    b2.grid(row=0, column=1)
    b3.grid(row=0, column=2)

    b4.grid(row=1, column=0)
    b5.grid(row=1, column=1)
    b6.grid(row=1, column=2)

    b7.grid(row=2, column=0)
    b8.grid(row=2, column=1)
    b9.grid(row=2, column=2)


def disable():
    b1.config(state = DISABLED)
    b2.config(state = DISABLED)
    b3.config(state = DISABLED)
    b4.config(state = DISABLED)
    b5.config(state = DISABLED)
    b6.config(state = DISABLED)
    b7.config(state = DISABLED)
    b8.config(state = DISABLED)
    b9.config(state = DISABLED)


def check_win ():
    global winner , count
    if ( b1["text"] == 'X' and b2["text"] == 'X' and b3["text"]=='X' ):
        b1.config(bg="red")
        b2.config(bg="red")
        b3.config(bg="red")
        messagebox.showinfo("Tic Tac Toe" , "ohhhh , X won!\n")
        disable()
        winner = True
    elif ( b4["text"] == 'X' and b5["text"] == 'X' and b6["text"]=='X' ):
        b4.config(bg="red")
        b5.config(bg="red")
        b6.config(bg="red")
        messagebox.showinfo("Tic Tac Toe" , "ohhhh , X won!\n")
        disable()
        winner = True
    elif ( b7["text"] == 'X' and b8["text"] == 'X' and b9["text"]=='X' ):
        b7.config(bg="red")
        b8.config(bg="red")
        b9.config(bg="red")
        messagebox.showinfo("Tic Tac Toe" , "ohhhh , X won!\n")
        disable()
        winner = True

    elif ( b1["text"] == 'X' and b4["text"] == 'X' and b7["text"]=='X' ):
        b1.config(bg="red")
        b4.config(bg="red")
        b7.config(bg="red")
        messagebox.showinfo("Tic Tac Toe" , "ohhhh , X won!\n")
        disable()
        winner = True

    elif ( b2["text"] == 'X' and b5["text"] == 'X' and b8["text"]=='X' ):
        b2.config(bg="red")
        b5.config(bg="red")
        b8.config(bg="red")
        messagebox.showinfo("Tic Tac Toe" , "ohhhh , X won!\n")
        disable()
        winner = True

    elif ( b3["text"] == 'X' and b6["text"] == 'X' and b9["text"]=='X' ):
        b3.config(bg="red")
        b6.config(bg="red")
        b9.config(bg="red")
        messagebox.showinfo("Tic Tac Toe" , "ohhhh , X won!\n")
        disable()
        winner = True

    elif ( b1["text"] == 'X' and b5["text"] == 'X' and b9["text"]=='X' ):
        b1.config(bg="red")
        b5.config(bg="red")
        b9.config(bg="red")
        messagebox.showinfo("Tic Tac Toe" , "ohhhh , X won!\n")
        disable()
        winner = True

    elif ( b3["text"] == 'X' and b5["text"] == 'X' and b7["text"]=='X' ):
        b3.config(bg="red")
        b5.config(bg="red")
        b7.config(bg="red")
        messagebox.showinfo("Tic Tac Toe" , "ohhhh , X won!\n")
        disable()
        winner = True


    if ( b1["text"] == 'O' and b2["text"] == 'O' and b3["text"]=='O' ):
        b1.config(bg="red")
        b2.config(bg="red")
        b3.config(bg="red")
        messagebox.showinfo("Tic Tac Toe" , "ohhhh , O won!\n")
        disable()
        winner = True
    elif ( b4["text"] == 'O' and b5["text"] == 'O' and b6["text"]=='O' ):
        b4.config(bg="red")
        b5.config(bg="red")
        b6.config(bg="red")
        messagebox.showinfo("Tic Tac Toe" , "ohhhh , O won!\n")
        disable()
        winner = True
    elif ( b7["text"] == 'O' and b8["text"] == 'O' and b9["text"]=='O' ):
        b7.config(bg="red")
        b8.config(bg="red")
        b9.config(bg="red")
        messagebox.showinfo("Tic Tac Toe" , "ohhhh , O won!\n")
        disable()
        winner = True

    elif ( b1["text"] == 'O' and b4["text"] == 'O' and b7["text"]=='O' ):
        b1.config(bg="red")
        b4.config(bg="red")
        b7.config(bg="red")
        messagebox.showinfo("Tic Tac Toe" , "ohhhh , O won!\n")
        disable()
        winner = True
    elif ( b2["text"] == 'O' and b5["text"] == 'O' and b8["text"]=='O' ):
        b2.config(bg="red")
        b5.config(bg="red")
        b8.config(bg="red")
        messagebox.showinfo("Tic Tac Toe" , "ohhhh , O won!\n")
        disable()
        winner = True
    elif ( b3["text"] == 'O' and b6["text"] == 'O' and b9["text"]=='O' ):
        b3.config(bg="red")
        b6.config(bg="red")
        b9.config(bg="red")
        messagebox.showinfo("Tic Tac Toe" , "ohhhh , O won!\n")
        disable()
        winner = True

    elif ( b1["text"] == 'O' and b5["text"] == 'O' and b9["text"]=='O' ):
        b1.config(bg="red")
        b5.config(bg="red")
        b9.config(bg="red")
        messagebox.showinfo("Tic Tac Toe" , "ohhhh , O won!\n")
        disable()
        winner = True
    elif ( b3["text"] == 'O' and b5["text"] == 'O' and b7["text"]=='O' ):
        b3.config(bg="red")
        b5.config(bg="red")
        b7.config(bg="red")
        messagebox.showinfo("Tic Tac Toe" , "ohhhh , O won!\n")
        disable()
        winner = True

    elif (count == 9 and winner==False):
        messagebox.showinfo("Tic Tac Toe","Game draw!\nPlease press restart to play again!")
        disable()



def click(b):
    global count , turn
    if (b["text"] == ' ' and turn == True):
        b["text"] = 'X'
        turn = False
        count = count+1
        check_win()
    elif (b["text"] == ' ' and turn == False):
        b["text"] = 'O'
        turn = True
        count = count+1
        check_win()
    else:
        messagebox.showerror("Tic Tac Toe" , "Please try other option!\n")


#יצירת כפתור
b1 = Button(window , text = " " , font = ("Impact" ,20), height= 4 , width = 10 , bg = "dark blue" , command =lambda: click(b1) )
b2 = Button(window , text = " " , font = ("Impact" ,20), height= 4 , width = 10 , bg = "blue" , command =lambda: click(b2))
b3 = Button(window , text = " " , font = ("Impact" ,20), height= 4 , width = 10 , bg = "dark blue",command =lambda: click(b3) )

b4 = Button(window , text = " " , font = ("Impact" ,20), height= 4 , width = 10 , bg = "blue",command =lambda: click(b4) )
b5 = Button(window , text = " " , font = ("Impact" ,20), height= 4 , width = 10 , bg = "dark blue" ,command =lambda: click(b5))
b6 = Button(window , text = " " , font = ("Impact" ,20), height= 4 , width = 10 , bg = "blue",command =lambda: click(b6) )

b7 = Button(window , text = " " , font = ("Impact" ,20), height= 4 , width = 10 , bg = "dark blue" ,command =lambda: click(b7))
b8 = Button(window , text = " " , font = ("Impact" ,20), height= 4 , width = 10 , bg = "blue",command =lambda: click(b8) )
b9 = Button(window , text = " " , font = ("Impact" ,20), height= 4 , width = 10 , bg = "dark blue",command =lambda: click(b9) )


#מיקום של הכפתור
b1.grid(row = 0 , column = 0 )
b2.grid(row = 0 , column = 1 )
b3.grid(row = 0 , column = 2 )

b4.grid(row = 1 , column = 0 )
b5.grid(row = 1 , column = 1 )
b6.grid(row = 1 , column = 2 )

b7.grid(row = 2 , column = 0 )
b8.grid(row = 2 , column = 1 )
b9.grid(row = 2 , column = 2 )

#יצירת תפריט
Game_Menu = Menu(window)
window.config(menu = Game_Menu)

#יצירת חלון בתפריט

Restart = Menu(Game_Menu)
Game_Menu.add_command(label = "Restart Game!" , command = func_restart )


window.mainloop()