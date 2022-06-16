# find the sum of all subarrays of length k
# list = [1, 2, 3, 4, 5, 6]
from typing import List


def sum_of_subarray(arr: List[int], k: int) -> List[int]:
    '''sum up the first subarray and add it to the result
    cs = current_subarray
    '''
    cs = sum(arr[:k])
    result = [cs]

    '''To get each subsequence subarray, add the next value
    in the list and remove the first value
    '''
    for i in range(1, len(arr) - k + 1 ):
        cs = cs - arr[i - 1]
        cs = cs + arr[i + k - 1]

        result.append(cs)
    return result


print(sum_of_subarray([1, 2, 3, 4, 5, 6], 3))
