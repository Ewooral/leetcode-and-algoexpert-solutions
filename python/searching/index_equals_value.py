"""
Given an array of integers, check if the first integer in the array
is equal to its index return the integer, do better complexity than O(n)T

input: arr = [8, 1, 2, 12, 15, 1000]
output: 1, because, integer 1 is at the position of 1
"""


# O(n) T, O(1) S
def index_equal_value(arr):
    for i in range(len(arr)):
        if i == arr[i]:
            return arr[i]
    return -1


# O(log N) T, O(1) S
def indexEqualValue(arr):
    i = 0
    j = len(arr) - 1
    mid = (i + j) // 2
    while i <= mid:
        print("first: ", arr[i])
        if arr[i] == i:
            return arr[i]
        i += 1
        # while i > mid and i <= j: OR
    print()
    while mid < i <= j:
        print("second: ", arr[i])
        if arr[i] == i:
            return arr[i]
        i += 1
    return -1


def main():
    arr = [8, 1, 2, 12, 15, 1000]
    arr1 = [85, 7, 20, 12, 78, 5]

    print("final answer: ", index_equal_value(arr))
    print("final answer: ", indexEqualValue(arr1))


if __name__ == '__main__':
    main()
