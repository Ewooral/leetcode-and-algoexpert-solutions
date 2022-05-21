def selection_sort(array):
    for i in range(len(array)):
        min_index = i
        for j in range(i + 1, len(array)):
            if array[min_index] > array[j]:
                min_index = j
        # array[i], array[min_index] = array[min_index], array[i]
        swap(array, i, min_index)
    return array


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]


print("Approach 1: ", selection_sort([9, 2, 3, 8, 4]))


# O(n^2) T, O(1) S
def Selection_Sort(customList):
    currentIndex = 0
    while currentIndex < len(customList) - 1:
        minValueIndex = currentIndex
        for i in range(currentIndex + 1, len(customList)):
            if customList[minValueIndex] > customList[i]:
                minValueIndex = i
        swap1(currentIndex, minValueIndex, customList,)
        currentIndex += 1
    return customList


def swap1(i, j, array):
    array[i], array[j] = array[j], array[i]


print("Approach 2: ", Selection_Sort([9, 2, 3, 8, 4]))
