def sort(arr: list):
    res = []
    i = 0
    while len(arr) > 0:
        mini = min(arr)
        res.insert(i, mini)
        arr.remove(mini)
        i += 1
    return res


def main():
    arr = [8, -2, 1, 3]
    sort(arr)


main()
