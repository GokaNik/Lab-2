from csv import reader
tags=set()
with open('books.csv') as csv_file:
    table=reader(csv_file,delimiter=';')
    for row in table:
        tags1=row[12].split('#')
        for i in tags1:
            if i!='':
                tags.add(i)
print(tags)
