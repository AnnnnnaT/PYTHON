
from random import randint

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

# 4. 

# UPPER_LIMIT = 1000
# attempt = 1
# num = randint(LOWER_LIMIT, UPPER_LIMIT)
# while attempt < 11:
#     user_num = int(input("Input number from 0 to 1000: "))
#     if user_num != num:
#         if user_num < num:
#             print("Attempt ", attempt)
#             print("Your number is less than ours. Try again!")
#             print()
#             attempt+=1
#         elif user_num > num:
#             print("Attempt ", attempt)
#             print("Your number is more than ours. Try again!")
#             print()
#             attempt+=1
#     else: 
#         print("Attempt ", attempt)
#         print("You're right, the number is ", user_num)
# print("Attempts are over.")