"""
Given four sorted arrays, merge them into 1-dimensional array without
using the in-built sort function. Also, improve time complexity O(n log n)
Input:
a = [1, 5, 9, 21]
b = [-1, 0]
c = [-124, 81, 121]
d = [3, 6, 12, 20, 150]

Output: [-124, -1, 0, 1, 3, 5, 6, 9, 12, 20, 21, 81, 121, 150]
"""
from typing import List
import heapq as heap


def mergeSortedArr(a: List, b: List, c: List, d: List):
    n_dim = []
    n_dim.extend(a)
    n_dim.extend(b)
    n_dim.extend(c)
    n_dim.extend(d)
    # xidx = 0
    heap.heapify(n_dim)

    return n_dim


def merge_sorted_arr(_list: List):
    nth_dim = []
    _1d_arr = [nth_dim.extend(nth_dim[arr1][:]) for arr1 in range(len(nth_dim))]


def main():
    a = [1, 5, 9, 21]
    b = [-1, 0]
    c = [-124, 81, 121]
    d = [3, 6, 12, 20, 150]
    print(mergeSortedArr(a, b, c, d))


if __name__ == '__main__':
    main()
