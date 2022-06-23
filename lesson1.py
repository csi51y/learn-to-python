from car import Car
from electric_car import ElectricCar

# Глава 2.
# Переменные и простые типы данных


first_name = "ADA "
name = first_name + "loveLace"  # конкатенация.
print(name.title())
print(name.upper())
print(name.lower())

# Функции rstrip(), lstrip() и strip() удаляют пробелы справа, слево и с
# обеих сторон переменной соответственно. a = " A"; a = a.lstrip()
# >>> a = "A"

print((2 + 1) ** 2)  # возведение в степень обозначается **.

print("Happy " + str(23) + "rd Birthday!")


# Глава 3.
# Списки


# Список - это набор элементов, следующих в определенном порядке.

bicylces = ['treck', 'cannondale', 'redline', 'specialized']
print(bicylces[-1].title())  # элемент с индексом -1 является последним
# в списке.
print("My first bicycle was a " + bicylces[-2].title() + ".")

bicylces.append('stork')  # метод append() добавляет новый элемент в
# конец списка.
bicylces.insert(0, 'stels')  # метод insert() добавляет новый элемент в
# произвольную позицию списка.
print(bicylces)

del bicylces[4]  # метод del удаляет элемент из списка по его индексу.
# Удаленное значение становится недоступным для использования.
print(bicylces)
bicylces.pop(0)  # метод pop() удаляет последний элемент из списка, если
# не указать индекс, но позволяет работать с ним после удаления.
last_element = bicylces.pop()
print(bicylces, last_element + ", " + bicylces.pop(0))

bicylces.remove('cannondale')  # метод remove() удаляет элемент из
# списка по его значению, не позволяя работать с удаленным элементом.
print(bicylces)
# Метод remove() удаляет только первое вхождение заданного значения.

# Если не все значения записаны в нижнем регистре, алфавитная сортировка
# списка усложняется.
cars = ['toyota', 'audi', 'bmw', 'subaru']
cars.sort()  # метод sort() позволяет сортировать списки.
print(cars)
cars.sort(reverse=True)  # с параметром reverse=True метод sort()
# отсортирует список в обратном алфавитном порядке.
print(cars)

print(sorted(cars))  # метод sorted() сортирует список не изменяя
# порядок элементов в списке. Возможно использовать
# параметр reverse=True.

cars = ['toyota', 'audi', 'bmw', 'subaru']
cars.reverse()  # метод reverse() предоставляет элементы списка в
# обратном порядке.
print(cars)

print(len(cars))  # метод len() определяет длину списка.


# Глава 4.
# Работа со списками.


magicians = ['alice', 'david', 'caroline']
for i in magicians:
    print(i)

for value in range(1, 5):  # функция range() выведет числа от 1 до 4.
    print(value)
even_numbers = list(range(2, 11, 2))  # функция list() преобразует
# результат функции range() в список. Функция range() начинает с
# числа 2, а затем увеличивает его на 2.
print(even_numbers)
digits = range(0, 10)
print(min(digits), max(digits), sum(digits))  # функции min() выводят
# max() минимальное и максимальное значение в списке, функция sum() -
# сумму всех значений.

squares = [value**2 for value in range(1, 11)]  # генератор списков
# (list comprehension) позволяет сгенерировать список квадратов и
# автоматически присоеденить все новые элементы с помощью цикла for,
# используя всего одну строку кода.
print(squares)

print(squares[1:4])  # срезы (slices) позволяют получить подмножество
# списка.
new_squares = squares[:]  # копирование списка с помощью среза позволяет
# создать новый список независимый от изначального. При копировании без
# использования срезов списки будут связаны.

dimensions = (200, 50)  # кортежи (tuples) - список элементов, которые
# невозможно изменить.
print(dimensions)
dimensions = (300, 150)  # хотя элементы кортежа не изменить, можно
# присвоить новое значение переменной, в которой хранится кортеж.
# dimensions[0] = 300 - выдаст ошибку.
print(dimensions)


