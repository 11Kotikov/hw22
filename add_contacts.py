def new_contact():
    first_name = input('Name: ')
    second_name = input('Surname: ')
    cellphone_number = input('mobile phone: ')
    homephone_number = input('home phone: ')
    comment = input('add comment: ')
    return {'Name': first_name, 'Surname': second_name,
            'Mobile': cellphone_number, 'Home number': homephone_number,
            'Note': comment}
def phone_book():
    with open('phone_book.csv', 'a+') as pb:
        for key,val in new_contact().items():
            pb.write('{}: {};'.format(key,val))
        pb.write('\n')