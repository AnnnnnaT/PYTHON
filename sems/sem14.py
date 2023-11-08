# Напишите для задачи 1 тесты doctest. Проверьте
# следующие варианты:
# возврат строки без изменений
# возврат строки с преобразованием регистра без потери
# символов
# возврат строки с удалением знаков пунктуации
# возврат строки с удалением букв других алфавитов
# возврат строки с учётом всех вышеперечисленных пунктов
# (кроме п. 1)


from string import ascii_lowercase
import doctest

def clear_text(text:str):
    """
    Clear text
    >>> clear_text('text') == 'text'
    True
    >>> clear_text('TexT') == 'text'
    True
    >>> clear_text('te.xT') == 'text'
    True
    >>> clear_text('TФФффext') == 'text'
    True
    >>> clear_text('TeЯ..xT') == 'text'
    True
    """
    result = ''
    for i in text:
        if i.lower() in ascii_lowercase + ' ':
            result += i
    return result.lower()

if __name__ == '__main__':
    doctest.testmod(verbose=True)


import unittest

class TestUnitCheck(unittest.TestCase):

    def setUp(self):
        self.first = Rectangle(2, 3)
        self.second = Rectangle(4, 5)

    def test_eq(self):
        self.assertTrue(self.first == self.second)

    def test_not_eq(self):
        self.assertFalse(self.first == self.second)

    def test_sum(self):
        self.assertEqual(self.first + self.second, Rectangle(6, 8))

    def test_exist(self):
        self.assertRaises(ValueError, Rectangle, (0, 3))

if __name__ == '__main__':
    unittest.main(verbosity=2)
  
# 📌Изменяем класс прямоугольника.
# 📌Заменяем пару декораторов проверяющих длину и ширину на дескриптор с валидацией размера.

class ValidateRectangle:
    def __init__(self, min_value: int = 1):
        self.min_value = min_value

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def validate(self, value):
        if not isinstance(value, int):
            raise TypeError('Invalid type of input')
        if value < self.min_value:
            raise ValueError('Invalid value of input')


class Rectangle:
    width = ValidateRectangle()
    height = ValidateRectangle()

    def __init__(self, width, height):
        self._width = width
        self._height = height

    def perimeter(self):
        return 2 * (self._width + self._height)

    def area(self):
        return self._width * self._height

    def __add__(self, other):
        return Rectangle(self.width + other.width, self.height + other.height)

    def __eq__(self, other):
        return self.width == other.width and self.height == other.height

    def __str__(self):
        return f"Прямоугольник со сторонами {self._width} и {self._height}"

    def __repr__(self):
        return f"{self.__class__.__name__}({self._width}, {self._height})"

r1 = Rectangle(1, 2)
print(r1)
r1.width = 5
print(r1)
r1.width = -1