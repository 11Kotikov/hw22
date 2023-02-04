# clear_contacts = {'Name': ' ', 'Surname': ' ',
#                   'Mobile': ' ', 'Home number': ' ', 'Note': ' '}


def new_clear_book():
    # global clear_contacts
    with open('phone_book.csv', 'w') as pb:
        # for key, val in clear_contacts.items():
        #     pb.write('{}: {}; '.format(key, val))
        pb.write('')