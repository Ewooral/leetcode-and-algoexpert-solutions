# Quick sort in Python

# function to find the partition position
def partition(array, low, high):
    # choose the rightmost element as pivot
    pivot = array[high]

    # pointer for greater element
    i = low - 1

    # traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:
            # if element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1

            # swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])

    # swap the pivot element with the greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])

    # return the position from where partition is done
    return i + 1


# function to perform quicksort
def quickSort(array, low, high):
    if low < high:
        # find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(array, low, high)

        # recursive call on the left of pivot
        quickSort(array, low, pi - 1)

        # recursive call on the right of pivot
        quickSort(array, pi + 1, high)


data = [8, 7, 2, 1, 0, 9, 6]
print("Unsorted Array")
print(data)

size = len(data)

quickSort(data, 0, size - 1)

print('Sorted Array in Ascending Order:')
print(data)
'''
Time Complexity	 
Best	O(n*log n)
Worst	O(n2)
Average	O(n*log n)
Space Complexity	O(log n)
Stability	No
'''


# AlgoExpert Version
def quickSort(array):
    quickSortHelper(array, 0, len(array) - 1)
    return array


# startIndex = s, endIndex = e
def quickSortHelper(array, s, e):
    if s >= e:
        return
    # pivot = p
    # leftIndex = l
    # rightIndex = r
    p = s
    l = s + 1
    r = e
    while r >= l:
        # if array[l] > array[p] and array[r] < array[p]: OR the second one
        if array[l] > array[p] > array[r]:
            swap(l, r, array)
        if array[l] <= array[p]:
            l += 1
        if array[r] >= array[p]:
            r -= 1
    swap(p, r, array)
    leftSubarrayIsSmaller = r - 1 - s < e - (r + 1)
    if leftSubarrayIsSmaller:
        quickSortHelper(array, s, r - 1)
        quickSortHelper(array, r + 1, e)
    else:
        quickSortHelper(array, r + 1, e)
        quickSortHelper(array, s, r - 1)


def swap(i, j, array):
    array[i], array[j] = array[j], array[i]


'''
Time Complexity	 
Best	O(n*log n)
Worst	O(n2)
Average	O(n*log n)
Space Complexity	O(log n)
Stability	No
'''

print(quickSort([8, 7, 2, 1, 0, 9, 6]))