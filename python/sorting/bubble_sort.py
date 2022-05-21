def Bubble_sort(array):
    for i in range(len(array) - 1):
        for j in range(len(array) - 1):
            if array[j] > array[j + 1]:
                swap(j, j + 1, array)
    print("Approach 1: ", array)


def swap(i, j, array):
    array[i], array[j] = array[j], array[i]


Bubble_sort([9, 2, 3, 8, 1, 4])


# Worse Case:  O(n^2)T, O(1) T
# Best Case:  O(n)T, O(1) T, thus if the array is sorted

# APPROACH TWO
def Bubble_Sort(array):
    isSorted = False
    # counter keeps track of the sorted region on the right and avoid
    # looping through that region since it is already sorted
    counter = 0
    while not isSorted:
        isSorted = True
        for i in range(len(array) - 1 - counter):
            if array[i] > array[i + 1]:
                swap1(i, i + 1, array)
                isSorted = False
        counter += 1
    return array


def swap1(i, j, array):
    array[i], array[j] = array[j], array[i]


print("Approach 2: ", Bubble_Sort([9, 2, 3, 8, 1, 4]))
