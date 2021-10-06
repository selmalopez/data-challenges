import csv

with open('data/phone_book.csv', mode='r') as csv_file:
    csv_reader = csv.reader(csv_file)
    line_count = 0
    for row in csv_reader:
        #print(row[0],row[2])

        if line_count > 0:
            print(row[0], row[2])

        line_count += 1
