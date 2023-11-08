# Создайте функцию, которая запрашивает числовые данные от
# пользователя до тех пор, пока он не введёт целое или
# вещественное число.
# Обрабатывайте не числовые данные как исключения.






# Создайте функцию аналог get для словаря.
# Помимо самого словаря функция принимает ключ и
# значение по умолчанию.
# При обращении к несуществующему ключу функция должна
# возвращать дефолтное значение.
# Реализуйте работу через обработку исключений.

def func(some_dict: dict, key, default = "Nothing's found"):

    try:
        return some_dict[key]
    except KeyError:
        return default
    
# if __name__ == "__main__":
#     my_dict = {1:"text"}
#     print(func(my_dict, 2, "None"))

# Создайте класс с базовым исключением и дочерние классы исключения:
# ○ ошибка уровня,
# ○ ошибка доступа.

class MyException(Exception):

    def __init__(self, msg: str):
        self.msg = msg

    def __str__(self):
        return f"My exception: {self.msg}"
    
class LevelError(MyException):
    def __init__(self, msg: str):
        super(LevelError, self).__init__(msg)

class AccessError(MyException):
    def __init__(self, msg: str):
        super(AccessError, self).__init__(msg)

# raise AccessError("STOP")

# Вспоминаем задачу из семинара 8 про сериализацию данных,
# где в бесконечном цикле запрашивали имя, личный
# идентификатор и уровень доступа (от 1 до 7) сохраняя
# информацию в JSON файл.
# Напишите класс пользователя, который хранит эти данные в
# свойствах экземпляра.
# Отдельно напишите функцию, которая считывает информацию
# из JSON файла и формирует множество пользователей


import json
import os


class User:

    def __init__(self, name: str, the_id: int, level: int):
        if not isinstance(name, str) or not name.isalpha():
            raise ValueError('Имя должно быть текстового вида')
        self.name = name
        if not isinstance(the_id, int) or the_id <= 0:
            raise ValueError('Личный идентификатор должен быть целым числом')
        self.the_id = the_id
        if not isinstance(level, int) or level not in range(1, 8):
            raise ValueError('Уровень доступа должен быть целым числом от 1 до 7')
        self.level = level

    def __str__(self):
        return f'{self.name = }, {self.the_id = }, {self.level = }'

    def load_json(path):
        if os.path.exists(path):
            with open(path, 'r', encoding='UTF-8') as file:
                data = json.load(file)
        else:
            data = {}
        return data


    def worker():
        while True:
            try:
                name = input('Введите имя: ')
                the_id = int(input('Введите личный идентификатор: '))
                level = int(input('Введите уровень доступа: '))
                return User(name, the_id, level)
            except ValueError as e:
                print(e)


    def save_json(path, user_db):
        with open(path, 'w', encoding='UTF-8') as file:
            json.dump(user_db, file, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    path = 'my_json.json'
    user_db = User.load_json(path)
    new_user = User.worker()
    if str(new_user.the_id) in user_db:
        raise Exception('Пользователь с этим ID уже записан в базу')
    else:
        user_db[new_user.the_id] = (new_user.name, new_user.level)
    User.save_json(path, user_db)

# Доработаем задачи 3 и 4. Создайте класс проекта, который
# имеет следующие методы:
# загрузка данных (функция из задания 4)
# вход в систему - требует указать имя и id пользователя. Для
# проверки наличия пользователя в множестве используйте
# магический метод проверки на равенство пользователей.
# Если такого пользователя нет, вызывайте исключение
# доступа. А если пользователь есть, получите его уровень из
# множества пользователей.
# добавление пользователя. Если уровень пользователя
# меньше, чем ваш уровень, вызывайте исключение уровня
# доступа.

class Loger:
    db = {}

    def __init__(self, path):
        self.__class__.db = load_json(path)
        self.level = None

    def authorize(self, the_id, name):
        user = User(name, the_id)
        print(user)
        print(self.__class__.db)
        for obj in self.__class__.db.values():
            if user == obj:
                self.__class__.db[str(the_id)]['level']
                return self.level
            else:
                raise Exception('Пользователь с такими данными не найден')


if __name__ == '__main__':
    PATH = 'my_json.json'
    loger = Loger(PATH)
    print(f"Уровень доступа: {loger.authorize(1, 'Алекс')}")

