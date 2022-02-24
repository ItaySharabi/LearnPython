





# נשים לב מה קורה כאשר מנסים להכניס מספר ערכים בתור מפתח במילון:
dictionary = {}

# נכניס מספר ערכים בתור tuple לתוך המילון:
x, y, z = 10, 20, 30  # x = 10,   y = 20,    z = 30
dictionary['A'] = x + y - z
dictionary[x, y, z] = x + y - z


print(dictionary)
print('\n-------------------------------------\n')


x, y, z = 5, 2, 4
dictionary[(x, y, z)] = x + y - z

print(dictionary)

dictionary[x, y] = x
dictionary[y, z] = y

dictionary[4*z, ' '] = z, z, z, z

print(dictionary)


# תרגיל:
# כתבו פונקציה בשם:
# f(x)
# המקבלת מספר x
# Write a function f(x)
# f(x) will return x+3

# Write a function g(x)
# g(x) will return x^3

# Write a function fog(x)
# fog(x) will return the same value as applying g(x)=y and then f(y) = f(g(x)).
# fog(x) = f(g(x))

def f(x):
    return x + 3


def g(x):
    return x ** 3


def fog(x):
    return f(g(x))


x = 1
print(f'x = {x}\n'
      f'f({x}) = {f(x)}\n'
      f'g({x}) = {g(x)}\n'
      f'fog({x}) = f(g({x})) = f({g(x)}) = {fog(x)}')
