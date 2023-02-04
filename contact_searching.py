import os


def open_full_book():
    empty = 'phone_book.csv'
    if os.path.getsize(empty) == 0:
        print('The phone book is empty, please add at least one contact')
    else:
        with open('phone_book.csv') as pb:
            while True:
                lines = pb.readline()
                if not lines:
                    break
                print(lines.strip())


def contact_searching():
    empty = 'phone_book.csv'
    if os.path.getsize(empty) == 0:
        print('The phone book is empty, please add at least one contact')
    else:
        with open('phone_book.csv') as pb:
            search = input('Whose contact do you want to find?: ')
            lines = pb.readlines()
            for i, line in enumerate(lines):
                if search in line:
                    print('|{}| {}'.format(i+1, line))
                else:
                    print(
                        f'There are no such key-words as the "{search}", please check your input (including capital letters) and try again or chose "2. Show all contacts"')
