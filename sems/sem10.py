# Создайте класс окружность.
# Класс должен принимать радиус окружности при создании
# экземпляра.
# У класса должно быть два метода, возвращающие длину
# окружности и её площадь.


from math import pi


class Circle:

    def __init__(self, radius: float) -> None:
        self.radius = radius

    def circumference(self):
        return round(2**pi*self.radius, 2)
    
    def area(self):
        return round(pi*(self.radius**2), 2)
    
# circle = Circle(4)
# print(circle.area())
# print(circle.circumference())

# Создайте класс прямоугольник.
# Класс должен принимать длину и ширину при создании
# экземпляра.
# У класса должно быть два метода, возвращающие периметр
# и площадь.
# Если при создании экземпляра передаётся только одна
# сторона, считаем что у нас квадрат.

class Rectangle:

    def __init__(self, side_a, side_b = None) -> None:
        if side_b is None:
            self.side_a = self.side_b = side_a
        else:
            self.side_a = side_a
            self.side_b = side_b
    
    def perimetr(self):
        return 2*(self.side_a + self.side_b)

    def area(self):
        return self.side_a * self.side_b

# rect = Rectangle(5)
# rect_2 = Rectangle(2, 5)
# print(rect.area(), rect.perimetr())
# print(rect_2.area(), rect_2.perimetr())

# Напишите класс для хранения информации о человеке:
# ФИО, возраст и т.п. на ваш выбор.
# У класса должны быть методы birthday для увеличения
# возраста на год, full_name для вывода полного ФИО и т.п. на
# ваш выбор.
# Убедитесь, что свойство возраст недоступно для прямого
# изменения, но есть возможность получить текущий возраст

class Person:
    def __init__(self, name: str, surname: str, patronymic: str, age: int):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self._age = age

    def show_age(self):
        return self._age
    
    def birthday(self):
        self._age += 1
    
    def full_name(self):
        return f'ФИО: {self.surname} {self.name} {self.patronymic}'
    
# person = Person("Stas", "Efimov", "Mikhailovich", 23)
# print(person.full_name())
# print(person.show_age())
# person.birthday()
# print(person.show_age())

# Создайте класс Сотрудник.
# Воспользуйтесь классом человека из прошлого задания.
# У сотрудника должен быть:
# ○ шестизначный идентификационный номер
# ○ уровень доступа вычисляемый как остаток от деления
# суммы цифр id на семь

class Employee(Person):
    def __init__(self, id: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.id = id
        self.access = sum(list(map(int, id))) % 7

# emp = Employee("000012", "Egor", "Efimov", "Andreevich", 34)
# print(emp.full_name())
# print(emp.access)

# Создайте три (или более) отдельных классов животных.
# Например рыбы, птицы и т.п.
# У каждого класса должны быть как общие свойства,
# например имя, так и специфичные для класса.
# Для каждого класса создайте метод, выводящий
# информацию специфичную для данного класса

class Animal:
     def __init__(self, name: str, age: int, weigth: float) -> None:
        self.name = name
        self.age = age
        self. weigth = weigth

class Fish(Animal):

    type = "Fish"

    def __init__(self, name: str, age: int, weigth: float, ocean: str) -> None:
        super().__init__(name, age, weigth)
        self.ocean = ocean 

    def get_ocean(self):
        return self.ocean
    
    def get_type(cls):
        return cls.type
    
class Horse(Animal):

    type = "Horse"

    def __init__(self, name: str, age: int, weigth: float, tricks: list) -> None:
        super().__init__(name, age, weigth)
        self.tricks = tricks

    def get_tricks(self):
        return self.tricks
            
    def get_type(cls):
        return cls.type
    
class Bird(Animal):

    type = "Bird"

    def __init__(self, name: str, age: int, weigth: float, flies: bool) -> None:
        super().__init__(name, age, weigth)
        self.flies = flies

    def flies(self):
        return self.flies
    
    def get_type(cls):
        return cls.type
# horse = Horse("Roxy", 10, 400, ["runs", "jumps"])
# fish = Fish("Nemo", 4, 0.3, "Pacific ocean")
# bird = Bird("Chick", 13, 0.5, True)
# print(horse.get_tricks(), fish.get_ocean(), bird.flies, sep ="\n")