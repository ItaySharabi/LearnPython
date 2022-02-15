# שאלה 1: (כולל פתרון לדוגמה)
# כתבו פונקציה המקבלת רשימה.
# הפונקציה תחזיר את סכום כל המספרים ברשימה.
# תניחו שברשימה יש רק מספרים ולא מחרוזות למשל
def list_sum(x: list):
    total = 0
    for num in x:  # נעבור על כל המספרים ברשימה x
        total += num  # נוסיף כל מספר לסכום

    return total


# כעת ניתן לקרוא לפונקציה בשמה,
# בתוספת הרשימה שהיא מוגדרת לקבל:
my_list = [1, 2, 4, 8, 16]
x = list_sum([1, 2, 4, 8, 16])
print(f'The sum of all numbers in {my_list} is {x}')


# שאלה 2:
# # כתבו פונקציה המקבלת רשימה.
# הפונקציה תחזיר את מכפלת כל המספרים ברשימה.
def list_product(x):
    pass  # Remove the 'pass' before writing your code


# שאלה 3:
# # כתבו פונקציה המקבלת רשימה ושני אינדקסים.
# הפונקציה תחזיר את סכום המספרים שבין שני האינדקסים.
# לדוגמה:
# input: ([1, 2, 3, 4, 5], 2, 4 )
# output: 12
def list_inner_sum(x: list, a: int, b: int):
    pass  # Remove the 'pass' before writing your code


# שאלה 4:
# כתבו פונקציה המקבלת רשימה של מספרים
# הפונקציה תחזיר את המספר ברשימה הקרוב ביותר לממוצע
# כעת עליכם גם להמציא את "חתימת הפונקציה" (השם שלה והפרמטרים שהיא מקבלת, לעיתים גם מה היא מחזירה)


# שאלה 5:
# כתבו פונקציה המקבלת מחרוזת
# הפונקציה תחשב ותדפיס את מספר התווים שכתובים באות קטנה ומספר התווים באות גדולה
# לדוגמה:
# upper_lower_count("Hello") --> 4, 1
def upper_lower_count(x: str):
    pass  # Remove the 'pass' before writing your code
