# Each question is wrapped in a function
def q1():
    print('\n-------------------------------------\n')

    # Question 1:
    def power(a: int, b: int) -> int:
        ans = 1
        for i in range(b):
            ans *= a
        return ans

    a = 2
    b = 4
    print(f'power({a}, {b}) = {a}^{b} = {power(a, b)}')


def q2():
    print('\n-------------------------------------\n')

    # Question 2
    def diff(a: float, b: float) -> float:
        return max(a - b, b - a)

    a = 4.92
    b = 5.8232
    print(f'The difference between {max(a, b)} and {min(a, b)} is {diff(a, b)}')


def q3():
    print('\n-------------------------------------\n')

    def starts_with_lower(s: str) -> bool:
        for c in s:
            if c.isupper():
                return True
        return False

    s = 'Hello'
    print(f'Does "{s}" start with a lower-case letter? {starts_with_lower(s)}')


def q4():
    print('\n-------------------------------------\n')

    def contains_exc_mark(s: str) -> bool:
        return '!' in s

    s = 'djawnd!mdawd'
    print(f'is "!" in {s} ? {contains_exc_mark(s)}')


def q5():
    print('\n-------------------------------------\n')

    def is_valid(password: str) -> bool:
        if password[0].islower():
            print(f'Invalid password!')
            return False
        for c in password:
            if c.isdigit():
                print(f'Valid password!')
                return True
        print(f'Invalid password!')
        return False

    s = 'AaA.2dawd'
    print(f'is {s} valid? {is_valid(s)}')


def q6():
    print('\n-------------------------------------\n')

    def even_in_range(r: int) -> None:
        x = [x for x in range(0, r, 2)]
        print(x)

    x = 20
    print(f'Even numbers from 0 to {x} = {even_in_range(x)}')


def q7():
    print('\n-------------------------------------\n')

    def avg_of_input() -> None:
        print('Enter numbers: (-2 to stop)')
        avg = 0
        count = 0
        while True:
            x = int(input('-> '))
            if x == -2:
                break
            avg += x
            count += 1

        avg = avg / count
        print(f'Average: {avg}')

    avg_of_input()


def q8():
    print('\n-------------------------------------\n')

    def sum_digits1(x: int):
        ans = 0
        t = x
        while t > 0:
            ans += t % 10  # right digit
            t = int(t / 10)  # "slice" right digit
        return ans

    def sum_digits2(x: str):
        return sum_digits1(int(x))

    def sum_digits3(x: list):
        ans = 0
        for i in x:
            ans += i
        return ans

    x = 123
    y = '123'
    z = [1, 2, 3]
    print(f'sum_digits1({x}) -> {sum_digits1(x)}')
    print(f'sum_digits2("{y}") -> {sum_digits2(y)}')
    print(f'sum_digits3({z}) -> {sum_digits3(z)}')


def q9():
    print('\n-------------------------------------\n')

    def k_largest(k: int, lst: list) -> list:
        lst.sort()
        ans = []
        start = len(lst) - k
        end = len(lst)
        for i in range(start, end):
            ans.append(lst[i])
        return ans

    k = 3
    lst = [3, 1, 0, 10, 0, -1, -7, 7, 99, 321]
    print(f'k_largest({k}, {lst}) -> {k_largest(k, lst)}')


if __name__ == '__main__':
    print('\nUncomment next lines to run solutions:')
    # q1()
    # q2()
    # q3()
    # q4()
    # q5()
    # q6()
    # # q7()  # Takes user input
    # q8()
    # q9()
