import fractions

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

