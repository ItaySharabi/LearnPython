
print("Hello, class! Nice to meet you!")

# כתוב תכנית שתדפיס את כל המספרים מ- 1 עד 50.
# ליד כל מספר המתחלק ב- 8 יש להדפיס את המילה  “nice” ולרדת שורה.
name = "Itay"
age = 26
languages = ["Hebrew", "English"]
prog_languages = ["Python", "Java", "JavaScript", "C", "C++", "C#"]

# Easy Printing:
print(f"My name is {name},\nmy age is {age},\nI speak {languages},\nI write code in {prog_languages}!\n")

# לולאה המדפיסה מספרים המתחלקים ב-8
# for i in range(1, 51):
#     if i % 8 == 0:
#         print(f"{i}, nice")
#     else:
#         print(f"{i}")


# כתוב תכנית המדפיסה כל המספרים האי-זוגיים, מ- 1 ועד 50.
for i in range(1, 51):
    if i % 2 == 1:
        print(f"{i}")


# כתוב תכנית המדפיסה את כל המספרים הראשוניים בין 1 ל 100
# מזה ראשוני?
# מספר ראשוני מתחלק רק בעצמו או ב-1

print("Find Prime Numbers:")

# Primes: 2, 3, 5, 7, 11, 13, 17, 19, ............

# 1, 2, 3, 4, 5, ...., ..., 50, 51, ...., 10000, 10001, ....
print("Find primes using a `For Loop`")

# 2 הוא מספר מיוחד, הוא הראשוני הזוגי היחיד, וגם הכי קטן.
# לכן נדפיס את 2 בתור ראשוני בנפרד מכל שאר המספרים
print("2 is Prime!")

for i in range(3, 101):

    # i:= 3 -> 100: # נבדוק את כל המספרים
    #   j:= 3 -> (i-1): # עבור כל מספר שנבדוק, נבדוק אותו מול כל הקודמים שלו
    is_prime = True # אני מניח שהמספר שאני בודק הוא ראשוני
    for j in range(3, i):

        if i % j == 0:
            is_prime = False
            break

    if is_prime:    # == True
        print(f"{i} is Prime!")

# פתרון זהה בעזרת לולאת while יעשה את העבודה

print("Find primes using a `While Loop` (Same concept)")

i = 3
while i < 101:

    j = 3
    is_prime = True
    while j < i:
        if i % j == 0:  # If `j` divides `i`, then:
            is_prime = False
            break   # לא חייבים להשתמש - אבל המילה break תחסוך לנו בדיוקת מיותרות כאשר כבר גילינו שהמספר לא ראשוני
        else:
            j += 1  # Increase `j` by 1 and continue checking

    if is_prime:
        print(f"{i} is Prime!!!")
    i += 1
