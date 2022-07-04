"""
Given an array of positive integers and a number ‘S,’ find the length of
the smallest contiguous subarray whose sum is greater than or equal to ‘S’. Return 0 if no such subarray exists.

Example 1:

    Input: [2, 1, 5, 2, 3, 2], S=7
    Output: 2
    Explanation: The smallest subarray with a sum greater than or equal to ‘7’ is [5, 2].
"""
import math


def smallest_subarray_sum(arr, s):
    win_start = win_sum = 0
    min_len = math.inf
    for win_end in range(len(arr)):
        win_sum += arr[win_end]
        while win_sum >= s:
            min_len = min(min_len, win_end - win_start + 1)
            win_sum -= arr[win_start]
            win_start += 1
    if min_len == math.inf:
        return 0
    return min_len


def main():
    Input = [2, 1, 5, 2, 3, 2]
    S = 7
    print(smallest_subarray_sum(Input, S))


if __name__ == '__main__':
    main()


