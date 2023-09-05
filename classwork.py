# ✔ Напишите программу, которая вычисляет площадь
# круга и длину окружности по введённому диаметру.
# ✔ Диаметр не превышает 1000 у.е.
# ✔ Точность вычислений должна составлять
# не менее 42 знаков после запятой.

   
import decimal
import math
decimal.getcontext().prec = 42

diam = decimal.Decimal((input("input diametr: ")))
if diam < 1000:
    s_circle = decimal.Decimal(math.pi) * (diam/2**2)
    length = decimal.Decimal(math.pi) * diam / 2 * 2
    print(s_circle, length, sep ='\n')
else:
    print("sorry")


