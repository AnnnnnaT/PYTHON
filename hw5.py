# ✔ Создайте функцию-генератор. Функция генерирует N простых чисел, начиная с числа 2.
# Для проверки числа на простоту используйте
# правило: «число является простым, если делится
# нацело только на единицу и на себя».

def prime_generator(N):
    primes = []  
    num = 2 
    while len(primes) < N:
        is_prime = True  
        for prime in primes:
            if num % prime == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)  
        num += 1  

    return primes

N = 10
primes = prime_generator(N)


[2, 3, 5, 7, 11, 13, 17]

# def check_num(num: int):
#     for i in range(2,num):
#         if num % i != 0:
#             return True

# def gener_func(n: int):
#     for num in range(2, n+1):
#         if check_num(num):
#             yield num
# print(*gener_func(10))

def is_prime(num):
    del_ = 2
    while del_ ** 2 < num and num % del_ != 0:
        del_ += 1
    return del_ ** 2 > num


def gen_is_prime(number):
    """Генератор простых чисел от 2 до n"""
    start = 1
    while number > 1:
        start += 1
        number -= 1
        if is_prime(start):
            yield start


print(*gen_is_prime(100))

# ✔ Напишите функцию, которая принимает на вход строку —
# абсолютный путь до файла. Функция возвращает кортеж из трёх
# элементов: путь, имя файла, расширение файла.
# C:\Users\User\Desktop\hw1\hw3.py

# file_path = input("Input file's path: ")
# def convert():
#         file_path = input("Input file's path: ")
#         *a, b, c = file_path.split("\\").split(".")                                 
#         return tuple({f'path: {a}, name: {b}, extension: {c}'})
# print(convert())

# ✔ Напишите однострочный генератор словаря, который принимает
# на вход три списка одинаковой длины: имена str, ставка int,
# премия str с указанием процентов вида «10.25%». В результате
# получаем словарь с именем в качестве ключа и суммой
# премии в качестве значения. Сумма рассчитывается
# как ставка умноженная на процент премии

# names = ["Tom", "Jack", "Mary"]
# salary = [20000, 10000, 50000]
# bonus = ["10.25%", "5%", "3.2%"]

# res =  {n : s*float(b.replace('%',''))//100 for n, s, b in zip(names, salary, bonus, strict = False)}
# print(res)

# ✔ Создайте функцию генератор чисел Фибоначчи (см. Википедию).
# def fibb(n: int):
#     lst = [item for item in range(1, n+1)]
#     num = iter(lst)
#     for i in num:
#         if num.next().next() == num.next() + i:
#             yield i
# print(*fibb(10))