import os
import csv
csvpath = os.path.join('..', 'Resources', 'budget_data.csv')
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    total = 0
    for row in csvreader:
        p_l = row[1]
        try:
            p_l = int(p_l)
        except ValueError:
            p_l = 0
        total += p_l
print("Total Revenue:", total)

myList = row[0]
print(len(myList))

datelist = []
datelist.append(row[0])
print(len(datelist))
