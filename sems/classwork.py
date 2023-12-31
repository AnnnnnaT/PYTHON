# Пользователь вводит данные. Сделайте проверку данных
# и преобразуйте если возможно в один из вариантов ниже:
# ✔ Целое положительное число
# ✔ Вещественное положительное или отрицательное число
# ✔ Строку в нижнем регистре, если в строке есть
# хотя бы одна заглавная буква
# ✔ Строку в нижнем регистре в остальных случаях


# a = input("Input: ")
# if  isinstance(a, int) and int(a) > 0:
#     print(int(a))
# elif isinstance(a, float):
#     print(float(a))
# elif any(i[0].isupper() for i in a):
#     print(a.lower())
# else:
#     print(a.lower())

# ✔ Создайте вручную кортеж содержащий элементы разных типов.
# ✔ Получите из него словарь списков, где:
# ключ — тип элемента,
# значение — список элементов данного типа.

# from pprint import pp

# a = (3, True, 'egfwe', 7.14, (5, 6, 7), {'a': 4, 'b': 5}, [None], 5, 6, 54)
# dict = {}
# for item in a:
#     if type(item) not in dict:
#         dict[type(item)] = []
#     dict[type(item)].append(item)
# pp (dict)

# ✔ Создайте вручную список с повторяющимися элементами.
# ✔ Удалите из него все элементы, которые встречаются дважды.

import json
import random 
# a = [random.randint(0,10) for _ in range(20)]
# print(a)
# for i in a:
#     if a.count(i) == 2:
#         while i in a:
#             a.remove(i)
# print(a)


# Создайте вручную список с повторяющимися целыми числами.
# ✔ Сформируйте список с порядковыми номерами
# нечётных элементов исходного списка.
# ✔ Нумерация начинается с единицы.

# a = [random.randint(0,10) for _ in range(20)]
# print(a)
# for i in range(len(a)):
#     if a[i]%2 != 0:
#         print(i+1)
    

# Пользователь вводит строку текста. Вывести каждое слово с новой строки.
# ✔ Строки нумеруются начиная с единицы.
# ✔ Слова выводятся отсортированными согласно кодировки Unicode.
# ✔ Текст выравнивается по правому краю так, чтобы у самого длинного
# слова был один пробел между ним и номером строки.

# a = "dhef fhejf kefjeyruije"
# lst = a.split()
# lst.sort()
# for i in range(len(lst)):
#     if len(lst[i]) == len(max(lst, key = len)):
#         print(f'{i+1}. {lst[i]}')
#     else:
#         print(f'{i+1}. {lst[i]:>{len(max(lst, key = len))}}')  # выравниваем по правому краю по ширине самого длинного слова


# Пользователь вводит строку текста.
# ✔ Подсчитайте сколько раз встречается
# каждая буква в строке без использования
# метода count и с ним.
# ✔ Результат сохраните в словаре, где ключ —
# символ, а значение — частота встречи
# символа в строке.
# ✔ Обратите внимание на порядок ключей.
# Объясните почему они совпадают
# или не совпадают в ваших решениях.

# a = input("Input: ")
# count = 0
# res = {}
# res_2 = {}

# for i in a:
#         res[i] = res.get(i,0) + 1        
# print(res)


# for i in a:
#         res_2[i] = a.count(i)
# print(res_2)

# Напишите функцию, которая принимает строку текста.
# Вывести функцией каждое слово с новой строки.
# ✔ Строки нумеруются начиная с единицы.
# ✔ Слова выводятся отсортированными согласно кодировки Unicode.
# ✔ Текст выравнивается по правому краю так, чтобы у самого
# длинного слова был один пробел между ним и номером строки.

# ✔ Напишите функцию, которая принимает строку текста.
# ✔ Сформируйте список с уникальными кодами Unicode каждого
# символа введённой строки отсортированный по убыванию.

# stroka = "dsghewgydehd uweyew jjryyy"

# def unicode_func(a: str):
#     res = []
#     for i in set(a):
#         res.append(ord(i))
#     res = sorted(res, reverse = True)
#     return res

# print(unicode_func(stroka))

# ✔ Функция получает на вход строку из двух чисел через пробел.
# ✔ Сформируйте словарь, где ключом будет
# символ из Unicode, а значением — целое число.
# ✔ Диапазон пар ключ-значение от наименьшего из введённых
# пользователем чисел до наибольшего включительно.

