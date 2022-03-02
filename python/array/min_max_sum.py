""" 
Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.

Example

The minimum sum is  and the maximum sum is . The function prints

16 24
Function Description

Complete the miniMaxSum function in the editor below.

miniMaxSum has the following parameter(s):

arr: an array of  integers
Print

Print two space-separated integers on one line: the minimum sum and the maximum sum of  of  elements.

Input Format

A single line of five space-separated integers.

Constraints


Output Format

Print two space-separated long integers denoting the
respective minimum and maximum values that can be
calculated by summing exactly four of the five integers. 
(The output can be greater than a 32 bit integer.)

Sample Input

1 2 3 4 5
Sample Output

10 14
Explanation

The numbers are , , , , and . Calculate the following sums using four of the five integers:

Sum everything except , the sum is .
Sum everything except , the sum is .
Sum everything except , the sum is .
Sum everything except , the sum is .
Sum everything except , the sum is .
"""
import math
import os
import random
import re
import sys
def miniMaxSum(arr):
    # Write your code here
    arr.sort()
    hold = [None]*int(len(arr)-3)
    for i in range(0, len(arr)-3):
        temp = 0
        for j in range(i, i+4):
            temp = temp + arr[j]
        hold[i] = temp

    print(hold[0], hold[-1])


miniMaxSum([1,5,3,4,2])

# This code outputs the min and max values in an array without
#  calculations
def miniMax(array):
    min = array[0]
    for i in array:
        if i < min:
            min = i 
    print(min)
    max = array[0]
    for i in array:
        if i > max:
            max = i 
    print(max) 

miniMax([1,5,3,4,2])