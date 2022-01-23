
# In this file we will introduce Python's List object

# רשימה בפייתון זה אובייקט שמכיל כל מיני טיפוסים שונים של מידע.

# דוגמאות ליצור רשימה ריקה
lst = []
my_other_list = list()

# דוגמאות לאיתחול רשימה לא ריקה
lst = [9, -4, "Shalom", ((9*4)/3)]
my_other_list = list(["Shalom", "Olam", 6])

# --------------------------------------------------------
my_list = []

# פונקציית הוספה לרשימה:
my_list.append("Hello, world!")
my_list.append(6)
my_list.append(my_other_list)

# פונקציית מחיקה מרשימה:
my_list.pop()   # מוחק את האיבר האחרון ברשימה אם לא מציינים אחרת
my_list.pop(1)  # מוחק את האיבר במיקום שצויין
my_list.pop(-1) # -1 זה האינדקס הראשון מהסוף

# print(my_list)

# עוד פונקציות שימושיות על רשימות בפייתון:
numbers = [1, 2, 3, 4, 5]
# 1:
numbers.sort() # ממיינים מקטן לגדול
numbers.sort(reverse=False) # ממיינים מגדול לקטן
# 2:
numbers.reverse() # להפוך את סדר האיברים ברשימה
# 3:
numbers.count(-1) # נספור את מספר האיברים

# איך "רצים" על רשימות?

# For loops: Easier
for element in numbers:
    print(element)

# While loops: Harder
i = 0
max_index = len(numbers) - 1 # למה פחות 1? כי אינדקסים מתחילים מ-0.

while i <= max_index:
    print(numbers[i])
    i += 1

# While loops: Harder
i = 0
max_index = len(numbers)
while i < max_index:
    i += 1

