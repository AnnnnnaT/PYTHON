# ✔ Создайте функцию-генератор. Функция генерирует N простых чисел, начиная с числа 2.
# Для проверки числа на простоту используйте
# правило: «число является простым, если делится
# нацело только на единицу и на себя».

# def prime_gen(n: int):
#     primes = []  
#     num = 2 
#     while len(primes) < n:
#         num_prime = True  
#         for prime in primes:
#             if num % prime == 0:
#                 num_prime = False
#                 break
#         if num_prime:
#             primes.append(num)  
#         num += 1  
#     return primes

# n = int(input("Input number of prime numbers: "))
# res = prime_gen(n)
# print(res)


# ✔ Напишите функцию, которая принимает на вход строку —
# абсолютный путь до файла. Функция возвращает кортеж из трёх
# элементов: путь, имя файла, расширение файла.

# def convert():
#         file_path = input("Input file's path: ")
#         ext = file_path.split(".") 
#         *a, name = ext[0].split("\\")
#         path_ = "\\".join(a)
#         res = path_, name, ext[1] 
#         return res
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

# def fibb():
#     n = int(input("Input your fibonacci limit: "))
#     num = 0
#     num_1 = 1
#     while num < n:
#         yield num
#         num, num_1 = num_1, num + num_1
# print(*fibb())