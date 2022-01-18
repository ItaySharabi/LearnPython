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