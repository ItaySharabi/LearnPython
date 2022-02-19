print("\n------------------------------------------\n")
# 1:
d = {
    'Noam': 'fish',
    'May': 'horse',
    'Daniel': 'dog',
    'Amit': 'cat',
    'Tal': 'snake',
    'Liam': 'bird',
    'Roni': 'cat'
}

print("\n------------------------------------------\n")

# 2:
print('Dan' in d)  # Prints False

print("\n------------------------------------------\n")

# 3:
if 'Roni' in d:
    print(f"Does Roni have a cat? -> {'cat' in d['Roni']}")

print("\n------------------------------------------\n")

# 4:
for key in d.keys():
    if 'fish' in d[key]:
        print(f"{key} has a fish!")

print("\n------------------------------------------\n")

# 5:
print("Names that start with A:")
for key in d.keys():
    if key[0] == 'A':
        print(key)

print("\n------------------------------------------\n")

# 6:
prices = {'Gold fish': 5, 'Black fish': 10, 'Aquarium (Small)': 50, 'Aquarium (Big)': 100}
cart = {'Gold fish': 3, 'Black fish': 2, 'Aquarium (Big)': 2}

total = 0

for key in cart.keys():
    total += prices[key] * cart[key]

print(f"Total cart price is: {total}")
