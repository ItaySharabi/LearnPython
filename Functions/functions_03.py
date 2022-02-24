def menu_opt1():
    print('Option 1 selected')


def menu_opt2():
    print('Option 2 selected')


def menu_opt3():
    print('Option 3 selected')


def menu_opt4():
    print('Option 4 selected')


def menu_opt5():
    print('Option 5 selected')


def menu():

    while True:

        user_input = int(input('Choose an option 1-5:\t(-1 To quit)'))
        if user_input == -1:
            break

        if user_input == 1:
            menu_opt1()

        elif user_input == 2:
            menu_opt2()

        elif user_input == 3:
            menu_opt3()

        elif user_input == 4:
            menu_opt4()

        elif user_input == 5:
            menu_opt5()
        else:
            print('Invalid option! Try again')

    print('Stopping program...')


menu()
