def moveZeroes(arr):
    count_nonzero_elements = 0
    for element in arr:
        if element != 0:
            arr[count_nonzero_elements] = element
            count_nonzero_elements += 1

    for index_of_zero_elements in range(count_nonzero_elements, len(arr)):
        arr[index_of_zero_elements] = 0

    return arr


array = [0, 1, 0, 3, 12]
print(moveZeroes(array))

""" Example:      0 1 0 3 12 

#  Expected Output: 1 3 12 0 0

#  We are to push all zeros to the end of the array and 
#  maintain the order of the non zero elements in the array
# """
