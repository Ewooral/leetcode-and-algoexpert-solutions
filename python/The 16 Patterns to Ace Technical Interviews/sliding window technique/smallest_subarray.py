import math


# APPROACH 1
def smallest_subarray_sum(s, arr):
    # win_start = i, win_end = j
    i = _sum = 0
    min_len = math.inf
    for j in range(len(arr)):
        _sum += arr[j]
        while _sum >= s:
            min_len = min(min_len, j - i + 1)
            _sum -= arr[i]
            i += 1
    if min_len == math.inf:
        return 0
    return min_len


def main():
    print("Smallest subarray length: " + str(smallest_subarray_sum(7, [2, 1, 5, 2, 3, 2])))
    print("Smallest subarray length: " + str(smallest_subarray_sum(8, [3, 4, 1, 1, 6])))
    print("Smallest subarray length: " + str(smallest_subarray_sum(8, [2, 1, 5, 2, 3, 2])))


main()
