# כאשר כותבים קובץ פייתון ורוצים להשתמש בספריות חיצוניות
# נקדיש את שורות הקוד הראשונות בד"כ כדי להצהיר על הקבצים והספריות בהם נשתמש
import math  # ייבוא הספריה לשימוש בכלים מתמטיים

print('The number `pi`, comes from the `math` library: ', math.pi)


# יש הרבה יכולות בייבוא ספריות חיצוניות בפייתון.
# נוכל להגדיר פונצקיות שמשתמשות בפונקציות של ספריות חיצוניות:
def multiply_by_pi(x: float) -> float:
    ans = math.pi * x
    return ans


# עכשיו נוכל לקבל תוצאת חישוב של פאי כפול כל מספר שנרצה
x = 2
print(f' (pi * {x}) = {multiply_by_pi(x)}')

# נוכל לייצר מספרים רנדומאליים:
import random as r

rand_numbers = []
for i in range(10):
    rand_numbers.append(r.randint(1, 11))  # Append random numbers between 1 - 10.
print(f'random numbers: {rand_numbers}')
# print(f'random numbers: {[r.randint(1, 11) for i in range(10)]}')
