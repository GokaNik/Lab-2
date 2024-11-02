from csv import reader
count=0
with open('books.csv','r') as csv_file:
    table = reader(csv_file,delimiter=';')
    for row in table:
        if len(row[1])>30:
            count+=1
print(count)