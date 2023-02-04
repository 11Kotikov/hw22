def input_check ():
    try:
        input_number = int(input('Please, choose one number from the menu: '))
        return input_number
    except ValueError:
        print('Error: Input a number, please')
        return input_check()