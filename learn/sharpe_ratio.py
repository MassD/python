import csv

def csv_rows(file):
    with open(file, "rb") as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            print ', '.join(row)
