""" 
Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
If all assertions pass, then your solution will be accepted.

 

Example 1:

Input: nums = [1,1,1,2,2,3]
Output: 5, nums = [1,1,2,2,3,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
Example 2:

Input: nums = [0,0,1,1,1,1,2,3,3]
Output: 7, nums = [0,0,1,1,2,3,3,_,_]
Explanation: Your function should return k = 7, with the first seven elements of nums being 0, 0, 1, 1, 2, 3 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
 

Constraints:

1 <= nums.length <= 3 * 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order.

Solution
Approach 1: Popping Unwanted Duplicates
Intuition

The input array is already sorted and hence, all the duplicates 
appear next to each other. The problem statement mentions that we a
re not allowed to use any additional space and we have to modify the
 array in-place. The easiest approach for in-place modifications would
  be to get rid of all the unwanted duplicates. For every number in the
   array, if we detect > 2 duplicates, we simply remove them from the 
   list of elements and we do this for all the elements in the array.



Algorithm

1. The implementation is slightly tricky so to say since we will be
 removing elements from the array and iterating over it at the same
  time. So, we need to keep updating the array's indexes as and when 
  we pop an element else we'll be accessing invalid indexes.
2. Say we have two variables, i which is the array pointer and count 
which keeps track of the count of a particular element in the array
. Note that the minimum count would always be 1.

3. We start with index 1 and process one element at a time in the array.

4.If we find that the current element is the same as the previous element 
i.e. nums[i] == nums[i - 1], then we increment the count. If the value 
of count > 2, then we have encountered an unwanted duplicate element
and we can remove it from the array. Since we know the index of this 
element, we can use the del or pop or remove operation (or whatever operation 
corresponding operation is supported in your language of choice) to 
delete the element at index i from the array. Since we popped an 
element, we decrement the index by 1 as well.

5. If we encounter that the current element is not the same as
 the previous element i.e. nums[i] != nums[i - 1], then it means 
 we have a new element at hand and so accordingly, we update count = 1.


6. Since we are removing all the unwanted duplicates from the 
original array, the final array that remains after process all 
the elements will only contain the valid elements and hence we 
simply return the length of this array.




"""


class Solution(object):
    def remove_duplicates_1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Initialize the counter and the array index.
        i, count = 1, 1
        # Start from the second element of the array and process
        # elements one by one.
        while i < len(nums):
            # If the current element is a duplicate,
            # increment the count.
            if nums[i] == nums[i - 1]:
                count += 1

                # If the count is more than 2, this is an
                # unwanted duplicate element and hence we
                # remove it from the array.
                if count > 2:
                    nums.pop(i)

                    # Note that we have to decrement the
                    # array index value to keep it consistent
                    # with the size of the array.
                    i -= 1
            else:

                # Reset the count since we encountered a different element
                # than the previous one
                count = 1
            # Move on to the next element in the array
            i += 1

        return len(nums)

""" 
Complexity Analysis

Time Complexity: Let's see what the costly operations in our array are:
We have to iterate over all the elements in the array. Suppose that the original array contains N elements, the time taken here would be O(N)O(N).
Next, for every unwanted duplicate element, we will have to perform a delete operation and deletions in arrays are also O(N)O(N).
The worst case would be when all the elements in the array are the same. In that case, we would be performing N - 2N−2 deletions thus giving us O(N^2)O(N2) complexity for deletions
Overall complexity = O(N) + O(N^2) \equiv O(N^2)O(N)+O(N2)≡O(N2).
Space Complexity: O(1)O(1) since we are modifying the array in-place.
"""

# APPROACH TWO 
#Clean code: (.


class Solution:
    def remove_duplicates_2(self, nums):
        if not nums:
            return 0
        i = 0
        for n in nums:
            if i < 2 or n > nums[i - 2]:
                nums[i] = n
                i += 1
        return i


# APPROACH THREE
class Solution(object):
    def remove_duplicates_3(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Initialize the counter and the second pointer.
        j, count = 1, 1

        # Start from the second element of the array and process
        # elements one by one.
        for i in range(1, len(nums)):
            # If the current element is a duplicate,
            # increment the count.
            if nums[i] == nums[i - 1]:
                count += 1
            else:
                # Reset the count since we encountered a different element
                # than the previous one
                count = 1
            
            # For a count <= 2, we copy the element over thus
            # overwriting the element at index "j" in the array
            if count <= 2:
                nums[j] = nums[i]
                j += 1
        return j

""" 
Complexity Analysis

Time Complexity: O(N) since we process each element exactly once.
Space Complexity: O(1).
"""
