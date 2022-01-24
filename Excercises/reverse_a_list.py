
# כתבו קטע קוד שהופך את סדר האיברים ברשימה מהסוף להתחלה

# Solution 1:
# נכין רשימה לעבוד עליה:
my_list = [8, 2, -1, "Python!", "Hello"]

# ניצור רשימה חדשה - היא תהיה הפתרון של השאלה:
ans = []
for i in range(len(my_list)):
    ans.append(my_list[-1-i])

print(f"My first answer is: {ans}")


# Solution 2

# נשתמש בפונקציות מוכנות של רשימות בפייתון:
my_list.reverse() # הופך את האיברים שבתוך הרשימה
print(f"My second answer is: {my_list}")
