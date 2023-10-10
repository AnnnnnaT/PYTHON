# Создайте класс Моя Строка, где:
# будут доступны все возможности str
# дополнительно хранятся имя автора строки и время создания
# (time.time)
from time import time

class MyStr(str):
    def __new__(self, author, value):
        super().__new__()
        self.author = author
        self.create_time = time()
        self.value = value
        
# Создайте класс Архив, который хранит пару свойств.
# Например, число и строку.
# При нового экземпляра класса, старые данные из ранее
# созданных экземпляров сохраняются в пару списковархивов
# list-архивы также являются свойствами экземпляра

class MyZip:
    
    zip_lst = []
    def __new__(cls, *args, **kwargs):
        instance = MyZip(*args, **kwargs)
        self.list = list(num, string_)

    def __init__(self, text:str, num: int):
        self.text = text
        self.num = num
        

from copy import deepcopy


# class MyZip:
# zip_lst = []

# def __new__(cls, value: int, text: str):
# instance = super().__new__(cls)
# cls.zip_lst.append((value, text))
# return instance

# def __init__(self, value: int, text: str):
# self.value = value
# self.text = text
# self.zip_lst = deepcopy(self.zip_lst)


# a = MyZip(5, 'слово')
# b = MyZip(4, 'слово слово')
# c = MyZip(3, 'слово!!!')
# print(c.zip_lst)
# print(a.zip_lst)
# print(b.zip_lst)

# Дорабатываем класс прямоугольник из прошлого семинара.
# Добавьте возможность сложения и вычитания.
# При этом должен создаваться новый экземпляр
# прямоугольника.
# Складываем и вычитаем периметры, а не длинну и ширину.
# При вычитании не допускайте отрицательных значений.

