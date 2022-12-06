import csv

people = [
    {'name': 'Маша', 'age': 25, 'job': 'Scientist'}, 
    {'name': 'Вася', 'age': 8, 'job': 'Programmer'}, 
    {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
    ]

with open('people.csv', 'w', encoding='utf-8') as my_file:
    header_list = ['name', 'age', 'job']
    writer = csv.DictWriter(my_file, header_list, delimiter=';')
    writer.writeheader()
    for user in people:
        writer.writerow(user)