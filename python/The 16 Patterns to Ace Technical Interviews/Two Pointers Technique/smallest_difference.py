def smallest_difference(arr1, arr2):
    arr1.sort()
    arr2.sort()
    l = r = 0
    smallest = float("inf")
    current = float("inf")
    smallestPair = []
    while l < len(arr1) and r < len(arr2):
        firstNum = arr1[l]
        secondNum = arr2[r]
        # current = abs(firstNum - secondNum)
        if firstNum < secondNum:
            current = secondNum - firstNum
            l += 1
        elif secondNum < firstNum:
            current = firstNum - secondNum
            r += 1
        else:
            return [firstNum, secondNum]
        if smallest > current:
            smallest = current
            smallestPair = [firstNum, secondNum]
    return smallestPair


print(smallest_difference([-1,5, 10, 20, 28, 3], [20, 26, 134, 135, 15, 17]))