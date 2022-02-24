import tkinter as tk
from tkinter import *
from tkinter import messagebox

grade = 0
def increase():
  global grade
  if grade<100:
   grade = grade+20
def decrease():
    global grade
    if grade!=0:
      grade = grade-20


def finish(top7):
    top7.destroy()
    top8 = tk.Tk()
    top8.title("End of the game!")
    top8.geometry("600x450")
    top8.geometry("600x450")
    frame4 = tk.Frame(master=top8, height=150)
    frame4.pack(fill=tk.X)
    frame5 = tk.Frame(master=top8, height=150)
    frame5.pack(fill=tk.X)
    frame6 = tk.Frame(master=top8, height=150)
    frame6.pack(fill=tk.X)
    lbl3 = Label(frame4, text='You Are Done!', font=('Comic Sans MS', 30), fg='blue')
    lbl3.place(relx=0.5, rely=0, anchor='n')
    lbl4 = Label(frame5, text='your score:', font=('Comic Sans MS', 30), fg='blue')
    lbl4.place(relx=0.5, rely=0, anchor='n')
    lbl5 = Label(frame6, text=grade, font=('Comic Sans MS', 30), fg='blue')
    lbl5.place(relx=0.5, rely=0, anchor='n')
    btn4 = Button(top8, text="back to choose level", fg="red",command=menu)
    btn4.pack(side=LEFT)
    btn4.place(x=260, y=400)
def level1question5(top6):
    top6.destroy()
    top7 = tk.Tk()
    top7.title("level 1 question 5!")
    top7.geometry("600x450")
    frame4 = tk.Frame(master=top7, height=150)
    frame4.pack(fill=tk.X)
    frame5 = tk.Frame(master=top7, height=300)
    frame5.pack(fill=tk.X)
    lbl3 = Label(frame4, text='hello', font=('Comic Sans MS', 30), fg='blue')
    lbl3.place(relx=0.5, rely=0, anchor='n')
    rbtn3 = Radiobutton(frame5, text="כלב",
                        value="1",command=decrease).pack(side='top')
    rbtn4 = Radiobutton(frame5, text="חתול",command=decrease,
                        value="2").pack(side='top')
    rbtn5 = Radiobutton(frame5, text="שלום",command=increase,
                        value="3").pack(side='top')
    btn3 = Button(top7, text="continue", fg="red",command=lambda : finish(top7))
    btn3.pack(side=LEFT)
    btn3.place(x=260, y=400)
    return top7

def level1question4(top5):
    top5.destroy()
    top6 = tk.Tk()
    top6.title("level 1 question 4!")
    top6.geometry("600x450")
    frame4 = tk.Frame(master=top6, height=150)
    frame4.pack(fill=tk.X)
    frame5 = tk.Frame(master=top6, height=300)
    frame5.pack(fill=tk.X)
    lbl3 = Label(frame4, text='eat', font=('Comic Sans MS', 30), fg='blue')
    lbl3.place(relx=0.5, rely=0, anchor='n')
    rbtn3 = Radiobutton(frame5, text="לאכול",command=increase,
                        value="1").pack(side='top')
    rbtn4 = Radiobutton(frame5, text="חתול",
                        value="2",command=decrease).pack(side='top')
    rbtn5 = Radiobutton(frame5, text="דג",command=decrease,
                        value="3").pack(side='top')
    btn3 = Button(top6, text="continue", fg="red",command=lambda : level1question5(top6))
    btn3.pack(side=LEFT)
    btn3.place(x=260, y=400)
    return top6

def level1question3(top4):
    top4.destroy()
    top5 = tk.Tk()
    top5.title("level 1 question 3!")
    top5.geometry("600x450")
    frame4 = tk.Frame(master=top5, height=150)
    frame4.pack(fill=tk.X)
    frame5 = tk.Frame(master=top5, height=300)
    frame5.pack(fill=tk.X)
    lbl3 = Label(frame4, text='drink', font=('Comic Sans MS', 30), fg='blue')
    lbl3.place(relx=0.5, rely=0, anchor='n')
    rbtn3 = Radiobutton(frame5, text="כלב",
                        value="1",command=decrease).pack(side='top')
    rbtn4 = Radiobutton(frame5, text="לשתות",command=increase,
                        value="2").pack(side='top')
    rbtn5 = Radiobutton(frame5, text="דג",command=decrease,
                        value="3").pack(side='top')
    btn3 = Button(top5, text="continue", fg="red", command=lambda :level1question4(top5))
    btn3.pack(side=LEFT)
    btn3.place(x=260, y=400)
    return top5

