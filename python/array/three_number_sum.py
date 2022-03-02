class three_sum_number:
     def three_sums(self, array, target_sum):
         for i in range(len(array) - 1):
             current_num = array[i]
             for j in range(i + 1, len(array)):
                 next_num = array[j]
                 for k in range(j + 1, len(array)):
                     last_num = array[k]
                     if current_num + next_num + last_num == target_sum:
                         return [current_num, next_num, last_num]
         return []


three_sum = three_sum_number()
print(three_sum.three_sums([4, 1, 2, 3, 4, 5, -5, 6, -1], 6))
# array = [4, 1, 2, 3, 4, 5, -5, 6, -1]
# target_sum = 6
# T = 0(n^3)
# S = 0(1)
 

def threeNumberSum(array, targetSum):
    # targetSum = current + left + right
	array.sort()
	trip = []
	for num in range(len(array)-2):
         current = array[num]
         left = num + 1
         right = len(array) - 1
         while left < right:
            current_sum = current + array[left] + array[right]
            if current_sum == targetSum:
                trip.append([current, array[left], array[right]])
                left += 1
                right -= 1
            elif current_sum < targetSum:
                        left += 1
            elif current_sum > targetSum:
                        right -= 1
         return trip


print(threeNumberSum([12, 3, 1, 2, -6, 5, -8, 6], 0))

# array [12, 3, 1, 2, -6, 5, -8,  6]
# sorted array [-8, -6, 1, 2, 3, 5, 6, 12] 2
# tagetSum = 0
# [[5, 1, -6], [-8, 2, 6], [-8, 3, 5]]
#


# APPROACH THREE
""" 
Algorithm

The implementation is straightforward - we just need to modify twoSumII to produce triplets and skip repeating values.

For the main function:

Sort the input array nums.
Iterate through the array:
If the current value is greater than zero, break from the loop. Remaining values cannot sum to zero.
If the current value is the same as the one before, skip it.
Otherwise, call twoSumII for the current position i.
For twoSumII function:

Set the low pointer lo to i + 1, and high pointer hi to the last index.
While low pointer is smaller than high:
If sum of nums[i] + nums[lo] + nums[hi] is less than zero, increment lo.
If sum is greater than zero, decrement hi.
Otherwise, we found a triplet:
Add it to the result res.
Decrement hi and increment lo.
Increment lo while the next value is the same as before to avoid duplicates in the result.
Return the result res.
"""
class Solution:
    def threeSum(self, nums):
        res = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i - 1] != nums[i]:
                self.twoSumII(nums, i, res)
            return res


    def twoSumII(self, nums, i, res):
        lo, hi = i + 1, len(nums) - 1
        while (lo < hi):
            sum = nums[i] + nums[lo] + nums[hi]
            if sum < 0:
                lo += 1
            elif sum > 0:
                hi -= 1
            else:
                res.append([nums[i], nums[lo], nums[hi]])
                lo += 1
                hi -= 1
                while lo < hi and nums[lo] == nums[lo - 1]:
                    lo += 1

myThree = Solution()
print(myThree.threeSum([12, 3, 1, 2, -6, 5, -8, 6]))
""" 
Complexity Analysis

Time Complexity: O(n^2). twoSumII is O(n), and we call it n times.
Sorting the array takes O(nlogn), so overall complexity is 
O(nlogn+n2). This is asymptotically equivalent to O(n2).

Space Complexity: from O(logn) to O(n), depending on the 
implementation of the sorting algorithm. For the purpose of 
complexity analysis, we ignore the memory required for the output.
"""


class Solution1:
    def three_sum(self, nums):
        res = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i - 1] != nums[i]:
                self.two_sum(nums, i, res)
        return res

    def two_sum(self, nums, i, res):
        lo, hi = i + 1, len(nums) - 1
        while (lo < hi):
            sum = nums[i] + nums[lo] + nums[hi]
            if sum < 0:
                lo += 1
            elif sum > 0:
                hi -= 1
            else:
                res.append([nums[i], nums[lo], nums[hi]])
                lo += 1
                hi -= 1
                while lo < hi and nums[lo] == nums[lo - 1]:
                    lo += 1


myThreeI = Solution1()
print(myThreeI.three_sum([12, 3, 1, 2, -6, 5, -8, 6]))
