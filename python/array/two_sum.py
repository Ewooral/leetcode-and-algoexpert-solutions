'''TWO NUMBER sum
Write a function that takes in a non-empty array of distinct integers 
and an integer representing a target sum. If any two numbers in the array sum
up to the target sum, the function should return them in an array, 
in any order. If no two numbers sum up to the target sum, 
the function should return an empty array.

SAMPLE INPUT
array = [3, 5, -4, 8, 11, 1, -1, 6]
targetSum = 10

'''




def two_number_sum(array, target_sum):
    # Write your code here. 
    # O(n^2) time complexity
    # O(1) space complexity
    for i in range(len(array) - 1 ):
        current = array[i]
        for j in range(i+1, len(array)):
            next_value = array[j]
            if current + next_value == target_sum:
                return [current, next_value]
    return []


print(two_number_sum([3, 5, -4, 8, 11, 1, -1, 6], 10))
print(two_number_sum([4,6,1,-3], 3))
print(two_number_sum([0,2,4,6,8,10], 12))
print(two_number_sum([3, 5, -4, 8, 11, 1, -1, 6], 15))
print(two_number_sum([8, -1, 1, 3, 5, 6, -4, 11], 13))

# APPROACH TWO - Two sum using hash table
# x + y = target_sum
# x = target_sum - y
# y = current

class two_number_sum:
    def two_number_sum_hash(self, array, target_sum):
        # Write your code here. 
        # O(n) time complexity
        # O(n) space complexity
        hash_table = {}
        for i in range(len(array)):
            current = array[i]
            if target_sum - current in hash_table:
                return [current, target_sum - current]
            else:
                hash_table[current] = True 
        return []   
# instance of the class 
two_sum = two_number_sum()
print(two_sum.two_number_sum_hash([3, 5, -4, 8, 11, 1, -1, 6], 10))
print(two_sum.two_number_sum_hash([4,6,1,-3], 3))
print(two_sum.two_number_sum_hash([0,2,4,6,8,10], 12))
print(two_sum.two_number_sum_hash([3, -2, 1, 9, -1], 0))


# pointer method
# O(nlogn)T, O(1)S
class two_sum_pointer(): 
    def two_sums(self, array, target_sum):
        left = 0;
        right = len(array) - 1
        sum = []
        while left < right: # while both variables haven't overlapped
            current_sum = array[left] + array[right]
            if current_sum == target_sum:
                sum.append([array[left], array[right]])
            elif current_sum > target_sum:
                right -= 1 
            elif current_sum < target_sum:
                left += 1
        return sum




pointer = two_sum_pointer() # instance of the class 
print(pointer.two_sums([1, -1, 2, 4, -2, 8, 3, -3, -8], 0))
# print(pointer.two_sums([1, 4, 3, -1, 11, 8], 0))




# array = [1, 4, 3, -1, 11, 8]
# sort the array. [-1, 1, 3, 4, 8, 11]

# target_sum = 0

#currentSum = left + right
# currentSum must be equal to targetSum ( currentSum == targetSum )
