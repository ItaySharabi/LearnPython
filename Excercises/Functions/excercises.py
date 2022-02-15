print('\n-----------------------------------------------\n')


def create_student(name, school, age, grade) -> dict:
    student = {
        'Name': name,
        'School': school,
        'Age': age,
        'Grade': grade
    }

    return student


my_student1 = create_student('David', 'Rishonim', 13, '7th - 1')

my_student2 = create_student('Daniel', 'HaRishonim', 12, '7th - 3')

print(f'my_student = {my_student1}')
print(f'my_student = {my_student2}')

print('\n-----------------------------------------------\n')


def special_arguments(**args):
    print(args)
    for i in args.values():
        print(i)


special_arguments(a=1, b='Hello', c=123712)


def special_arguments(**args):
    for i in args.values():
        print(i)


special_arguments(emp="Kelly", salary=9000)


def create_student_easy(**student_args) -> dict:
    student = {}
    for key in student_args.keys():
        student[key] = student_args[key]
    return student


x = create_student_easy(name='David', school='HaRishonim', age=24, grade='7th -3')
my_student = create_student_easy(name='Moshe', school='HaRishonim', age=24, grade='7th -3')

my_student = create_student_easy(name="David",
                                 age=15,
                                 grade="7th",
                                 lessons=['Math', "Computer Science", 'English'],
                                 height=1.70)
print(f'create_student_easy:\n{my_student}')

print('\n-----------------------------------------------\n')


def outer_fun(a, b):
    print('Hello, outer function!')
    print('Some calculations')

    def inner_fun(c, d):
        return c + d

    return inner_fun(a, b)


res = outer_fun(5, 10)
# inner = inner_fun()
print(res)


# כתבו פונציה שמקבלת שני מספרים
# הפונקציה תחזיר את סכום המספרים, ההפרש ביניהם והמכפלה שלהם
def operations(a, b) -> tuple:
    return (a + b, a - b, a * b)


print(operations(3, 8))
