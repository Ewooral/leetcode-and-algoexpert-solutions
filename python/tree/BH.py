# Binary Heap by Elijah Owusu Boahen
# 13th April, 2022

import heapq
# O(1) T, O(N) S
class BH:
    def __init__(self, size) -> None:
        self.List = (size + 1) * [None] # fix size list
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
    try:
        for i in range(1, rootNode.heapSize + 1):
            print(rootNode.List[i])
        
    except (ValueError, RuntimeError, TypeError, NameError, SyntaxError) as err:
        print(f"Oops!... traversing failed. List is empty")


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


# O(log N)T, S
def insert(rootNode, nodeValue, heapType):
    if rootNode.heapSize + 1 == rootNode.maxSize:
        return "Binary Heap is full"
    rootNode.List[rootNode.heapSize + 1] = nodeValue
    rootNode.heapSize += 1
    heapifyInsert(rootNode, rootNode.heapSize, heapType)
    return "Inserted Successfully"


# O(log N)T, S
def heapifyExtract(rootNode, index, heapType):
    leftIndex = index * 2
    rightIndex = index * 2 + 1
    swapChild = 0
    if rootNode.heapSize < leftIndex:
        return
    elif rootNode.heapSize == leftIndex:
        if heapType == "Min":
            if rootNode.List[index] > rootNode.List[leftIndex]:
                temp = rootNode.List[index]
                rootNode.List[index] = rootNode.List[leftIndex]
                rootNode.List[leftIndex] = temp
            return 
        else:
            if rootNode.List[index] < rootNode.List[leftIndex]:
                temp = rootNode.List[index]
                rootNode.List[index] = rootNode.List[leftIndex]
                rootNode.List[leftIndex] = temp
            return 
    else:
        if heapType == "Min":
            if rootNode.List[leftIndex] < rootNode.List[rightIndex]:
                swapChild = leftIndex
            else:
                swapChild = rightIndex
            if rootNode.List[index] > rootNode.List[swapChild]:
                temp = rootNode.List[index]
                rootNode.List[index] = rootNode.List[leftIndex]
                rootNode.List[leftIndex] = temp
        else:
            if rootNode.List[leftIndex] > rootNode.List[rightIndex]:
                swapChild = leftIndex
            else:
                swapChild = rightIndex
            if rootNode.List[index] < rootNode.List[swapChild]:
                temp = rootNode.List[index]
                rootNode.List[index] = rootNode.List[leftIndex]
                rootNode.List[leftIndex] = temp
    heapifyExtract(rootNode, swapChild, heapSize)


# The only element allowed to be extracted from a heap is the root Node
# O(log N)T, S
def extract(rootNode, heapType):
    if rootNode.heapSize == 0:
        return 
    else:
        extractedNode = rootNode.List[1]
        rootNode.List[1] = rootNode.List[rootNode.heapSize]
        rootNode.List[rootNode.heapSize] = None
        rootNode.heapSize -= 1
        heapifyExtract(rootNode, 1, heapType)
        return extractedNode


# O(1)T, S 
def deleteHeap(rootNode):
    rootNode.List = None
    return "Binary Heap Tree has been Deleted"


newBH = BH(5)
print("...insert...")
insert(newBH, 4, "Max")
insert(newBH, 5, "Max")
insert(newBH, 2, "Max")
insert(newBH, 1, "Max")
levelorder(newBH)
print("...extract Node...")
extract(newBH, "Max")
levelorder(newBH)
print("....list....")
print(newBH.List)
print("...peek...")
print(peek(newBH))
print("...heap size...")
print(heapSize(newBH))
print("...traversal...")
levelorder(newBH)
print(".....delete binary heap tree...")
deleteHeap(newBH)
levelorder(newBH)
