"""
Given an array of integers, find combination of integers that will
amount to a target K
"""

from itertools import combinations
from functools import reduce
from operator import add


def Kth_sum(lst, dev, target):
    match_sum = []
    for i in range(1, len(lst)):
        x = list(combinations(lst, i))
        for matches in x:
            tmp = reduce(add, matches)
            if abs(tmp-target) == dev:
                match_sum.append(matches)
                match_sum.sort()
    print(*set(match_sum), sep='\n')


if __name__ == '__main__':
    lst = [9, 4, 2, 13, 14, 22, 11, 7, 12, 8, 81, 9, 6]
    dev = 0
    target = 50
    Kth_sum(lst, dev, target)

