# def == define == להגדיר

def func1(x):
    x = x + 1
    print(x)
    return x

def func2(x):
    x = x + 1000
    print(x)
    return x

# x = 8

def func3(y):
    print(f'Our global x: {x}')
# איך נשתמש בפונקציה?
func1(1000)
func2(2000)
func3(3000)
x = 8

