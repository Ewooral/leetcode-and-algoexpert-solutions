'''
given an array of integers nums, there is a sliding window of
size k which is moving from the very left of the array to the
very right. You can only see the k numbers in the window.
Each time the sliding window moves right by one position
Return the max sliding window.

Eg. nums = [1, 3, -1, -3, 5, 3, 6, 7], k=3
output: = [3, 3, 5, 5, 6, 7]
'''
from typing import List


def max_sliding_window(nums: List[int], k: int) -> List:
    output = []
    Queue = []
    l = r = 0
    while r < len(nums):
        # pop smaller values from q
        while len(Queue) >= 1 and nums[Queue[-1]] < nums[r]:
            # nums[Queue[-1] points to the left value in nums and nums[r] points to the right value in nums
            # print(af = nums[Queue[-1]])
            Queue.pop(0)
        Queue.append(r)
        # remove left value from window
        if l > Queue[0]:
            Queue.pop(0)
        if (r + 1) >= k:
            output.append(nums[Queue[0]])
            l += 1
        r += 1
    return output


def main():
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    print(max_sliding_window(nums, k))


if __name__ == "__main__":
    main()
