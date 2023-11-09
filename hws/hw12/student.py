MIN_MARK = 2
MAX_MARK = 5
MIN_TEST = 0
MAX_TEST = 100

# ДЕСКРИПТОРЫ, КОТОРЫЕ ОБЕСПЕЧИВАЮТ УНИВЕРСАЛЬНЫЙ ИНТЕРФЕЙС ДЛЯ ВСЕХ ЭКЗЕМПЛЯРОВ КЛАССА

class Naming:
    def __set_name__(self, owner, name):
        self.parameter_name = "_" + name
    
    def __get__(self, instance, owner):
        return getattr(instance, self.parameter_name)

    def __set__(self, instance, value: str):
        if not value.isalpha():
            raise ValueError(f"{value} - имя должно состоять только из букв")
        if not value.istitle():
            raise ValueError(f'{value} - имя должно начинаться с большой буквы')
        setattr(instance, self.parameter_name, value)

class Marks:
    def __init__(self, name: str, min_limit: int, max_limit: int):
        self.name = name
        self.min_limit = min_limit
        self.max_limit = max_limit

    def __set_name__(self, owner, name):
        self.parameter_name = "_" + name
    
    def __get__(self, instance, owner):
        return getattr(instance, self.parameter_name)

    def __set__(self, instance, value: str):
        self.mark_validator(value)
        setattr(instance, self.parameter_name, value)
    
    def mark_validator(self, marks_dict: dict):
        for subjects, marks in marks_dict.items():
            for mark in set(marks):
                if not (self.min_limit <= mark <= self.max_limit):
                    raise ValueError(f'{self.name} имеет значение {mark}'
                                        f'при допустимых от {self.min_limit} до {self.max_limit}')

# с помощью дескрипторов Naming(для имени студента) и Marks (для его оценок)
# написан класс Студента, экземпляры которого проходят
# по всем критериям задания, благодаря валидации в дескрипторах


class Student:
    first_name = Naming()           #переданные имена в случае успешной валидации присваиваются переменным
    last_name = Naming()
    patronymic = Naming()
    marks = Marks("Оценки", MIN_MARK, MAX_MARK)
    tests = Marks("Тесты", MIN_TEST, MAX_TEST)

    def __init__(self, first_name: str, last_name: str, patronymic: str):
        self.first_name = first_name
        self.last_name = last_name
        self.patronymic = patronymic

    def __str__(self):
        tests_result = "\n".join([f"\t{subj:.<15}: {test}" for subj, test in self.test_average()])
        return (f'{self.first_name} {self.last_name} {self.patronymic}\nСредняя оценка: {self.mark_average()}\n'
                    f'Результаты тестов:\n{tests_result}\n\n')

    def mark_average(self):
        all_marks = []
        for marks in self.marks.values():
            all_marks.append(sum(marks)/len(marks))           #средние оценки по КАЖДОМУ предмету добавляются в список
        return round(sum(all_marks)/len(all_marks), 2)        #средняя оценка по ВСЕМ предметам

    def test_average(self):
        all_tests = []
        for subject, test in self.tests.items():
            all_tests.append((subject, round(sum(test)/len(test), 2)))  #в список добавляется кортеж из названия и среднего теста по предмету
        return all_tests                                            