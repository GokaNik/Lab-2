from csv import reader

search=input('Автор: ')
with open('books.csv','r') as csv_file:
    table=reader(csv_file,delimiter=';')
    for row in table:
        lower_case=row[3].lower()+' '+ row[4].lower()
        index=lower_case.find(search.lower())
        if index!=-1:
            if int(row[6][6:10])<2016:
                print(row[1])