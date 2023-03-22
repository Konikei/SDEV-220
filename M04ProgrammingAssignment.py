import zoo as menagerie
import csv
import os

menagerie.hours()

with open('books.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['author'], row['book'])

#Dictreader didn't handle the quote the second one disappeared

print(os.getcwd())
