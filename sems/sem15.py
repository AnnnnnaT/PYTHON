import logging 

# Напишите программу, которая использует модуль logging для
# вывода сообщения об ошибке в файл.
# Например отлавливаем ошибку деления на ноль.

logger = logging.getLogger(__name__) #обычно передаем имя текущего файла

format = "{asctime:<20} - {levelname:<10} - {msg}"

logging.basicConfig(filename="sems\mylog.log", filemode="w", encoding="utf-8", level=logging.ERROR,
                    style="{", format=format)

def func(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        logger.error(msg=e)

func(100,0)

# На семинаре про декораторы был создан логирующий
# декоратор. Он сохранял аргументы функции и результат её
# работы в файл.
# Напишите аналогичный декоратор, но внутри используйте
# модуль logging

from functools import wraps
from typing import Callable


def decor(func: Callable) -> Callable:
    logger = logging.getLogger(__name__)
    my_format = '{msg}'
    logging.basicConfig(filename='mylog.log', filemode='a', encoding='UTF-8',
    level=logging.INFO, style='{', format=my_format)

    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        str_args, str_kwargs = '', ''
        if args:
            str_args = 'args: ' + ', '.join(args)
        if kwargs:
            str_kwargs = 'kwargs: ' + ', '.join([f"{key}={value}" for key, value in kwargs.items()])
        logger.info(msg=f'result: {result}, {str_args}' + (', ' if str_args and str_kwargs else '') + f'{str_kwargs}')
        return result

    return wrapper

@decor
def some_func(a: str, b: str):
    return a + '_' + b


some_func('первая', 'вторая')
some_func('первая', b='вторая')
some_func(a='первая', b='вторая')

# Доработаем задачу 2.
# Сохраняйте в лог файл раздельно:
# ○ уровень логирования,
# ○ дату события,
# ○ имя функции (не декоратора),
# ○ аргументы вызова,
# ○ результат.


# Функция получает на вход текст вида: “1-й четверг ноября”, “3-
# я среда мая” и т.п.
# Преобразуйте его в дату в текущем году.
# Логируйте ошибки, если текст не соответсвует формату.

import datetime

WEEKDAYS = {
    "понедельник": 0,
    "вторник": 1,
    "среда": 2,
    "четверг": 3,
    "пятница": 4,
    "суббота": 5,
    "воскресенье": 6
}

MONTHS = {
    "январь": 1,
    "февраль": 2,
    "март ": 3,
    "апрель ": 4,
    "май": 5,
    "июнь": 6,
    "июль": 7,
    "август": 8,
    "сентябрь": 9,
    "октябрь": 10,
    "ноябрь": 11,
    "декабрь": 12
}

def func(datd: str):
    