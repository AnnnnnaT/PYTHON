# 1.Решить задачи, которые не успели решить на семинаре.
# 2.Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей. Дано a, b, c - стороны предполагаемого треугольника. 
# Требуется сравнить длину каждого отрезка-стороны с суммой двух других. Если хотя бы в одном случае отрезок окажется больше суммы двух других, 
# то треугольника с такими сторонами не существует. Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.
# 3. Напишите код, который запрашивает число и сообщает является ли оно простым или составным. Используйте правило для
# проверки: “Число является простым, если делится нацело только на единицу и на себя”. Сделайте ограничение на ввод 
# отрицательных чисел и чисел больше 100 тысяч.



# 1

# for i in range(2, 10, 4):
#     for j in range(2, 11):    
#         for k in range (i, i + 4):
#             print(k, 'x', j, '=', k*j,  end = '\t')
#         print()
#     print()


# 2

# a = int(input('Input 1st side: '))
# b = int(input('Input 2nd side: '))
# c= int(input('Input 3rd side: '))
# if a + b > c and a + c > b and c + b > a:
#     print("You have scalene triangle!")
#     if a == b == c:
#         print("You have equilateral triangle!")
#     elif a == b or b == c or a == c:
#         print("You have isosceles triangle!")
# else:
#     print("A triangle with such sides doesn't exists!")


# 3

# num = int(input("Input number that's more than a 0 and  less than 100 thousand"))
# if 0 < num < 100000:
#     for i in range(1,num):
#         if num % i == 0:
#             print("You have a composite number")
#         else:
#             print("You havea a prime number")
# else:
#     print("Your number is out of range")