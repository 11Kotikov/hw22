import os

def delete_contact ():
    with open('phone_book.csv') as pb, open('new_phonebook.csv', 'w') as npb :
        search = input('Whose contact do you want to delete?: ')
        for line in pb:
            if search not in line:
                npb.write(line)
    os.remove('phone_book.csv')
    os.rename('new_phonebook.csv', 'phone_book.csv')