"""
VALIDATE SUBSEQUENCE
Given two non-empty arrays of integers, write a function that
determines whether the second array is a subsequence of the
first one.
A SUBSEQUENCE of an array is a set of numbers that aren't
necessarily adjacent in the array but that are in the same
order as they appear in the array. For instance, the numbers[1, 3, 4]
form a subsequence of the array [1, 2, 3, 4], and so do the numbers [2, 4]

"""


# 1st Approach
def isValidSequence(arr, subarr):
    arrPointer = 0
    subarrPointer = 0
    while arrPointer < len(arr) and subarrPointer < len(subarr):
        if subarr[subarrPointer] == arr[arrPointer]:
            subarrPointer += 1
        arrPointer += 1
    return subarrPointer == len(subarr)


print(isValidSequence([1, 2, 3, 4], [4, 3]))


