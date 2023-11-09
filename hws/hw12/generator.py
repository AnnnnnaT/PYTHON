# МОДУЛЬ КОТОРЫЙ ГЕНЕРИРУЕТ СПИСОК СТУДЕНТОВ И ИХ ОЦЕНКИ И ТЕСТЫ ПО ПРЕДМЕТАМ и записывает их в json

from faker import Faker
from random import randint as RI
import json
import csv
import pprint 


# задаем константы для использования в  коде

MIN_MARK = 2
MAX_MARK = 5
MIN_TEST = 0
MAX_TEST = 100
MIN_MARK_COUNT =  5
MAX_MARK_COUNT = 10
MIN_TEST_COUNT = 1
MAX_TEST_COUNT = 5


STUDENT_COUNT = 20
SUBJECT_FILE = 'hws\hw12\subjects.csv'   #здесь написаны предметы
STUDENT_FILE = "students.json"  #здесь будет бз студентов и их предметов с оценками

# фнкция для выгрузки данных из csv файла в виде кортежа предметов

def load_subjects(file_name: str) -> tuple[str]:
    with open(file_name, "r", encoding = "UTF-8") as file:
        csv_reader = csv.reader(file, dialect='excel')
        result = tuple((next(csv_reader)))
    return result

# ФУНКЦИЯ-ДЕКОРАТОР
# снаружи формируется словарь, 
# где ключ - название предмета из входящего кортежа предметов
# значение - кортеж из рандомных оценок, который получаем
# внутренней функцией (генератор чисел, возвращающий кортеж 
# рандомного количества рандомных оценок)

def mark_generator(subjects: tuple[str],
                    min_mark: int,
                    max_mark: int,
                    min_mark_count: int,
                    max_mark_count: int ) :  
                                                     
    def generator_numbers() -> tuple[int]:
        return tuple([RI(min_mark, max_mark)
                        for _ in range(RI(min_mark_count, max_mark_count))])

    return {sub: generator_numbers() for sub in subjects}   

# генератор студентов который принимает пустой словарь base_students
# и заполняет его ключами - именами студентов
# значениями - словарями с ключами marks и tests, 
# где значения - сгенерированные кортежи оценок и тестов

def generator_students(base_students: dict,
                        subjects: tuple,
                        students_count: int = STUDENT_COUNT):
    fake = Faker("ru-RU")
    for _ in range(students_count):
        if RI(0,1):
            first_name = fake.first_name_male()
            last_name = fake.last_name_male()
            patronynic = fake.middle_name_male()
        else:
            first_name = fake.first_name_female()
            last_name = fake.last_name_female()
            patronynic = fake.middle_name_female()
        base_students[" ".join((first_name, patronynic, last_name))] = {
            "marks": mark_generator(subjects, MIN_MARK, MAX_MARK, 
                                    MIN_MARK_COUNT, MAX_MARK_COUNT),
            "tests": mark_generator(subjects, MIN_TEST, MAX_TEST,
                                    MIN_TEST_COUNT, MAX_TEST_COUNT)
        }

# записывает созданный словарь студентов в JSON, создаем БД студентов    
def create_students_base(dict_to_dump: dict, path: str = STUDENT_FILE):
    with open(path, "w", encoding="UTF-8") as file:
        json.dump(dict_to_dump, file, indent=4, ensure_ascii=False)

if __name__=="__main__":
    base_student = {}
    generator_students(base_student, load_subjects(SUBJECT_FILE))
    create_students_base(base_student)