# ייבוא קבצים/ספריות
import math
import random

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