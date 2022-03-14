def moveZeroes(arr):
    count_nonzero_elements = 0
    for element in arr:
        if element != 0:
            arr[count_nonzero_elements] = element
            count_nonzero_elements += 1

    for index_of_zero_elements in range(count_nonzero_elements, len(arr)):
        arr[index_of_zero_elements] = 0

    return arr, "No of non-zero elements: " + str(count_nonzero_elements)


array = [0, 1, 0, 3, 12]
array_II = [0, 8, -2, 1, 0 ]
array_III = [ 0]
array_IV = [0, 4, -2, 0]

print(moveZeroes(array)) 
print(moveZeroes(array_II)) 
print(moveZeroes(array_III)) 
print(moveZeroes(array_IV)) 

"""  
 Question:
 We are to push all zeros to the end of the array and 
 maintain the order of the non zero elements in the array

    Example:      0, 1, 0, 3, 12 

 Expected Output: 1, 3, 12, 0, 0
 
"""
