"""
238. Product of Array Except Self
Medium

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.



Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]


Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.


Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
"""

# T = O(n^2), S = O(n)
def array_of_product(array):
    # products = [1 for _ in range(len(array))];
    final_products = [None] * len(array);

    for i in range(len(array)):
        currentProduct = 1;
        for j in range(len(array)):
            if i != j :
                currentProduct *= array[j]
        final_products[i] = currentProduct
    return final_products


print("1st Approach: ", array_of_product([5, 1, 4, 2]))  # [8, 40, 10, 20]


# T = O(n), S = O(n)
def array_of_product2(arr):
    leftProduct, rightProduct, product = [1] * len(arr), [1] * len(arr), [1] * len(arr)
    # print(left, right, product)
    left_product = 1   
    for i in range(len(arr)):
        leftProduct[i] = left_product
        left_product *= arr[i]

    right_product = 1
    for i in range(len(arr)-1, -1, -1):
        rightProduct[i] = right_product
        right_product *= arr[i]

    for i in range(len(arr)):
        product[i] = leftProduct[i] * rightProduct[i]
    return product


print("2nd Approach: ", array_of_product2([5, 1, 4, 2]))  # [8, 40, 10, 20]


def arr_P(arr):
    mainProduct = [1] * len(arr) # where mP is MainProduct

    leftProduct = 1
    for i in range(len(arr)):
        mainProduct[i] = leftProduct
        leftProduct = leftProduct * arr[i]

    rightProduct = 1
    for i in reversed(range(len(arr))):
        mainProduct[i] *= rightProduct
        rightProduct = rightProduct * arr[i]
    return mainProduct


print("3rd Approach: ", arr_P([2, 5, 1, 4]))
