import user_interface as ui
import new_phone_book as npb
import add_contacts as ac
import contact_searching as cs
import delete_contacts as dc
import input_checking as check
# import change name, surname, phone
import export_contacts as export
# import contacts_import as ci


def output_hub():
    ui.user_interface()
    number = check.input_check()
    # if number < 0 or number > 9:
    #     print('Error: Wrong choise')
    #     check.input_check()
    if number == 0:
        npb.new_clear_book()
        print('You have created a new clean phone book!')
    elif number == 1:
        cs.open_full_book()
    elif number == 2:
        ac.add_to_phone_book()
        print('A new contact has been created')
    elif number == 3:
        cs.contact_searching()
    elif number == 4:
        dc.delete_contact()
        print('The contact has been deleted')
    elif number == 5:
        print ('Sorry, this function is not ready yet')
        output_hub()
    elif number == 6:
        print ('Sorry, this function is not ready yet')
        output_hub()
    elif number == 7:
        print ('Sorry, this function is not ready yet')
        output_hub()
    elif number == 8:
        export.export_in()
    elif number == 9:
        print('Good bye!')
        exit()
