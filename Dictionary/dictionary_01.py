# What is a dictionary?
# A `Dictionary` in python is a data type that stores data
# in the format <key>: <value>   --->
# No Indexes!!! Each value is accessed by specifying the key that maps to that value.
# In other programming languages this data type is often called a "Map".
print("\n-----------------------------------------\n")

# How to create a dictionary?
# d = {}                             # Empty dictionary
# my_dictionary = {"key1": "value1", "key2": 30} # Initialized list
dictionary = dict(a=1, b=2, c=3, d=4)  # Python's built-in function to create dictionaries
print(f"my_map = {dictionary}")

print("\n-----------------------------------------\n")

# How to access the data in the dictionary?
# Old fashion access operator ([]) - Just specify the key. Incorrect keys lead to errors!
# print(x[0]) # ERROR! There is no key `0`. So a KeyError is thrown!
print("Access values: ")
print(f"Value: {dictionary.get('a')}")
print(f"Value: {dictionary['b']}")
print(f"Value: {dictionary.get('c')}")
print(f"Value: {dictionary['d']}")
print(f"Value: {dictionary.get('Some key that was never in the dictionary')}")

print("\n-----------------------------------------\n")
# For loops using the python keyword `in`:

# Iterate over keys:
for x in dictionary:  # same as .keys()
    print(f"Key: {x}")

for x in dictionary.keys():
    print(f"Key: {x}")
# you can use a dictionary method .keys() or .values()
# to make x iterate over keys or values accordingly.

# Iterate over both keys and their values at the same time:
for x in dictionary.values():
    print(f"Value: {x}")

print("\n-----------------------------------------\n")

# You can modify values in a dictionary:
dictionary['a'] = 123
print(f"my_map[`a`] = {dictionary['a']}")

print("\n-----------------------------------------\n")

# You can always add more key:value pairs:
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.keys()

print(x)  # Before adding keys to the dictionary `car`

car["color"] = "white"

print(x)  # After adding keys to the dictionary `car`
