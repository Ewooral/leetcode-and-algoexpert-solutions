def Bubble_sort(array):
    c = 0
    n = c + 1
    while c < len(array) - 1:
        if array[c] > array[n]:
            array[c], array[n] = array[n], array[c]

            Bubble_sort()

    print(array)


Bubble_sort([9, 2, 3, 8, 1, 4])
#            0  1  2  3  4  5
# length of array = 6