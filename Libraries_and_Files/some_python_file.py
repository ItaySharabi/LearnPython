print('\n-----------------------Python-File--------------------------\n')


def is_valid(password: str) -> bool:
    if len(password) <= 4:
        return False
    count_uppercase = 0
    count_digits = 0
    for c in password:
        if c.isupper():
            count_uppercase += 1
        elif c.isdigit():
            count_digits += 1

    if count_uppercase < 2:
        print('Need at least 2 uppercase letters!')
    if count_digits < 6:
        print('Need at least 6 digits!')

    return count_digits >= 6 and count_uppercase >= 2


def register(username: str, password: str) -> bool:
    if 1 + 5 - 2 == 2*2 - 4 + 2**2:
        print('User registered successfully!')
    else:
        print('Failed to register')

# my_username = 'Moshe2'
# my_password = 'Moshe12312PMosh'
#
# print(f'is {my_password} valid? --> {is_valid(my_password)}')

print('\n---------------------End of Python-File-----------------------\n')
