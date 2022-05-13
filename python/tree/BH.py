# Binary Heap by Elijah Owusu Boahen
# 13th April, 2022

# O(1) T, O(N) S
class BH:
    def __init__(self, size) -> None:
        self.List = (size + 1) * [None]
        self.heapSize = 0
        self.maxSize = size + 1


# Peek of a BH is the root value
# O(1)T, S
def peek(rootNode):
    if rootNode is None:
        return
    else:
        return rootNode.List[1]

# 
def heapSize(rootNode):
    if not rootNode:
        return
    else:
        return rootNode.heapSize


newBH = BH(5)
print(newBH.List)
print(heapSize(newBH))