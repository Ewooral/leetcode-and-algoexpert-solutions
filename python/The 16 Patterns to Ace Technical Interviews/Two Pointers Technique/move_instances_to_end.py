"""
Given two inputs, an array of elements and an integer, Find all instances
of the integer in the input array and move them to the end of the array

Eg. Input arr = [2, 1, 2, 2, 2, 3, 4, 2], valueToMove = 2
    Output arr = [1, 3, 4, 2, 2, 2, 2, 2]

constraints
This operation should be done in place
order of the other numbers is not relevant
"""

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