# Глава 5.
# Команды if.


print(150 in dimensions)  # проверка вхождения значения в список.
banned_users = ['andrew', 'caroline', 'david']
if 'marie' not in banned_users:  # проверка отсутствия значения в
# списке.
    print('marie'.title() + " you can post a response if you wish.")
else:
    print("you're banned.")


# Глава 6.
# Словари.


# Любой объект, создаваемый в Python, может стать значением в
# словаре (dictionary).
alien_0 = {
    'color': 'green',
    'points': 5,
    }
print(alien_0['color'])
alien_0['attitude'] = 'enemy'  # добавление новой пары "ключ-значение".
print(alien_0)
alien_0['color'] = 'yellow'  # изменение значения в словаре.
del alien_0['attitude']  # удаление пары "ключ-значение".
print(alien_0)

for key, value in alien_0.items():  # метод items() возвращает список
# пар "ключ-значение".
    print(key + ", " + str(value))
# Метод keys() возвращает список ключей словаря, метод values() - список
# значений.
for k in sorted(alien_0.keys()):  # порядок получения элементов из
# словаря непредсказуем. Для получения упорядоченной копии ключей можно
# воспользоваться функцией sorted().
    print(k)
# Множества (set) похоже на список, но все его элементы должны быть
# уникальными.
alien_1 = {
    'color': 'red',
    'points': 15,
    }
aliens = [alien_0, alien_1]  # вложение словарей в список.
for alien in aliens:
    print(alien)


# Глава 7.
# Ввод данных и циклы while.


# message = input("Please enter your name: ")  # функция input()
# интерпретирует все данные, введенные пользователем, как строку.
# print("Hello, " + message + "!")
# age = input("How old are you? ")
# print(int(age) > 18)  # функция int() интерпретирует строку как число.

# message = ""
# while message != "quit":
#     message = input("Enter 'quit' to end the program. ")


# Глава 8.
# Функции.


def greet_user(username):
    """Выводит простое приветствие."""  # тройные кавычки обозначают
    # строку документации.
    print("Hello, " + username.title() + "!")
greet_user('jesse')  # username - параметр, а jesse - аргумент.
# Выше приведен пример поцизионной передачи аргументов.
# great_user(username='jesse')  # именованные аргументы.
# def greet_user(username='jesse')  # значение по умолчанию.
# def greet_user(username='')  # необязательный аргумент.

# def greet_user(*username)  # передача произвольного набора аргументов.
# Python создает пустой кортеж с именем username, куда упаковываются все
# полученные значения.
# def greet_user(**username)  # произвольный набор именованных
# аргументов. Python создаст пустой словарь для упаковки всех значений.

# import имя_модуля  # необходимо использовать точечную нотацию.
# from имя_модуля import имя_функции_0, имя_функции_1
# from имя_модуля import имя_функции as псевдоним
# import имя_модуля as псевдоним


# Глава 9.
# Классы.


class Dog():
    """Простая модель собаки."""

    def __init__(self, name, age):
        """Инициализирует атрибуты name и age."""
        self.name = name
        self.age = age

    def sit(self):
        """Собака садиться по команде."""
        print(self.name.title() + " is now sitting.")
    def roll_over(self):
        """Собака перекатывается по команде."""
        print(self.name.title() + " rolled over!")
# Функция, являющаяся частью класса, называется методом.
# Метод __init__ автоматически выполняется при создании каждого нового
# экземпляра класса.
# Параметр self обязателен в определении метода. При каждом вызове
# метода, связанного с классом, автоматически передается self - ссылка
# на экземпляр. Она предоставляет конкретному экземпляру доступ к
# атрибутам и методам класса.
# Любая переменная с префиксом self доступна для каждого метода в
# классе.
# Переменные, к которым обращаются через экземпляры, тоже называются
# атрибутами.
my_dog = Dog('willie', 6)
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years olds.")
my_dog.sit()

