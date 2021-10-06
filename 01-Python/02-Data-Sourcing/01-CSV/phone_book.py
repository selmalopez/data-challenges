import csv

with open('data/phone_book.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    #line_count = 0
    for row in csv_reader:
        #if line_count > 0:
        print(row['last_name'], int(row['phone_number']))
        #line_count += 1
