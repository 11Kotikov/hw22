def open_full_book():
    with open('phone_book.csv') as pb:
        while True:
            lines = pb.readline()
            if not lines:
                break
            print(lines.strip())


def contact_searching():

    with open('phone_book.csv') as pb:
        search = input('Whose contact do you want to find?: ')
        lines = pb.readlines()
        for i, line in enumerate(lines):
            if search in line:
                print('|{}| {}'.format(i+1, line))
            else:
                print('There are no such key-words, please check your input (including capital letters) and try again')
