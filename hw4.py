# 1

# matrix = [[1,2,3],
#          [4, 5, 6],
#          [7, 8, 9]]


# def trans_matrix(matrix:list[list]):
#     trans_matrix = [[0 for j in range(len(matrix))] for i in range(len(matrix[0]))]
#     for i in range(len(matrix)):
#         for j in range(len(matrix[0])):
#             trans_matrix[j][i] = matrix[i][j] 
#     return trans_matrix


# print(matrix)
# print(trans_matrix(matrix))


#2


# def func(**kwargs):
#     return {value : key for key, value in kwargs.items()}

# print(func(a = "e", b = 7, c = [2,8,9]))