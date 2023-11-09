from typing import TypeAlias
import json

from student import Student

STUDENT_FILE = "hws\hw12\students.json"
STUDENT_TYPE: TypeAlias = dict[str, dict[str, dict[str, list[int]]]]  #задаем определенному типу данных альяс и используем его дальше 

# загружаем студентов из json
def load_students(path: str) -> STUDENT_TYPE:
    with open(path, "r", encoding = "UTF-8") as file:
        result = json.load(file, parse_int=int)
    return result

if __name__ == '__main__':
    students_base = [] #список для объектов Студентов
    students = load_students(STUDENT_FILE) #загружаем студентов из json
    for student, marks  in students.items():
        students_base.append(Student(*student.split())) #разбиваем ФИО студентов на элементы (* чтобы распаковать список 
        students_base[-1].marks = marks["marks"]        # полученный после сплита) для создания объекта и добавляем в список 
        students_base[-1].tests = marks["tests"]        #для каждого последнего добавленного студента[-1] под ключами 
                                                            #     tests/marks добавляем бал в оценки либо в тесты
    for student in students_base:                        
        print(student)
