
# In this file we will introduce Python's List object

# רשימה בפייתון זה אובייקט שמכיל כל מיני טיפוסים שונים של מידע.

# דוגמאות ליצור רשימה ריקה
# Python program to demonstrate len(object)
lst = []
# print(f"The length of lst is: len(lst) = {len(lst)}")
lst.append("Hello")
lst.append("Python")
lst.append("Programmers!")
# print(f"The length of lst is: len(lst) = {len(lst)}")

# --------------------------------------------------------
my_list = []

# פונקציית הוספה לרשימה:
my_list.append("Hello, world!")
my_list.append(6)
my_list.append(lst)

# פונקציית מחיקה מרשימה:
my_list.pop()   # מוחק את האיבר האחרון ברשימה אם לא מציינים אחרת
my_list.pop(1)  # מוחק את האיבר במיקום שצויין
my_list.pop(-1) # -1 זה האינדקס הראשון מהסוף

# # עוד פונקציות שימושיות על רשימות בפייתון:
numbers = [100, -123, "Hello world!"]
# 1:
numbers.sort() # ממיינים מקטן לגדול
numbers.sort(reverse=False) # ממיינים מגדול לקטן
# 2:
numbers.reverse() # להפוך את סדר האיברים ברשימה
# 3:
numbers.count(-1) # נספור את מספר המופעים של (1-) בתוך הרשימה

# איך "רצים" על רשימות?

# For loops: Easier
for david in numbers: # כשרצים על רשימה, בכל פעם מקבלים איבר מהרשימה לתוך המשתנה של הלולאה
    # במקרה שלנו - david
    print(david)

for i in numbers:
    print(i)

# numbers[0, 1, ..., 29]
i = len(numbers) - 1
while i > 0:
    print(numbers[i])
    i -= 1

# While loops: Harder
i = 0
max_index = len(numbers) - 1

while i <= max_index:
    print(numbers[i])
    i += 1

# While loops: Harder
i = 0
max_index = len(numbers)
while i < max_index:
    i += 1