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


def main():
    arr = [8, -2, 1, 3]
    print(Bubble_Sort(arr))
    Bubble_sort([9, 2, 3, 8, 10, 1, 4])

main()