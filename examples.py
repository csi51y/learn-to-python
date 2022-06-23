import csv

l1 = ['111', '222']
l2 = ["333", "444", "555", "666"]
l = [l1, l2]
ll = [l, l]
dh = ['header1', 'header2']
d = {'header1': l1, 'header2': l2}
d1 = {'header1': 'one', 'header2': 'two'}
d2 = [
    {'header1': 'one', 'header2': 'two'},
    {'header1': 'three', 'header2': 'four'}
    ]

prod_header = ['Наименование', 'Цена']
products = [
    ['товар1', '10'], ['товар2', '20'],
    ['товар3', '30'], ['товар4', '40']
    ]

file_path = r'C:\Programming Language\Programming\Python\\'
file_path += r'python_work\csv_files\test.csv'

with open(file_path, 'w', newline='') as file_object:
    writer = csv.writer(file_object, quoting=csv.QUOTE_NONE)
    writer.writerow(prod_header)
    writer.writerows(products)
    # writer = csv.DictWriter(file_object, dh)
    # writer.writeheader()
    # writer.writerow(d1)

f_p = r'C:\Programming Language\Programming\Python\\'
f_p += r'python_work\csv_files\\'
f_p += 'test2.csv'
def write_to_file(f_path, l):
    with open(f_path, 'w', newline='') as file_obj:
        writer = csv.writer(file_obj)
        writer.writerows(l)

with open(file_path, 'r') as file_object:
    reader = csv.reader(file_object)
    result = []
    for i, row in enumerate(reader):
        if i == 0: continue
        result.append(int(row[1]))
    write_to_file(f_p, [['Итого', sum(result)]])
