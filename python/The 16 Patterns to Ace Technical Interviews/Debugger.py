# INSERTION SORT
"""
1. First Item in the list is always deemed as sorted.
2. Traverse each item in the list starting from the second item and find the minimum
3. Compare the item to the sorted item. If sorted item is lesser, do nothing, else, swap both items.

kye = [9, 2, 3, 8, 10, 1, 4]
      [2, 3, 8, 9, 1, 4, 10]

i = 0
j = 0
"""

lst = [2, 0, 1, 7, -12]
kye = [9, 2, 3, 8, 10, 1, 4]


def Bubble_sort(array):
    for i in range(len(array) - 1):
        for j in range(len(array) - 1):
            if array[j] > array[j+1]:
                array[j+1], array[j] = array[j], array[j+1]
    print("Approach 1: ", array)


print(Bubble_sort(lst))
