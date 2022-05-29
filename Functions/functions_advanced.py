# כתבו פונקציה שמקבלת פרמטר lst
# שהוא רשימה של מספרים
# הפונקציה תחזיר את המספר המקסימלי ברשימה

def list_max(lst: list):
    _max = lst[0]

    for item in lst:
        if item > _max:
            _max = item
    return _max


my_list = [1, 2, 3, 4, 5]
print(list_max(my_list))  # 5
my_list = [1, 2, 3, 3, 4 ,5]
print(list_max(my_list))  # 5
my_list = [5, 4, 3, 2, 1, 1, 0]
print(list_max(my_list))  # 5
my_list = [-5, -4, -3, -2, -1, -1, 0]
print(list_max(my_list))  # 0


# כתבו פונקציה המקבלת מספר
# n = 0, 1, 2, 3, 4, ..., 100
# הפונקציה תחזיר את מספר פיבונאצ'י ה-n

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n >= 2:
        return fibonacci(n - 1) + fibonacci(n - 2)


def fib_improved(n: int):

    fibs = [0, 1]
    for i in range(2, n):  # i = 2
        fibs.append(fibs[i-1] + fibs[i-2])
    return fibs[n-1]



# print(fibonacci(0))
# print(fibonacci(1))
# print(fibonacci(2))
# print(fibonacci(3))
# print(fibonacci(4))
# print(fibonacci(5))
import time

n = 24
start_time = time.time()

# Recursive:
print(f'Calculating fibonacci({n})')
print("============================")
print(fibonacci(n))
print(f'The time to calculate fibonacci({n}) is {time.time() - start_time}')

# Improved:
start_time = time.time()
print(f'Calculating fibonacci({n})  (Improved!)')
print("============================")
print(fib_improved(n))
print(f'The time to calculate fibonacci({n}) is {time.time() - start_time}')