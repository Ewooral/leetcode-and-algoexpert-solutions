def selection_sort(arr):
    for i in range(len(arr)):
        minIdx = i
        for j in range(i+1, len(arr)):
            if arr[minIdx] > arr[i]:
                minIdx = j
        swap(i, minIdx, arr)

    return arr


def swap(i, j, arr):
    arr[i], arr[j] = arr[j], arr[i]


def main():
    # arr = [-5, -2, 1, 3]
    # arr1 = [8, -2, 1, 3]
    arr2 = [8, 7, 2, 1, 0, 9, 6]
    print(selection_sort(arr2))

main()