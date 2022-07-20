# O(n) T, O(1) S
def find_three_largest_num(ari):
    largest = [None] * 3
    for num in ari:
        updateLargest(largest, num)
    return largest


def updateLargest(largest, num):
    if largest[2] is None or num > largest[2]:
        shiftAndUpdate(largest, num, 2)
    elif largest[1] is None or num > largest[1]:
        shiftAndUpdate(largest, num, 1)
    elif largest[0] is None or num > largest[0]:
        shiftAndUpdate(largest, num, 0)


def shiftAndUpdate(array, num, idx):
    '''
    [0, 1, 2]
    [x, y, z]
    updated = [y, z, num]
    for i in range(0, 2+1):
        if i == 2:
            array[2] = num
        else:
            array[2] = array[2 + 1]

    '''
    for i in range(idx + 1):
        if i == idx:
            array[i] = num
        else:
            array[i] = array[i + 1]


# O(n)T, O(n log K) where k is length of largest
def findThreeLargestNum(ari):
    largest = [None] * 3
    i = 0
    while i < len(largest):
        largest[i] = max(ari)
        ari.remove(max(ari))
        i += 1
    largest.sort()
    return largest


def main():
    arr = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]
    print(find_three_largest_num(arr))
    print(findThreeLargestNum(arr))


if __name__ == '__main__':
    main()
