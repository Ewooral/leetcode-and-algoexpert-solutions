def duplicate_removal(array):
    hashset = set()
    for element in range(len(array)):
        if array[element] in hashset:
#             return True, hashset
#         hashset.add(array[element])
#     return False


# print(duplicate_removal([1, 2, 3, 6, 3, 6, 2, 1, 4, 5,  6, 0]))
# print(duplicate_removal([1, 2, 3, 6, 0]))
