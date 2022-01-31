# Some useful dictionary methods:
print("\n-----------------------------------------\n")

#
student = {
    'name' : "David",
    'age' : 16,
    'Math grade' : 100
}

print(f"student = {student}")


# Access operators:
# [] operator:
name = student['name']
print(f'name = {name}')

# .get() -> Runs a "safe" search inside the dictionary `student`:

age = student.get('age')
print(f"age = {age}")

# Why "Safe" search? Because using the [] operator with a non-existing key you get errors!
# age = student['Age'] # KeyError - The key is not found and the program is stopped!

print("\n-----------------------------------------\n")
# How many keys does that student object has?
print(f"len(student) -> {len(student)}\n")

# Find if a key exists in the dictionary:
print(f"Is `name` a key in our dictionary?")
print(f"print(`name` in student) --> {'name' in student}\n")
print(f"Is `English grade` a key in our dictionary?")
print(f"print(`English grade` in student) --> {'English grade' in student}")

print("\n-----------------------------------------\n")

# Adding to dictionaries:
student['Computer Science grade'] = 95
student['English grade'] = 90
student['History grade'] = 89
print(f"After adding key:value pairs: {student}")

# Removing from dictionaries:
x = student.popitem()  # removes and returns as (key,value) the last item that was added ('History grade` with value 89)
print(f"x = student.popitem() -> {x}")

x = student.pop('English grade')  # removes the key 'English grade' and its value and return the value
print(f"x = student.pop('English grade') -> {x}")
