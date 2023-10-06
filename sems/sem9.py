import json
import os
from random import randint
from typing import Callable

# Создайте функцию-замыкание, которая запрашивает два целых
# числа:
# ○ от 1 до 100 для загадывания,
# ○ от 1 до 10 для количества попыток
# Функция возвращает функцию, которая через консоль просит
# угадать загаданное число за указанное число попыток. 

# def guess(): 
#     attempt = int(input("Input number of attempts from 1 to 10: "))
#     num = int(input("Input num from 1 to 100: "))
#     def wrap():
#         nonlocal  attempt, num
#         while attempt:
#             a = int(input("Hidden number: "))
#             attempt-=1              
#             if a == num:
#                 return f"You right. Hidden number is {num}"
#             else:
#                 continue 
#             return "There is no more attempts"
#     return wrap

# # a = guess()
# # a()

# Дорабатываем задачу 1.
# Превратите внешнюю функцию в декоратор.
# Он должен проверять входят ли переданные в функциюугадайку числа в диапазоны [1, 100] и [1, 10].
# Если не входят, вызывать функцию со случайными числами
# из диапазонов

def guess_(func: Callable): 
    
    def wrap(*args):

        num, attempt = args

        if attempt not in range(1,11):
            print("Not that number")
            attempt = randint(1,10)
        if num not in range(1,101):
            num = randint(1,101)

        return func(*args)
    
    return wrap

@guess_
def inner():
    num = int(input("Input num from 1 to 100: "))
    attempt = int(input("Input number of attempts from 1 to 10: "))
    while attempt:
        a = int(input("Hidden number: "))
        attempt-=1              
        if a == num:
            print(f"You right. Hidden number is {num}")
            break
        elif a != num: 
            continue
        else:
            return "There is no more attempts"
    # return "There is no more attempts"
    
a = inner(3, 5)
print(a)

# Напишите декоратор, который сохраняет в json файл
# параметры декорируемой функции и результат, который она
# возвращает. При повторном вызове файл должен
# расширяться, а не перезаписываться.
# Каждый ключевой параметр сохраните как отдельный ключ
# json словаря.
# Для декорирования напишите функцию, которая может
# принимать как позиционные, так и ключевые аргументы.
# Имя файла должно совпадать с именем декорируемой
# функции.


def decor(func: Callable):

    def wrapper(*args, **kwargs):
        file_name = func.__name__ + ".json"

        if os.path.isfile(file_name):
            with open(file_name, "r", encoding = "utf-8") as file:
                data = json.load(file)
        else:
            data = {}

        result = func(*args, **kwargs)
        data[result] = list(args + tuple(kwargs.items()))

        with open(file_name, "w", encoding = "utf-8") as file:
            json.dump(data, file, indent = 4, ensure_ascii = False)

        return result
    
    return wrapper


# @decor
# def some_func(a:str, b: str):
#     return a + "_" + b

# print(some_func("Привет", "мир"))

# Создайте декоратор с параметром.
# Параметр - целое число, количество запусков декорируемой
# функции.

def outer(count: int):

    def decor(func: Callable):

        def wrapper(*args, **kwargs):
            res = []
            for _ in range(count):
                res.append(func(*args, **kwargs))
            return res
        
        return wrapper

    return decor      

@outer(5)
def some_func(a:str, b: str):
    return a + "_" + b

# print(some_func("Привет", "мир"))

# Объедините функции из прошлых задач.
# Функцию угадайку задекорируйте:
# ○ декораторами для сохранения параметров,
# ○ декоратором контроля значений и
# ○ декоратором для многократного запуска.
# Выберите верный порядок декораторов.
