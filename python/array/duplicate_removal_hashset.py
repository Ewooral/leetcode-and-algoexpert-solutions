from tkinter import E


def duplicate_removal(array):
    hashset = set()
    print(array)
    for element in range(len(array)):
        hashset.add(array[element])
    return hashset;


print(duplicate_removal([1, 2, 3, 6, 3, 6, 2, 1, 4, 5,  6, 0]))
print(duplicate_removal([1, 2, 3, 6, 0]))
