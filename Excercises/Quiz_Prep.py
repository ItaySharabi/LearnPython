# In this file we will be practicing some basic Python functionalities

# ---------------- Basics ------------------------------------------
ans = input("Output?")
for x in range(1, 11):
    print(f"x = {x}")

ans = input("Output?")

for y in range(1, 11, 2):
    print(f"y = {y}")

ans = input("Output?")

for y in range(0, 11, 2):
    print(f"y = {y}")

ans = input("Output?")

for i in "Python":
    print(f"i = {i}")

ans = input("Output?")
# lst = ["Python", "Java", "C", "C++"]
for z in ["Python", "Java", "C", "C++"]:
    print(f"z = {z}")
    for t in z:
        print(f"t = {t}")
# -------------------------------------------------------------------

# User input:

x = int(input("Please enter a number: "))

ans = input("Output?")
for i in range(x):
    if x % 2 == 0:
        if i % 2 == 1:
            print(f"i = {i}")
    elif x % 2 == 1:
        if i % 2 == 0:
            print(f"i = {i}")
# ---------------------------------------------------------------------
# lst = [x for x in range(1, 10)]
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

sum = 0
for i in range(len(lst)):
    sum += lst[i]

ans = input("Output?")
print(f"sum = {sum}")

# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum = 0
for i in lst:
    sum += i

ans = input("Output?")
print(f"sum = {sum}")

lst = []
for i in range(100):
    if i % 2 == 0:
        lst.append(i)

ans = input("Output?")
print(f"List size = {len(lst)}")


lst = []
for i in range(0, 100, 2):
    lst.append(i)

ans = input("Output?")
print(f"len(lst) = {len(lst)}")


# ---------------------------------------------------------------------

# Extra:
size = int(input("Please enter list size: "))
my_list = []

for i in range(size):
    my_list.append(((-1) ** i) * i)

ans = input("Output?")
print(f"list = {my_list}")