# a = input("Input your numbers: ")

# def chars_dict(a: str):
#     new_a = list(map(int, a.split()))
#     new_a.sort()   
#     res = {chr(int(i)): int(i) for i in range(new_a[0], new_a[1] + 1)}
#     return res
# # или
#     res = sorted([int[i] for i in a.split()])
#     return {chr(i) : i for i in range(res[0], res[1] + 1)}

# print(chars_dict(a))


# ✔ Функция принимает на вход три списка одинаковой длины:
# ✔ имена str,
# ✔ ставка int,
# ✔ премия str с указанием процентов вида «10.25%».
# ✔ Вернуть словарь с именем в качестве ключа и суммой
# премии в качестве значения.
# ✔ Сумма рассчитывается как ставка умноженная на процент премии. 

# name = ["Tom", "Jack", "Sara", "Mary"]
# salary = [200, 50 , 60, 70]
# bonus = ["10.25%", "5%", "7.1%", "6%"]

# def make_dict(a: list, b: list, c: list):
#     c = [float(i.replace("%"," "))/100 for i in c]
#     res = { name : salary*bonus for name, salary, bonus in zip(a, b, c, strict = False) }
#     return res

# print(make_dict(name, salary, bonus))

# ✔ Функция получает на вход список чисел и два индекса.
# ✔ Вернуть сумму чисел между между переданными индексами.
# ✔ Если индекс выходит за пределы списка, сумма считается
# # до конца и/или начала списка.
# def do_sum(lst: list[int], start: int, stop: int):
#     res = 0
#     if stop > len(lst):
#         for i in range (start, len(lst)):
#            res += lst[i]
#     else:
#         for i in range (start, stop):
#             res += lst[i]
#     return res


# lst = [1,7,3, 0, 8, 9, 10]
# print(do_sum(lst, 0, 3))

# ✔ Функция получает на вход словарь с названием компании в качестве ключа
# и списком с доходами и расходами (3-10 чисел) в качестве значения.
# ✔ Вычислите итоговую прибыль или убыток каждой компании. Если все компании
# прибыльные, верните истину, а если хотя бы одна убыточная — ложь.
# def revenue(company: dict):
#     for _ in company.values():
#         sum(company.values)
#     res = filter(company,)

# ✔ Пользователь вводит строку из четырёх
# или более целых чисел, разделённых символом “/”.
# Сформируйте словарь, где:
# ✔второе и третье число являются ключами.
# ✔первое число является значением для первого ключа.
# ✔четвертое и все возможные последующие числа
#  хранятся в кортеже как значения второго ключ

  
# def funcy(a, b, c, *args):
#     new_dict = {b:a, c: args}
#     return new_dict

# a = input("Iput numbers using / : ").split("/")

# print(funcy(*a))

# Самостоятельно сохраните в переменной строку текста.
# ✔ Создайте из строки словарь, где ключ — буква, а значение — код буквы.
# ✔ Напишите преобразование в одну строку. 

# a = "I love playing games"

# res = {i : ord(i) for i in a}
# print(res)

# iter_dict = iter(res.items())
# print(next(iter_dict, 6))


# Создайте генератор чётных чисел от нуля до 100.
# ✔ Из последовательности исключите
# числа, сумма цифр которых равна 8.
# ✔ Решение в одну строку

# a = (i for i in range(0, 101, 2) if sum(map(int, str(i)))!=8)
# b = (i for i in range(0, 101, 2) if (i//10 + i%10)!=8)
# print(*a)
# print(*b)

# ✔ Напишите программу, которая выводит
# на экран числа от 1 до 100.
# ✔ При этом вместо чисел, кратных трем,
# программа должна выводить слово «Fizz»
# ✔ Вместо чисел, кратных пяти — слово «Buzz».
# ✔ Если число кратно и 3, и 5, то программа
# должна выводить слово «FizzBuzz».
# ✔ *Превратите решение в генераторное выражение.

# a = ("FuzzBuzz" if i % 3 and i % 5 else "Fuzz" if i % 3 else "Buzz" if i % 5 else i \
#       for i in range (1, 101))
# for i in range(1,101):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FuzzBuzz")
#     if i % 3 == 0:
#        print("Fuzz")
#     if i % 5 == 0:
#         print("Buzz")
# print(i)
# print(*a)

