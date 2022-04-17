''' 
VALIDATE SUBSEQUENCE 
Given two non-empty arrays of integers, write a function that
determines whether the second array is a subsequence of the 
first one. 
A SUBSEQUENCE of an array is a set of numbers that aren't 
necessarily adjacent in the array but that are in the same 
order as they appear in the array. For instance, the numbers[1, 3, 4]
form a subsequence of the array [1, 2, 3, 4], and so do the numbers [2, 4]

'''
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



# 2nd Approach
# def is_vs(arr, subarr):
    seqI = 0
    for value in arr:
        if seqI == len(subarr):
            break
        if value == subarr[seqI]:
            seqI += 1

    return seqI == len(subarr)


print(is_vs([4, -1, 0, 2, 1, 3, -2], [-1, 2, 3, -2]))
print(is_vs([4, -1, 0, 2, 1, 3, -2], [3, 2, 4]))
