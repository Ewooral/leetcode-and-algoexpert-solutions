import _heapq as heap
from typing import List

def findkthLargest(nums:List[int], k:int):
    minHeap = []
    for num in nums:
        heap.heappush(minHeap, num)
        if len(minHeap) > k:
            heap.heappop(minHeap)
    return min(minHeap)

print(findkthLargest([3, 2, 1, 5, 6, 4], 2))
print(findkthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))