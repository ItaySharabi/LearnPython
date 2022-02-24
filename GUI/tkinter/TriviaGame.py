from tkinter import *
from tkinter import ttk

root = Tk()


def start_game():
    menu()


def menu():
    game_window = Tk()
    game_window.title("please choose a level")
    game_window.geometry("650x650")
    v = StringVar(game_window, "1")
    Radiobutton(game_window, text="level 1", variable=v,
                        value="1").pack(side=TOP, ipady=5)
    Radiobutton(game_window, text="level 2", variable=v,
                        value="2").pack(side=TOP, ipady=5)
    print(Radiobutton.configure(Radiobutton())['value'])
    print(f'rbtn.value = {Radiobutton()["value"]}')
    btn2 = Button(game_window, text="Instructions", fg="red")
    btn2.place(x=60, y=20)
    btn3 = Button(game_window, text="Start Game", fg="red")
    btn3.place(x=260, y=200)


def setup_main_window():
    root.title = 'Trivial Pursuit'
    root.geometry('650x650')

    frame = ttk.Frame(root, height=50, width=50, padding=10)
    print(frame.configure().keys())
    frame.pack()

    btn = ttk.Button(frame, text='Frame button', command=start_game)
    btn.pack()

    root.mainloop()


setup_main_window()
