from collections import Counter


def maxFrequency1(arr, n):
    arr.sort()
    lastItem = arr.pop()
    i, j = 0, len(arr) - 1
    newArr = [lastItem]
    while j > i - 1 or len(arr) > 0:
        limit = n
        k = 0
        elemNearLast = arr[j]
        while k < limit :
            elemNearLast += 1
            if elemNearLast == lastItem:
                newArr.append(elemNearLast)
                arr.pop(j)
                j -= 1
                if len(arr) > 0:
                    elemNearLast = arr[j]
            k += 1
    freq = Counter(newArr)
    for k, v in enumerate(freq.values()):
        return v

def main():
    # print(maxFrequency1([1, 2, 4], 5))
    print(maxFrequency1([1, 4, 8, 13], 5))
    # print(maxFrequency1([3, 9, 6], 2))
    # print(maxFrequency1([3, -19, 7, 6], 22))
    print(maxFrequency1([9940,9995,9944,9937,9941,9952,9907,9952,9987,9964,9940,
                         9914,9941,9933,9912,9934,9980,9907,9980,9944,9910,9997], 7925))
    print(maxFrequency1([9990, 9995, 9984, 9987], 7925))


if __name__ == '__main__':
    main()