def level1question2(top3):
    top3.destroy()
    top4 = tk.Tk()
    top4.title("level 1 question 2!")
    top4.geometry("600x450")
    frame4 = tk.Frame(master=top4, height=150)
    frame4.pack(fill=tk.X)
    frame5 = tk.Frame(master=top4, height=300)
    frame5.pack(fill=tk.X)
    lbl3 = Label(frame4, text='cat', font=('Comic Sans MS', 30), fg='blue')
    lbl3.place(relx=0.5, rely=0, anchor='n')
    rbtn3 = Radiobutton(frame5, text="כלב",
                        value="1",command=decrease).pack(side='top')
    rbtn4 = Radiobutton(frame5, text="חתול",command=increase,
                        value="2").pack(side='top')
    rbtn5 = Radiobutton(frame5, text="דג",
                        value="3",command=decrease).pack(side='top')
    btn3 = Button(top4, text="continue", fg="red",command=lambda : level1question3(top4))
    btn3.pack(side=LEFT)
    btn3.place(x=260, y=400)
    return top4


def level1question1():
    top3 = tk.Tk()
    top3.title("level 1 question 1!")
    top3.geometry("600x450")
    frame4 = tk.Frame(master=top3, height=150)
    frame4.pack(fill=tk.X)
    frame5 = tk.Frame(master=top3, height=300)
    frame5.pack(fill=tk.X)
    lbl3 = Label(frame4, text='dog', font=('Comic Sans MS', 30), fg='blue')
    lbl3.place(relx=0.5, rely=0, anchor='n')
    rbtn3 = Radiobutton(frame5, text="כלב",
                        value="1",command=increase).pack(side='top')
    rbtn4 = Radiobutton(frame5, text="חתול",
                        value="2",command=decrease).pack(side='bottom')
    rbtn5 = Radiobutton(frame5, text="דג",
                        value="3",command=decrease).pack(side='bottom')
    btn3 = Button(top3, text="continue", fg="red",command=lambda : level1question2(top3))
    btn3.pack(side=LEFT)
    btn3.place(x=260, y=400)
    """btn4 = Button(top3, text="save answer", fg="red", command=lambda : top3.destroy())
    btn4.pack(side=LEFT)
    btn4.place(x=370, y=400)"""
    return top3




def instructions():
    top2 = tk.Tk()
    top2.title("Instructions")
    top2.geometry("600x450")
    frame4 = tk.Frame(master=top2, height=600, bg="yellow")
    frame4.pack(fill=tk.X)
    lbl2 = Label(top2, text='Choose the correct answer each level of the game,pay attention only one answer is correct!',fg='blue')
    lbl2.place(relx=0.5, rely=0.1, anchor='n')
def start():
 name=T.get("1.0","end-1c")
 if not name :
     messagebox.showerror("ERROR", "please enter a name")
 else:
    messagebox.showinfo("let's start","Hey "+name+",lets start")
def menu():
    top1 = tk.Tk()
    top1.title("please choose a level")
    top1.geometry("600x450")
    v = StringVar(top1, "1")
    rbtn1=Radiobutton(top1, text="level 1", variable=v,command=level1question1,
                    value="1").pack(side=TOP, ipady=5)
    rbtn2 = Radiobutton(top1, text="level 2", variable=v,
                        value="2").pack(side=TOP, ipady=5)
    btn2 = Button(top1, text="Instructions", fg="red", command=instructions)
    btn2.pack(side=LEFT)
    btn2.place(x=60, y=10)
    btn3 = Button(top1, text="Start Game", fg="red",)
    btn3.pack(side=LEFT)
    btn3.place(x=260, y=200)




def exit1():
    MsgBox = messagebox.askquestion("Exit", "Are you sure you want to exit?",icon='warning')
    if MsgBox == 'yes':
        top.destroy()
    else:
        messagebox.showinfo('Return', 'You will now return to the application screen')


top = tk.Tk()
top.title("welcom to our vocabulary game")
top.geometry("600x450")
frame1 = tk.Frame(master=top, height=150, bg="red")
frame1.pack(fill=tk.X)

frame2 = tk.Frame(master=top, height=150, bg="yellow")
frame2.pack(fill=tk.X)

frame3 = tk.Frame(master=top, height=150, bg="blue")
frame3.pack(fill=tk.X)
# Code to add widgets will go here...
lbl = Label(top, text = 'WELCOM!', font = ('Comic Sans MS',30),
 bg = 'Green', fg = 'blue')
lbl.place(relx = 0.5,rely = 0.1,anchor = 'n')
lbl1 = Label(top, text = 'Your Name:', font = ('Comic Sans MS',30),
 bg = 'Green', fg = 'red')
lbl1.place(relx = 0.3,rely = 0.4,anchor = 'n')
btn = Button(top, text="save name",fg="red",command=start)
btn.pack(side = LEFT)
btn.place(x=520,y=200)
flag=0
bt = Button(top, text="continue",fg="red",command=menu)
bt.pack(side = LEFT)
bt.place(x=520,y=400)
btn1 = Button(top, text="EXIT",fg="red",command=exit1)
btn1.pack(side = LEFT)
btn1.place(x=270,y=400)
T = Text(top, height = 2, width = 25)
T.place(x=300,y=190)
top.mainloop()