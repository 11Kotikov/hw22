

def create():
    with open('html_phone_book.html', 'w') as page, open('phone_book.csv') as pb:
        page.write('<html>\n  <head></head>\n  <body>\n')
        while True:
            lines = pb.readline()
            if not lines:
                break
            page.write('<p style="font-size:30px;">')
            page.write(lines.strip())
            page.write('</p>\n')

        page.write(' <body>\n<html>\n')