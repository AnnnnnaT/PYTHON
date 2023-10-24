from random import randint
import random

# Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для случайной
# расстановки ферзей в задаче выше. Проверяйте различный случайные варианты и выведите 4 успешных расстановки.
a = [[1,2],[2,4],[2,4],[3,6],[7,8],[3,6],[2,3],[3,3]]

def check_queens(positions: list[list]):
    for i in range(len(positions)):
        for j in range(1, len(positions)):      
            if (positions[i][0] == positions[j][0] or \
            positions[i][1] == positions[j][1] or \
            abs(positions[i][0] - positions[j][0]) == abs(positions[i][1] - positions[j][1])):
                return False      
    return True

print(check_queens(a))

def gen_pos():
    positions = [[random.randint(1,8), random.randint(1,8)] for i in range(8)]
    return positions
print(gen_pos())