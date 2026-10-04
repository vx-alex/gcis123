import csv
file = open("students.csv")
read = csv.reader(file)
next(read)
print(next(read))
