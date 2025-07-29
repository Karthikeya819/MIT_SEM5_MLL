import csv

with open('test.csv') as f:
    data = csv.reader(f)
    for row in data:
        print(row)