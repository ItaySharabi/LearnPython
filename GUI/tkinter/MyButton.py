from tkinter import *


# --------------------------------------------------------------------------------------------
# בקורס הבא אתם תלמדו איך להגדיר כפתור משלכם כך שכל פעם שתיצרו אותו תקבלו אותו מוכן כמו שקבעתם
class MyButton(Button):

    def __init__(self, master):
        super().__init__(master=master)
        self.img = PhotoImage(file="./images/click_here.png")
        print(f'cnf = {self.configure().keys()}')
        self.config(image=self.img, command=self.my_click)

    def my_click(self):
        print(f'I am being clicked!')


# --------------------------------------------------------------------------------------------

# ניצור חלון
win = Tk()

win.geometry('600x600+700+100')

# ניצור את הכפתור שהגדרנו מראש
btn = MyButton(master=win)
btn.pack()

# נציג את החלון בלולאה
win.mainloop()
