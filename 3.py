import random
from csv import reader
from random import randint
output=open('result.txt','w')
a=[]
counter=0
for i in range(20):
    a.append(random.randint(1,9409))

with open('books.csv','r', encoding='windows-1251') as csv_file:
    table=reader(csv_file,delimiter=';')
    for row in table:
        counter+=1
        if counter in a:
            print(f'{counter}<{row[3]}> <{row[1]}> - <{row[6][6:10]}>')
            output.write(f'{counter}. <{row[3]}> <{row[1]}> - <{row[6][6:10]}>\n')
output.close





