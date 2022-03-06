def duplicate_removal(array):
    hashset = set()
    for element in range(len(array)):
        if array[element] in hashset:
            return True, hashset
        hashset.add(array[element])
    return False


print(duplicate_removal([1, 3, 6, 3, 2, 6, 1, 2, 3, 1, 4, 5,  6, 2, 0]))
