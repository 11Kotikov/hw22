import input_checking as check
import html_generator as html
import xml_generator as xml
import txt_generator as txt


def export_in():
    print('Choose one of the options:\n \
1. Export in .HTLM\n \
2. Export in .XML\n \
3. Export in .TXT')
    number = check.input_check()
    if number < 0 or number > 3:
        print('Error: Wrong choise')
        check.input_check()
    else:
        if number == 1:
            html.create()
            print('html_phone_book.HTML file have been created')
        if number == 2:
            xml.create()
            print('xml_phone_book.XML file have been created')
        if number == 3:
            txt.create()
            print('txt_phone_book.TXT file have been created')
