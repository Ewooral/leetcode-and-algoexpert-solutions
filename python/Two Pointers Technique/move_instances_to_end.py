# O(N)T, O(1)S
def move_instances_to_end(arr, move_value):
    # arr = [2, 1, 2, 2, 2, 3, 4, 2]
    l = 0
    r = len(arr) - 1
    while l < r:
        while l < r and arr[r] == move_value:
            r -= 1
        if arr[l] == move_value:
            arr[l], arr[r] = arr[r], arr[l]
        l += 1
    return arr


print(move_instances_to_end([2, 1, 2, 2, 2, 3, 4, 2], 2))


