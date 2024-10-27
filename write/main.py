import csv

name_1 = "Anna"
name_2 = "Victor"

data_names = ['Oleg', 'Vera', name_1, name_2]

with open('data.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(
        data_names
    )