# נשים לב מה קורה כאשר מנסים להכניס מספר ערכים בתור מפתח במילון:
dictionary = {}

# נכניס מספר ערכים בתור tuple לתוך המילון:
x, y, z = 10, 20, 30  # x = 10,   y = 20,    z = 30
dictionary[(x, y, z)] = x + y - z

print(dictionary)

x, y, z = 5, 2, 4
dictionary[(x, y, z)] = x + y - z

print(dictionary)

dictionary[x, y] = x
dictionary[y, z] = y
dictionary[4 * z] = z, z, z, z

print(dictionary)