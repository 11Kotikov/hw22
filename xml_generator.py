def create():
    with open('xml_phone_book.xml', 'w') as page, open('phone_book.csv') as pb:
        page.write(
            '<?xml-stylesheet type="text/css" href="stylesheet.css"?>\n<message>\n <warning>\n')
        while True:
            lines = pb.readline()
            if not lines:
                break
            page.write(lines.strip())
            page.write('\n')
        page.write(' </warning>\n</message>\n')