#  Выведите в консоль таблицу умножения
# от 2х2 до 9х10 как на школьной тетрадке.
# ✔ Таблицу создайте в виде однострочного
# генератора, где каждый элемент генератора —
# отдельный пример таблицы умножения.
# ✔ Для вывода результата используйте «принт»
# без перехода на новую стро

# for i in range (2, 10, 4):
#     for j in range(2,10):
#         for k in range (i, i +4):

#         print(f'{i} * {j} = {i*j}', end = "\t") 
    
#         # print(f'{i} * {k} = {k*i}') 

# import random
# from random import randbytes, randint, sample, uniform
# import string
# ✔ Напишите функцию, которая заполняет файл
# (добавляет в конец) случайными парами чисел.
# ✔ Первое число int, второе - float разделены вертикальной чертой.
# ✔ Минимальное число - -1000, максимальное - +1000.
# ✔ Количество строк и имя файла передаются как аргументы функции. 


# def fill_file(num: int, name: str):
#     with open(name, "a", encoding = "utf-8") as file:
#         for _ in range(num):
#             file.write(f"{randint(-1000,1000)} | {uniform(-1000,1000)}\n")

# fill_file(5, "file_1")

# ✔ Напишите функцию, которая генерирует
# псевдоимена.
# ✔ Имя должно начинаться с заглавной буквы,
# состоять из 4-7 букв, среди которых
# обязательно должны быть гласные.
# ✔ Полученные имена сохраните в файл.


# def gen_names(name_file: str):
#     names = []
#     vowels = "aeiou"
#     while len(names) < randint(3,10):
#         res = "".join(sample(string.ascii_letters, randint(4,7))).capitalize()
#         if len(set(res) & set(vowels)) > 0: #если в результате есть хоть 1 главсная, то добадяем его 
#             names.append(res)
#     with open(name_file, "a", encoding = "utf-8") as file:
#         file.writelines('\n'.join(names))

# gen_names("file_2")


# ✔ Напишите функцию, которая открывает на чтение созданные
# в прошлых задачах файлы с числами и именами.
# ✔ Перемножьте пары чисел. 
# В новый файл сохраните
# имя и произведение:
# ✔ если результат умножения отрицательный, сохраните имя
# записанное строчными буквами и произведение по модулю
# ✔ если результат умножения положительный, сохраните имя
# прописными буквами и произведение округлённое до целого.
# ✔ В результирующем файле должно быть столько же строк,
# сколько в более длинном файле.
# ✔ При достижении конца более короткого файла,
# возвращайтесь в его начало.

# def  zip_func(file_1, file_2):

#     with (
#         open(file_1, "r", encoding = "utf-8" ) as f1,
#         open(file_2, "r", encoding = "utf-8" ) as f2        
#     ):
#         names = f1.readlines()
#         nums = f2.readlines()

#     nums = list(map(lambda x: (int(x.strip().split('|')[0]) * float(x.strip().split("|")[1])), nums))
#     names = list(map(lambda x: x.strip(), names))
    
#     res = list(zip(names, nums))

#     with open("result_file.txt", "a", encoding = "utf-8") as f_res:
#         for list_ in res:
#             if list_[1] < 0:
#                 f_res.write(f'{list_[0].lower()} - {abs(list_[1])}\n')
#             else:
#                 f_res.write(f"{list_[0].upper()} - {round(list_[1])}\n")

# zip_func("file_2", "file_1")


# ✔ Создайте функцию, которая создаёт файлы с указанным расширением.
# Функция принимает следующие параметры:
# ✔ расширение
# ✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
# ✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
# ✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
# ✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
# ✔ количество файлов, по умолчанию 42
# ✔ Имя файла и его размер должны быть в рамках переданного диапазона

# def create_file(extension: str, min_name = 6, max_name = 30, min_byte = 256, \
#                  max_byte = 4096, num_files = 42):
#     res_name = "".join(sample(string.ascii_letters, randint(min_name, max_name)))
#     with open(f'{res_name}.{extension}', "wb") as f:
#         for _ in range(num_files):
#             f.write(randbytes(randint(min_byte, max_byte)))
    
# create_file("txt", num_files = 3)


# Доработаем предыдущую задачу.
# ✔ Создайте новую функцию которая генерирует файлы с разными расширениями.
# ✔ Расширения и количество файлов функция принимает в качестве параметров.
# ✔ Количество переданных расширений может быть любым.
# ✔ Количество файлов для каждого расширения различно.
# ✔ Внутри используйте вызов функции из прошлой задачи.

