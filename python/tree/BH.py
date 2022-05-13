# Binary Heap by Elijah Owusu Boahen
# 13th April, 2022

# O(1) T, O(N) S
class BH:
    def __init__(self, size) -> None:
        self.List = (size + 1) * [None]
        self.heapSize = 0
        self.maxSize = size


newBH = BH(5)
print(newBH.List)
