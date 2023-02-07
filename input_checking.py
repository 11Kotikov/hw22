def input_check():
    try:
        input_number = int(input('Please, choose one number from the menu: '))
        if input_number < 0 or input_number > 9:
            print('Error: Wrong choise')
            return input_check()
        else:
            return input_number
    except ValueError:
        print('Error: Input a number, please')
        return input_check()