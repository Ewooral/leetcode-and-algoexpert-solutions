def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j] < arr[j-1]:
            swap(j, j-1, arr)
            j -= 1
    return arr


def swap(i, j, arr):
    arr[i], arr[j] = arr[j], arr[i]


if __name__ == '__main__':
    print(insertion_sort([200, -234, 0, 2, 99, 1000, -18, 22, 1]))

# OR
def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j] < arr[j-1]:
            arr[i], arr[j] = arr[j], arr[i]
            j -= 1
    return arr
