print('\n-----------------------------------------------\n')


def create_student(name, school, age, grade) -> dict:
    student = {
        'Name': name,
        'School': school,
        'Age': age,
        'Grade': grade
    }

    return student


my_student = create_student('David', 'Rishonim', 13, '7th')
print(f'my_student = {my_student}')

print('\n-----------------------------------------------\n')


def special_arguments(**args):
    for i in args:
        print(i)


special_arguments(emp="Kelly", salary=9000)


def special_arguments(**args):
    for i in args.values():
        print(i)


special_arguments(emp="Kelly", salary=9000)


def create_student_easy(**student_args) -> dict:
    student = {}
    for key in student_args.keys():
        student[key] = student_args[key]
    return student


my_student = create_student_easy(name="David",
                                 age=15,
                                 grade="7th",
                                 lessons=['Math', "Computer Science", 'English'],
                                 height=1.70)
print(f'create_student_easy:\n{my_student}')

print('\n-----------------------------------------------\n')


def outer_fun(a, b):
    def inner_fun(c, d):
        return c + d

    return inner_fun(a, b)


res = outer_fun(5, 10)
print(res)
