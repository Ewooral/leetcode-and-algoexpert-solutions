"""
Given two inputs arr, and k sort arr of k value in place and
return the sorted version of the array

E.g Input: [3, 2, 1, 5, 4, 7, 6, 5], k = 3

Output: [1, 2, 3, 4, 5, 5, 6, 7]

"""

import _heapq as heap


# O(n log(k) time | O(k) space
def sort_k_sorted(arr, k):
    sorted_nums_idx = 0
    first_k_elems = arr[:k + 1]
    heap.heapify(first_k_elems)
    for idx in range(k + 1, len(arr)):
        min_num = heap.heappop(first_k_elems)
        arr[sorted_nums_idx] = min_num
        sorted_nums_idx += 1

        curElem = arr[idx]
        heap.heappush(first_k_elems, curElem)
    while not len(first_k_elems) == 0:
        min_num = heap.heappop(first_k_elems)
        arr[sorted_nums_idx] = min_num
        sorted_nums_idx += 1
    return arr


def main():
    Index = [0, 1, 2, 3, 4, 5, 6, 7]
    Input = [3, 2, 1, 5, 4, 7, 6, 5]

    k = 3
    print(sort_k_sorted(Input, k))


if __name__ == '__main__':
    main()

