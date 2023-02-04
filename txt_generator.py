def create():
    with open('txt_phone_book.txt', 'w') as page, open('phone_book.csv') as pb:
        while True:
            lines = pb.readline()
            if not lines:
                break
            page.write(lines.strip())
            page.write('\n')