from random import randint
import csv
from typing import Callable
import json
import os

# Напишите следующие функции:
# Нахождение корней квадратного уравнения
# Генерация csv файла с тремя случайными числами в
# каждой строке. 100-1000 строк.
# Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
# Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.


def save_to_json(func: Callable):
    def wrapper(*args):
        res = {}
        with open("res.json", "w", encoding = "utf-8") as f:
            res[func(*args)] = args
            json.dump(res, f , indent = 4, ensure_ascii = False)
        return res    
    return wrapper



def args_from_csv(func: Callable):    
    def wrapper(name: str):
        with open(name, "r") as f:                
            csv_file = csv.reader(f)
            for line in csv_file:
                return func(*line)
    return wrapper



@save_to_json
@args_from_csv("file.csv")
def find_root(a: int, b: int, c: int):
    d = b**2 - 4*a*c
    if d > 0:
        x1 = (-b + d**(0.5)) / 2*a 
        x2 = (-b - d**(0.5)) / 2*a 
        return round(x1,2), round(x2,2)
    elif d == 0:
        x = -b / 2*a
        return round(x,2)
    else:
        return "No roots"

def gen_csv(name: str):
    with open(name, "w", newline='') as f:
        csv_write = csv.writer(f)
        lines = randint(100, 1000)
        for _ in range(lines):
            line = [randint(1, 1000) for _ in range(3)]
            csv_write.writerow(line)



# gen_csv("file.csv")

print(find_root(10,21,23))


