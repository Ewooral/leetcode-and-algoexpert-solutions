# O(n) time, O(1) space
def kadanes_algorithm(array):
    currentMax = finalMax = array[0]
    for num in array[1:]:
        currentMax = max(num, currentMax + num)
        finalMax = max(finalMax, currentMax)
    return finalMax


# print(kadanes_algorithm([3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]))
print(kadanes_algorithm([4, 2, 1, -9, 8, 1, 2, -8, 1, 0]))