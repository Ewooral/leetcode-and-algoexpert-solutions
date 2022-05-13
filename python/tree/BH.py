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

# O(1)T, S
def heapSize(rootNode):
    if not rootNode:
        return
    else:
        return rootNode.heapSize

# Traversal
# O(N)T, O(1)S
def levelorder(rootNode):
    for i in range(1, rootNode.heapSize + 1):
        print(rootNode.List[i])

# O(log N)T, S
def heapifyInsert(rootNode, index, heapType):
    parentIndex = int(index/2)
    if index <= 1:
        return
    if heapType == "Min":
        if rootNode.List[index] < rootNode.List[parentIndex]:
            temp = rootNode.List[index]
            rootNode.List[index] = rootNode.List[parentIndex]
            rootNode.List[parentIndex] = temp
        heapifyInsert(rootNode, parentIndex, heapType)

    elif heapType == "Max":
        if rootNode.List[index] > rootNode.List[parentIndex]:
            temp = rootNode.List[index]
            rootNode.List[index] = rootNode.List[parentIndex]
            rootNode.List[parentIndex] = temp
        heapifyInsert(rootNode, parentIndex, heapType)

def insert(rootNode, nodeValue, heapType):
    if rootNode.heapSize + 1 == rootNode.maxSize:
        return "Binary Heap is full"
    rootNode.List[rootNode.heapSize + 1] = nodeValue
    rootNode.heapSize += 1
    heapifyInsert(rootNode, rootNode.heapSize, heapType)
    return "Inserted Successfully"




newBH = BH(5)
print("...insert...")
insert(newBH, 4, "Max")
insert(newBH, 5, "Max")
insert(newBH, 2, "Max")
insert(newBH, 1, "Max")
levelorder(newBH)
print("....list....")
print(newBH.List)
print("...peek...")
print(peek(newBH))
print("...heap size...")
print(heapSize(newBH))
print("...traversal...")
levelorder(newBH)

