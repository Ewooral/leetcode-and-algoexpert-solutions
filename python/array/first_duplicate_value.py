# First Duplicate value
# O(N)T, S
def first_Duplicate(arr):
    hash_set = set()
    for value in arr:
        if value in hash_set:
            return value
        hash_set.add(value)
    return -1


# O(N)T, O(1)T
def first_duplicate(arr):
    # Index = value - 1
    for value in arr:
        absValue = abs(value)
        # if value is a negative return it
        Index = absValue - 1
        if arr[Index] < 0:
            return absValue
        # else set values to negatives
        arr[Index] *= -1
    return -1


# O(N^2)t, O(1)s
def first_duplicate_I(arr):
    # duplicate Index = dI
    dI = len(arr)
    for i in range(len(arr)):
        value = arr[i]
        for j in range(i + 1, len(arr)):
            valueToCompare = arr[j]
            if value == valueToCompare:
                dI = min(dI, j)
    if dI == len(arr):
        return -1
    return arr[dI]


def main():
    arr2 = [4, 3, 5, 1, 5, 1, 2, 3, 3, 4]
    print(first_duplicate_I(arr2))
    print(arr2)
    print(first_Duplicate(arr2))
    print(arr2)
    print(first_duplicate(arr2))
    print(arr2)


if __name__ == '__main__':
    main()

