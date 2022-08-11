def traverse_nD_array(arr):
    i = 0
    j = 0
    res = []
    while i < len(arr):
        res.append(arr[i][j])
        j += 1
        if j == len(arr[i]):
            i += 1
            j = 0

    return res


arr= [
       [1, 5, 9, 21],
       [-1, 0],
       [-124, 81, 121],
       [3, 6, 12, 20, 150]
 ]
print(traverse_nD_array(arr))