class Poodle(Dog):
    """Простая модель пуделя."""
    def __init__(self, name, age):
        """Инициализирует атрибуты класса-родителя."""
        super().__init__(name, age)
my_poodle = Poodle('willie', 7)
print("My dog is " + str(my_poodle.age) + " years olds.")
# Класс-родитель называют суперклассом, а класс-потомок - сублкассом.

# from car import Car
# from electric_car import ElectricCar
my_beetle = Car('volkswagen', 'beetle', '2016')
print(my_beetle.get_descriptive_name())
my_tesla = ElectricCar('tesla', 'roadster', '2016')
print(my_tesla.get_descriptive_name())

# Класс OrderedDict из модуля collections позволяет создать словарь,
# сохраняющий порядок добавление пар "ключ-значение".


# Глава 10.
# Файлы и исключения.


file_path = 'C:\Programming Language\Programming\Python'
file_path += r'\python_work\text_files\pi_digits.txt'  # абсолютные пути
# обычно длинее относительных, поэтому их лучше сохранять в переменных.
with open(file_path) as file_object:
    contents = file_object.read()
    print(contents)
# Python сохраняет объект, представляющий файл, в переменной
# file_object.
# Конструкция с словом with закрывает файл после того, как он становится
# ненужным. Файлы можно открывать и закрывать явными вызовами open() и
# close().
# Метод read() читает все содержимое файла и сохраняет его содержимое в
# одной длинной строке переменной contents. В конце вывода появилась
# лишняя пустая строка. Метод read() возвращает ее при чтении, если
# достигнут конец файла. Избавиться от нее можно методом rstrip().

with open(file_path) as file_object:
    for line in file_object:  # чтение файла по строкам.
        print(line.rstrip())
# Без использования метода rstrip() пустые строки появятся после каждого
# вызова, поскольку каждая строка в текстовом файле завершается
# невидимым символом новой строки.

# При использовании with объект файла, возвращаемый вызовом open(),
# доступен только в пределах содержащего его блока with. Для получения
# доступа к содержимому файла за пределами блока with, сохраните строки
# файла в списке, внутри блока и в дальнейшем работайте с полученным
# списком.
with open(file_path) as file_object:
    lines = file_object.readlines()  # метод readlines() последовательно
# читает каждую строку из файла и сохраняет ее в списке.
for line in lines:
    print(line.rstrip())
# Читая данные из текстового файла, Python интерпретирует весь текст в
# файле как строку.
# Метод replace() может использоваться для замены любого слова в строке
# другим словом.

file_path = 'C:\Programming Language\Programming\Python'
file_path += r'\python_work\text_files\programming.txt'
with open(file_path, 'w') as file_object:
    file_object.write("I love programming.\n")
# При вызове open() вторым аргументом передается 'w', это сообщает
# Python, что файл должен быть открыт в режиме записи. Файлы можно
# открывать в режиме чтения 'r', записи 'w', присоединения 'a' или в
# режиме, допускающем как чтение так и запись в файл 'r+'. Если аргумент
# режима не указан, Python по умолчанию открывает файл в режиме только
# для чтения.
# Если файл, открываемый для записи существует, то Python уничтожит
# его данные перед возвращением объекта файла.
# Функция write() не добавляет символы новой строки в записываемый файл.
with open(file_path, 'a') as file_object:
    file_object.write("I love creating new games.\n")

# Исключения используются в Python для управления ошибками, возникающими
# в ходе выполнения программы.
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero")
else:
    print("You will never see it")  # блок else выполняется, если блок
# try был успешно выполнен, то есть когда ошибок не возникло.
filename = 'alice.txt'
try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = 'Sorry, the file ' + filename + ' does not exist.'
    print(msg)
    # pass  ## команда pass ничего не делает.
# Пример с сохранением данных в формате json в файле remember_me.py
