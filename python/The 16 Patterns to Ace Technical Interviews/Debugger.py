def swapNode(arr):
    l = 0
    r = l + 1
    lastI = 1
    if len(arr) % 2 == 1:
        lastItem = arr.pop()
        lastI *= lastItem
    while r <= len(arr):
        arr[l], arr[r] = arr[r], arr[l]
        l += 2
        r += 2
    arr.append(lastI)
    return arr


def main():
    # li = [0, 1, 2]
    li = [0, 1, 2, 3, 4, 5, 6]
    print(swapNode(li))


if __name__ == '__main__':
    main()
