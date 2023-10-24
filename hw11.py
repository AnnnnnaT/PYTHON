#1
from datetime import datetime
import random

# class MyStr(str):
    
#     def __new__(cls, value: str, author: str):
#         instance = super().__new__(cls, value)
#         instance.author = author
#         instance.time = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M')
#         return instance
    
#     def __init__(self, value: str, author: str):
#         self.value = value
#         self.author = author
#         self.time = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M')
        
    
#     def __str__(self):
#         return f"{self.value} (Автор: {self.author}, Время создания: {self.time})"
        
#     def __repr__(self):
#         return f"MyStr('{self.value}', '{self.author}')"
    
#2
# Введите ваше решение ниже

from typing import Union
class Archive:
    """
    Класс, представляющий архив текстовых и числовых записей.

    Атрибуты:
    - archive_text (list): список архивированных текстовых записей.
    - archive_number (list): список архивированных числовых записей.
    - text (str): текущая текстовая запись для добавления в архив.
    - number (int или float): текущая числовая запись для добавления в архив.
    """

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.archive_text = []
            cls._instance.archive_number = []
        else:
            cls._instance.archive_text.append(cls._instance.text)
            cls._instance.archive_number.append(cls._instance.number)
        return cls._instance

    def __init__(self, text: str, number: Union[int, float]):
        self.text = text
        self.number = number

    def __str__(self):
        return f'Text is {self.text} and number is {self.number}. Also {self.archive_text} and {self.archive_number}'

    def __repr__(self):
        return f'Archive("{self.text}", {self.number})'
    

#3
class Rectangle:
    
    width: int = None
    height: int = None    
        
    def __init__(self, width: int, height: int = None):
        if height is None:
            self.width = self.height = width
        else:
            self.width = width
            self.height = height
            
    def perimeter(self):
        return 2*(self.width + self.height)
    
    def area(self):
        return self.width * self.height
    
    def __add__(self, other):
        if isinstance(other, Rectangle):
            width = self.width + other.width
            height = self.height + other.heigth
        return Rectangle(width, height)
    
    def __sub__(self, other):
        if isinstance(other, Rectangle):
            if self.width > other.width and self.height > other.height:
                width = self.width - other.width
                height = self.height - other.height       
            else:
                width = other.width - self.width
                height = other.height - self.height
        return Rectangle(width, height)
    
    def __lt__(self, other): 
        if isinstance(other, Rectangle):
            if self.area() < other.area():
                return True

    def __eq__(self, other): 
        if isinstance(other, Rectangle):
            if self.area() == other.area():
                return True

    def __le__(self, other): 
        if isinstance(other, Rectangle):
            if self.area() <= other.area():
                return True
            
    def __str__(self):
        return f"Прямоугольник со сторонами {self.width} и {self.height}"
    
    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"
        

#4
class Matrix:
    
    def __init__(self, rows: int = 2, cols: int = 2, matrix: list[list[int]] = None):
        if matrix is None:
            if rows > 1 and cols > 1:
                self.rows = rows
                self.cols = cols
                self.matrix = [[random.randint(0,100) for _ in range (cols)] for _ in range (rows)]
            else:
                raise ValueError
        else:
            if Matrix._check_matrix(matrix):
                self.rows = len(matrix)
                self.cols = len(matrix[0]) #кол-во столбцов равно кол-ву элем в каждом списке
                self.matrix = matrix
            else:
                raise ValueError
                
    def __str__(self):
        return "\n".join("".join([f'{x:^5}' for x in row]) for row in self.matrix) + "\n"
        
        
    @staticmethod
    def _check_matrix(matrix: list[list[int]]):
        return len(set(map(len, matrix))) == 1 
    #т.е. для каждой строки матрицы находим длину, в сете остается одно
    # уникальное значение (если все равны) и длина сета дожна быть равна 1
    
    def __eq__(self, other):
        if Matrix._same(self, other):
