def user_interface ():
    hello_user = '######--This phone number book, hello dear "user_name"--######'
    print ('#'* len(hello_user))
    print ( '\n'+hello_user+'\n')
    print ('#'* len(hello_user))
    print (' \n \
0. New phone book (the old one will be deleted) \n \
1. Show all contacts \n \
2. Add a new contact \n \
3. Find a contact \n \
4. Delete a contact \n \
5. Change the "NAME" \n \
6. Change the "SURNAME" \n \
7. Change the phone number \n \
8. Export your phone book \n \
9. Quit from the phone book \n \
')

# def menu_button(user_choice):
#     print (f'You have chosen {user_choice}')
#     return user_choice