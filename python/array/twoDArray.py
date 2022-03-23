import numpy as np;
twoDarray = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(twoDarray);  

newtwoDarray = np.insert(twoDarray, 0, [[10, 11, 12]], axis=1)
print(newtwoDarray);

# def printElement(array):
#     for i in range(len(array)):
#         for j in range(len(array)):
#             return array[1][1]
#     return []

# print(printElement(newtwoDarray))