#словарь
slovar = [
        {'name': 'Маша', 'age': 25, 'job': 'Scientist'}, 
        {'name': 'Вася', 'age': 8, 'job': 'Programmer'}, 
        {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
]

import csv
with open('export.csv', 'w', encoding='utf-8', newline='') as f:
    fields = ['name', 'age', 'job']
    writer = csv.DictWriter (f, fields, delimiter=';')
    writer.writeheader()
    for yacheika in slovar:
        writer.writerow(yacheika)