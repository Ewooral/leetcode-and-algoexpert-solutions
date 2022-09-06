"""
1051. Height Checker
Easy

A school is trying to take an annual photo of all the students. The students are asked to stand in a
single file line in non-decreasing order by height. Let this ordering be represented by the integer array
expected where expected[i] is the expected height of the ith student in line.

You are given an integer array heights representing the current order that the students are standing in.
Each heights[i] is the height of the ith student in line (0-indexed).

Return the number of indices where heights[i] != expected[i].



Example 1:

Input: heights = [1,1,4,2,1,3]
Output: 3
Explanation:
heights:  [1,1,4,2,1,3]
expected: [1,1,1,2,3,4]
Indices 2, 4, and 5 do not match.
Example 2:

Input: heights = [5,1,2,3,4]
Output: 5
Explanation:
heights:  [5,1,2,3,4]
expected: [1,2,3,4,5]
All indices do not match.
Example 3:

Input: heights = [1,2,3,4,5]
Output: 0
Explanation:
heights:  [1,2,3,4,5]
expected: [1,2,3,4,5]
All indices match.
"""

import heapq as heap


def height_checker(heights):
    expected = sorted(heights)
    # i = j = count = 0
    # while i < len(heights) and j < len(expected):
    #     h = heights[i]
    #     e = expected[j]
    #     if h != e:
    #         count += 1
    #     i += 1
    #     j += 1
    #     OR
    count = 0
    for i in range(len(heights)):
        h = heights[i]
        e = expected[i]
        if h != e:
            count += 1

    return count


print(height_checker([1, 1, 4, 2, 1, 3]))
