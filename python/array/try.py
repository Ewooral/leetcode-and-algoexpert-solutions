# def solve(A, result=0):
#     B = sorted(A)
#     print(B)
#     for i in range(len(A)):
#         for j in range(len(A)):
#             if A[i] == A[j]:
#                 result = max(result, abs(i - j))

#     return result


# print(solve([4, 6, 2, 2, 6, 6, 1]))


# # T = nlogn, S = O(1)
# def miniMaxSum(arr):
#     # Write your code here
#     miminum_values = 0
#     maximum_values = 0
#     arr.sort()
#     for i in range(0, len(arr)-1):
#         miminum_values = miminum_values + arr[i]

# # range(lower bound, upper bound, increment value)
#     for i in range(len(arr)-1, 0, -1):
#         maximum_values = maximum_values + arr[i]
    
#     print(miminum_values, maximum_values)

# miniMaxSum([1, 9, 5, 7, 3])
# # miniMaxSum([1, 5, 2, 3, 4])

# # list = ['Mon', 'Tue', 'Wed', 'Thu']
# # for i in list[2::-1]:
# #    print(i)

