# ייבוא קבצים / ספריות
import math
import random

# השימוש בלולאות הוא כלי מאוד מועיל בכתיבת קוד והוא תורם לקוד קריא וקצר
# המסוגל לבצע קטעי קוד ארוכים
# למשל:
# נרצה לחשב את הסכום של כל המספרים מ-1 עד 1000:
# 1 + 2 + 3 + 4 + ... + 998 + 999 + 1000
# בעצם נרצה לבצע "לולאת קוד" המחשבת 1 + 2,
# שומרת את התוצאה,
# מוסיפה 3, מוסיפה 4, ..., מוסיפה 1000, ומחזירה את התוצאה.
# סיום ביצוע הקוד שבתוך הלולאה פעם אחת נקרא "איטרציה"

result = 0
for i in range(1001):
    result = result + i
    # result += i
    # result += (i+1)
    if i % 200 == 0: # אם i מתחלק ב-200: זה קורה 5 פעמים בין 1 ל 1000 ובגלל זה בחרתי להשתמש בזה
        print(f"i = {i}, result so far = {result}")
    # end of iteration - סיום האיטרציה
# בסוף הלולאה בדרך כלל נחזיר לאנשהו את התוצאה. כרגע נסתפק בהדפסה
print(f"result (for loop) = {result}")
a = 1
b = 1000
print(f"# Math trick: (a = 1, b = 1000)\n\t{a} + {a+1} + ... + {b} = \n"
      f"\t = [(a+b)(b-a+1)]/2 = \n"
      f"\t = {int((a+b)*(b-a+1)*(1/2))}\n-------------------------------------------------")

# אותו החישוב בלולאת while
result = 0
i = 1
while i <= 1000:
    result = result + i
    # result += i
    # result += (i+1)
    if i % 200 == 0: # אם i מתחלק ב-200: זה קורה 5 פעמים בין 1 ל 1000 ובגלל זה בחרתי להשתמש בזה
        print(f"i = {i}, result so far = {result}")

    i += 1 # חייבים תמיד לזכור לקדם את המשתנה שלולאת ה-while תלויה בו!
    # end of iteration - סיום האיטרציה
print(f"result (while loop) = {result}")

# -----------------------------------------------------------------------------------------------

# לולאת for בפייתון מתאתרת מעבר על מבנה כלשהו שמכיל נתונים
# נתונים: int, double, string, ...
# ללואות for ב-Python יש מבנה מאוד פשוט:
data_set = {1, 2, 3}
# [המבנה שרצים עליו] in [משתנה זמני מתוך המבנה] for
for temp_var in data_set:
    print("do something with temp_var...")
    print(f"temp_var = {temp_var}...")

# סך הכל עוברים על "מבנים" מסויימים ואוספים את הערכים שלהם לתוך משתנה/ים זמני/ים
# Examples:

for i in range(1,10):
    print(f"i = {i}")

print("------------------------------------\n")

for x in {1, 3, 5, 7, 9}:
    print(f"x = {x}")

print("------------------------------------\n")

for some_variable_name in {"banana", "apple", "watermelon"}:
    print(f"Variable name after `for` does not matter - it holds a data item in each iteration\n"
          f"var = {some_variable_name}")

print("------------------------------------\n")

# create a list
my_list = []
# my_list = list()

# append some normal items:
my_list.append(3)
my_list.append(14)
my_list.append("banana")
my_list.append("pi = " + str(math.pi))

for item in my_list:
    print(f"item = {item}")

print("------------------------------------\n")

for i in range(len(my_list)):
    print(f"i = {i}")
    print(f"my_list[{i}] = {my_list[i]}")

print("------------------------------------\n")

random_list = []
rand_number = random.randint(5, 10)

for i in range(rand_number):
    random_list.append(random.randint(1, 100))
for i in range(len(random_list)):

    for j in range(len(random_list)):
        if random_list[i] < random_list[j]:
            temp = random_list[i]
            random_list[i] = random_list[j]
            random_list[j] = temp
print(f"List after Bubble Sort = {random_list}")