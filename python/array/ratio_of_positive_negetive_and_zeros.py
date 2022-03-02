
"""
Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the decimal value of each fraction on a new line with  places after the decimal.

Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers with absolute error of up to  are acceptable.

Example

There are  elements, two positive, two negative and one zero. Their ratios are 2/5 = 0.400000, 2/5 = 0.400000, and 1/5 = 0.200000 Results are printed as:

0.400000
0.400000
0.200000
Function Description

Complete the plusMinus function in the editor below.

plusMinus has the following parameter(s):

int arr[n]: an array of integers
Print
Print the ratios of positive, negative and zero values in the array. Each value should be printed on a separate line with  digits after the decimal. The function should not return a value.

Input Format

The first line contains an integer, , the size of the array.
The second line contains  space-separated integers that describe .

Constraints
0 < n < n <= 100
-100 <= arr[i] <= 100



Output Format

Print the following  lines, each to  decimals:

proportion of positive values
proportion of negative values
proportion of zeros
Sample Input

STDIN           Function
-----           --------
6               arr[] size n = 6
-4 3 -9 0 4 1   arr = [-4, 3, -9, 0, 4, 1]
Sample Output

0.500000
0.333333
0.166667
Explanation

There are 3 positive numbers, 2 negative numbers, and 1 zero in the array.
The proportions of occurrence are positive: 3/6 = 0.500000 , 
negative: 2/6 = 0.333333, and zeros: 1/6 = 1.66667  .
"""

# O(n) T complexity
# O(1) time
def plusMinus(arr, N):
    # Write your code here
    positive_count = 0
    negetive_count = 0
    zero_count = 0
    N = len(arr)
    for i in range(N):
        if arr[i] < 0 and arr[i] > -101:
            negetive_count += 1
        if arr[i] == 0:
            zero_count += 1
        if arr[i] > 0 and arr[i] < 101:
            positive_count += 1

    print(format(positive_count / N, ".6f"))
    print(format(negetive_count / N,  ".6f"))
    print(format(zero_count / N,  ".6f"))

    print("..................................")
    print("positive count: ", positive_count)
    print("negetive count: ", negetive_count)
    print("zero count: ", zero_count)


plusMinus([-4, 3, -9, 0, 4, 1], 101)





# arrays = [i for i in range(-100, 101)]
# plusMinus(arrays, 100)

# N = int(input())
# listahan = input().split()
# diks = {"pos": 0, "neg": 0, "zer": 0}
# for i in listahan:
#     if int(i) > 0:
#         diks["pos"] += 1
#     elif int(i) < 0:
#         diks["neg"] += 1
#     else:
#         diks["zer"] += 1
# print(format(diks["pos"]/N, '.3f'))
# print(format(diks["neg"]/N, '.3f'))
# print(format(diks["zer"]/N, '.3f'))
