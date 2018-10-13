import os
import csv
csvpath = os.path.join('..', 'Resources', 'election_data.csv')
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    data = list(csvreader)
    row_count = len(data)
    print(row_count)
    
    count = 0
    for row in csvreader:
        count += 1
print(count)

   