# def == define == להגדיר

def func1(x: int):  # בשורה זו מוגדרת פונקציה שמקבלת פרמטר x כלשהו ומחזירה None
    x = x + 1  # הפונקציה מבצעת חישוב מתמטי כלשהו
    print(x)   # (לרוב לא מדפיסה כלום)
    return x   # מחזירה את התוצאה לשורה שקראה לפונקציה


def func2(x):
    x = x + 1000
    print(x)
    return x


def do_something(z):
    print(z)
    z.pop()  # If `z` is not a list - then an ERROR will be raised!!
    print(z)
    return z


print(do_something([1, 2, 3, 4, 5]))
