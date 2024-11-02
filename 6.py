from csv import reader
counter=0
book_dict={}
mx=0

with open('books.csv') as csv_file:
    table=reader(csv_file,delimiter=';')
    for row in table:
        counter+=1
        if counter!=1:
            if row[1] in book_dict:
                book_dict[row[1]]+=int(row[8])
            else:
                book_dict[row[1]]=int(row[8])


for i in book_dict:
    if book_dict[i]>mx:
        mx=book_dict[i]
        most_pop=i
