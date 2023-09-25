'''A permutation of an array of integers is an arrangement of its members into a sequence or linear order. 
    For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1]. 
The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order). 
    For example, the next permutation of arr = [1,2,3] is [1,3,2]. 
    Similarly, the next permutation of arr = [2,3,1] is [3,1,2]. 
    While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement. 
Given an array of integers nums, find the next permutation of nums. 
The replacement must be in place and use only constant extra memory. 
Example 1: 
Input: nums = [1,2,3] 
Output: [1,3,2] 
Example 2: 
Input: nums = [3,2,1] 
Output: [1,2,3] 
Example 3: 
Input: nums = [1,1,5] 
Output: [1,5,1] 
Constraints: 
    1 <= nums.length <= 100 
    0 <= nums[i] <= 100
To find the next permutation of an array of integers, you can follow these steps:

1. Start from the rightmost element and find the first pair of consecutive elements (i, i+1) where nums[i] < nums[i+1].
2. If no such pair is found, it means the array is sorted in descending order. In this case, reverse the entire array to get the lowest possible order.
3. If a pair is found, let the index of the first element be i.
4. Start from the rightmost element again and find the first element j where nums[j] > nums[i].
5. Swap nums[i] with nums[j].
6. Reverse the subarray starting from index i+1 to the end of the array.

Here's an implementation in Python:

'''
def nextPermutation(nums):
    # Step 1: Find the first pair where nums[i] < nums[i+1]
    i = len(nums) - 2
    while i >= 0 and nums[i] >= nums[i+1]:
        i -= 1

    if i >= 0:
        # Step 2: Find the first element greater than nums[i]
        j = len(nums) - 1
        while nums[j] <= nums[i]:
            j -= 1

        # Step 3: Swap nums[i] with nums[j]
        nums[i], nums[j] = nums[j], nums[i]

    # Step 4: Reverse the subarray from i+1 to the end
    left, right = i+1, len(nums)-1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1

    return nums

# Test cases
nums1 = [1, 2, 3]
nums2 = [3, 2, 1]
nums3 = [1, 1, 5]

print(nextPermutation(nums1))  # Output: [1, 3, 2]
print(nextPermutation(nums2))  # Output: [1, 2, 3]
print(nextPermutation(nums3))  # Output: [1, 5, 1]
# This implementation finds the next permutation in place and uses only constant extra memory, as required by the problem statement.