# def extensions(ext: list, num: int):
#     for i in ext:
#         create_file(i, num_files = num )


# Дорабатываем функции из предыдущих задач.
# ✔ Генерируйте файлы в указанную директорию — отдельный параметр функции.
# ✔ Отсутствие/наличие директории не должно вызывать ошибок в работе функции
# (добавьте проверки).
# ✔ Существующие файлы не должны удаляться/изменяться в случае совпадения имён.

# СЕМИНАР 8
# Напишите функцию, которая в бесконечном цикле
# запрашивает имя, личный идентификатор и уровень
# доступа (от 1 до 7).
# После каждого ввода добавляйте новую информацию в
# JSON файл.
# Пользователи группируются по уровню доступа.
# Идентификатор пользователя выступает ключём для имени.
# Убедитесь, что все идентификаторы уникальны независимо
# от уровня доступа.
# При перезапуске функции уже записанные в файл данные
# должны сохраняться.

import json
import os
import csv
import pickle


PATH_DB = "user_db.json"
CSV_FILE = "file.csv"

def load_json():
    if os.path.exists(PATH_DB):
        with open(PATH_DB, 'r', encoding = "utf-8") as file:
            data = json.load(file)
    else:
        data = {}
    return data

def input_name():
    return input("Input name: ")

def input_id(dict_users: dict):
    list_id = set()
    for users in dict_users.values():
        for user in users:
            for u_id in user:
                list_id.add(u_id)
    while True:
        u_id = input("Input id: ")
        if u_id not in list_id and u_id.isdigit():
            return u_id
        print("Try again!")

def input_lvl():
    while True:
        lvl = input("Input level access: ")
        if lvl.isdigit():
            if 0 < int(lvl) < 8:
                return lvl
        
def create_users():
    while True:
        user_db = load_json()
        name = input_name()
        if not name:
            break
        u_id = input_id(user_db)
        lvl = input_lvl()
        if lvl in user_db:
            user_db[lvl].append({u_id:name})
        else:
            user_db[lvl] = [{u_id:name}]
            with (
                open(PATH_DB, "w", encoding = "utf-8") as file_json, \
                open(CSV_FILE, "w", encoding = "utf-8") as file_csv):   
                json.dump(user_db, file_json, indent=4, ensure_ascii=False)
                result = []
                for lvl, users in user_db.items():
                    for user in users:
                        for u_id, name in user.items():
                            result.append([name, u_id, lvl])
                csv_writer = csv.writer(file_csv, dialect = "excel", delimiter='|', lineterminator="\n")
                csv_writer.writerows(result)
        
# create_users()

# Напишите функцию, которая сохраняет созданный в
# прошлом задании файл в формате CSV.

# Прочитайте созданный в прошлом задании csv файл без
# использования csv.DictReader.
# Дополните id до 10 цифр незначащими нулями.
# В именах первую букву сделайте прописной.
# Добавьте поле хеш на основе имени и идентификатора.
# Получившиеся записи сохраните в json файл, где каждая строка
# csv файла представлена как отдельный json словарь.
# Имя исходного и конечного файлов передавайте как аргументы
# функции.

def export_csv_to_json(csv_file: str, json_file: str):
    final_dict = {}
    with open(csv_file, "r", encoding = "utf-8") as file:
        data = file.readlines()
    for i, items in enumerate(data):
        data[i] = data[i].strip().split("|")
        data[i][1] = data[i][1].zfill(10)
        final_dict[hash(data[i][0] + data[i][1])] = data[i]
    with open(json_file, "w", encoding = "utf-8") as file:
        json.dump(final_dict, file, indent=4, ensure_ascii = False)
# export_csv_to_json("file.csv", "new_user_db.json")


# Напишите функцию, которая ищет json файлы в указанной
# директории и сохраняет их содержимое в виде
# одноимённых pickle файлов.

def json_to_pickle(path: str = os.getcwd()):
    file_list = []
    for files in os.walk(path):
        for file in files[2]:
            if file.endswith(".json"):
                file_list.append ((os.path.join(files[0], file),\
                os.path.join(files[0], file.rsplit(".")[0] + ".pickle")))
                
    for file in file_list:
        with open(file[0], "r", encoding = "utf-8") as json_in:
            data = json.load(json_in)
        with open(file[1], "wb") as f_out:
            pickle.dump(data, f_out)
            
# print(json_to_pickle())

# 