#             return all([all([self.matrix[r][c] == other.matrix[r][c]]
#                            for c in range(self.cols)) for r in range (self.rows)])
            return all(map(lambda x: x[0] == x[1], zip([y for x in self.matrix for y in x],
                                                         [y for x in other.matrix for y in x])))
        else:
            raise ValueError
        
    @staticmethod 
    def _same(matrix1, matrix2):
        return isinstance(matrix2, Matrix) and matrix1.rows == matrix2.rows \
                                and matrix1.cols == matrix2.cols
            
    
    def __add__(self, other):
        if Matrix._same(self, other):
            return Matrix(matrix = [[self.matrix[i][j] + other.matrix[i][j] for j in range(self.cols)]                         for i in range(self.rows)])
        
    def __mul__(self, other):
        if isinstance(other, Matrix):
            new_matrix = [[0] * other.cols for _ in range(self.rows)]
            for i in range(self.rows):
                for j in range(other.cols):
                    for k in range(other.rows):
                        new_matrix[i][j] += self.matrix[i][j] * other.matrix[k][j]
            return Matrix(matrix = new_matrix)
        
        elif isinstance(other, int | float):
            return Matrix(matrix = [[self.matrix[r][c] * other
                                for c in range(self.cols)] for r in range(self.rows)])
        else:
            raise ValueError       
            
    def __repr__(self):
        return f"Matrix({self.rows}, {self.cols})"
        
a = Matrix()
b = Matrix(4,5)
c = Matrix(matrix = [[1,2,3], [4,5,6]])


class Matrix:
    """
    Класс, представляющий матрицу.

    Атрибуты:
    - rows (int): количество строк в матрице
    - cols (int): количество столбцов в матрице
    - data (list): двумерный список, содержащий элементы матрицы

    Методы:
    - __str__(): возвращает строковое представление матрицы
    - __repr__(): возвращает строковое представление матрицы, которое может быть использовано для создания нового объекта
    - __eq__(other): определяет операцию "равно" для двух матриц
    - __add__(other): определяет операцию сложения двух матриц
    - __mul__(other): определяет операцию умножения двух матриц
    """

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[0 for j in range(cols)] for i in range(rows)]

    def __str__(self):
        """
        Возвращает строковое представление матрицы.

        Возвращает:
        - str: строковое представление матрицы
        """
        return '\n'.join([' '.join([str(self.data[i][j]) for j in range(self.cols)]) for i in range(self.rows)])

    def __repr__(self):
        """
        Возвращает строковое представление матрицы, которое может быть использовано для создания нового объекта.

        Возвращает:
        - str: строковое представление матрицы
        """
        return f"Matrix({self.rows}, {self.cols})"

    def __eq__(self, other):
        """
        Определяет операцию "равно" для двух матриц.

        Аргументы:
        - other (Matrix): вторая матрица

        Возвращает:
        - bool: True, если матрицы равны, иначе False
        """
        if self.rows != other.rows or self.cols != other.cols:
            return False
        for i in range(self.rows):
            for j in range(self.cols):
                if self.data[i][j] != other.data[i][j]:
                    return False
        return True

    def __add__(self, other):
        """
        Определяет операцию сложения двух матриц.

        Аргументы:
        - other (Matrix): вторая матрица

        Возвращает:
        - Matrix: новая матрица, полученная путем сложения двух исходных матриц
        """
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Матрицы должны иметь одинаковые размеры")
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[i][j] = self.data[i][j] + other.data[i][j]
        return result

    def __mul__(self, other):
        """
        Определяет операцию умножения двух матриц.

        Аргументы:
        - other (Matrix): вторая матрица

        Возвращает:
        - Matrix: новая матрица, полученная путем умножения двух исходных матриц
        """
        if self.cols != other.rows:
            raise ValueError("Количество столбцов первой матрицы должно быть равно количеству строк второй матрицы")
        result = Matrix(self.rows, other.cols)
        for i in range(self.rows):
            for j in range(other.cols):
                for k in range(self.cols):
                    result.data[i][j] += self.data[i][k] * other.data[k][j]
        return result
