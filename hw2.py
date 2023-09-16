from fractions import Fraction

# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление. 
# Функцию hex используйте для проверки своего результата.

# num = int(input("Input your number: "))
# res = ""
# while num > 16:
#     res += str(num // 16)
#     reminder = "" 
#     if (num % 16 > 9):
#         if(num % 16 == 10):
#             reminder = "A"
#         elif (num % 16 == 11):
#             reminder = "B"
#         elif (num % 16 == 12):
#              reminder = "C"
#         elif (num % 16 == 13):
#              reminder = "D"
#         elif (num % 16 == 14):
#              reminder = "E"
#         elif (num % 16 == 15):
#              reminder = "F"
#     else: 
#         reminder = str(num % 16)   
#     num = num // 16
#     res = res + reminder 
    
# print (res)
# print(hex(num))



# Напишите программу, которая принимает две строки вида “a/b” - 
# дробь с числителем и знаменателем. Программа должна возвращать сумму и произведение* дробей.
# Для проверки своего кода используйте модуль fractions.

# num_1 = input("Input num like a/b: ")
# num_2 = input("Input num like a/b: ")
# print()

# if(int(num_1.split('/')[1]) != int(num_2.split('/')[1])):
#     if(int(num_1.split('/')[1]) > int(num_2.split('/')[1])):
#         if(int(num_1.split('/')[1]) % int(num_2.split('/')[1]) == 0):
#             common = int(num_1.split('/')[1])  
#         else:
#             common = int(num_1.split('/')[1]) * int(num_2.split('/')[1])       
#     elif(int(num_1.split('/')[1]) < int(num_2.split('/')[1])):
#         if(int(num_2.split('/')[1]) % int(num_1.split('/')[1]) == 0):
#             common = int(num_2.split('/')[1])
#         else:
#             common = int(num_1.split('/')[1]) * int(num_2.split('/')[1])
#     numerator_1 = common//int(num_1.split('/')[1]) * int(num_1.split('/')[0])
#     numerator_2 = common//int(num_2.split('/')[1]) * int(num_2.split('/')[0])
#     numerator = numerator_1 + numerator_2 
#     print(f'{num_1} + {num_2} = {numerator}/{common}')
#     print()
# else:
#     numerator = int(num_1.split('/')[0]) + int(num_2.split('/')[0])
#     common =  int(num_1.split('/')[1])
#     print(f'{num_1} + {num_2} = {numerator}/{common}')
#     print()


# res_numerator = int(num_1.split('/')[0]) * int(num_2.split('/')[0])
# res_denumerator = int(num_1.split('/')[1]) * int(num_2.split('/')[1])
# print(f'{num_1} * {num_2} = {res_numerator}/{res_denumerator}')


first = input("Input first fraction: ").split("/")
second = input("Input second fraction: ").split("/")

num_sum = int(first[0]) * int(second[1]) + int(first[1]) * int(second[0])
denom_sum = int(first[1]) * int(second[1])
sum_fract = [num_sum, denom_sum]

multi_fract = [int(first[0]) * int(second[0]), int(first[1]) * int(second[1])]

#сокращать

a1, b1 = sum_fract
while b1:
    a1, b1 = b1, a1 % b1
a2, b2 = multi_fract
while b2:
    a2, b2 = b2, a2 % b2

print(f'{sum_fract[0]}, {sum_fract[1]}, {a1}, {b1}')
print(f'{sum_fract[0]//a1}/{sum_fract[1]//a1}', f'{multi_fract[0]//a2}/{multi_fract[1]//a2}')


res_1 = Fraction(f"{first[0]}/{first[1]}")
res_2 = Fraction(f"{second[0]}/{second[1]}")
print(res_1 + res_2,res_1 * res_2)