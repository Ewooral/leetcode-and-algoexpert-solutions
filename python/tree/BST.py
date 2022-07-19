import math
import queue


# O(1) T and S
class BST:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# O(log N) T, S
def insert(rootNode, value):
    if rootNode.data is None:
        rootNode.data = value
    elif value <= rootNode.data:
        if rootNode.left is None:
            rootNode.left = BST(value)
        else:
            insert(rootNode.left, value)
    else:
        if rootNode.right is None:
            rootNode.right = BST(value)
        else:
            insert(rootNode.right, value)
    return "..........Inserted!........"


# Iterative
# Average: O(log n) T | O(1)S
# Worse: O(n) T | O(1) S
def insertI(rootNode, value):
    while rootNode:
        if value < rootNode.value:
            if rootNode.left is None:
                rootNode.left = BST(value)
                return
            else:
                rootNode = rootNode.left
        else:
            if rootNode.right is None:
                rootNode.right = BST(value)
                return
            else:
                rootNode = rootNode.right


# O(N)T, S
def preorder(rootNode):
    if rootNode is None:
        return
    print(rootNode.data)
    preorder(rootNode.left)
    preorder(rootNode.right)


# O(N)T, S


def inorder(rootNode):
    if rootNode is None:
        return
    inorder(rootNode.left)
    print(rootNode.data)
    inorder(rootNode.right)


# O(N)T, S
def postorder(rootNode):
    if rootNode is None:
        return
    postorder(rootNode.left)
    postorder(rootNode.right)
    print(rootNode.data)


# O(N)T, S
def levelorder(rootNode):
    try:
        if rootNode is None:
            return
        else:
            cq = queue.Queue()
            cq.queue.appendleft(rootNode)
            while not cq.empty():
                root = cq.get()
                print(root.data)
                if root.left is not None:
                    cq.put(root.left)
                if root.right is not None:
                    cq.put(root.right)
    except (TypeError, SyntaxError, NameError, AttributeError) as err:
        print(f"Oops!, {err} \n")


# O(log N)T, S
def search(rootNode, nodeValue):
    try:
        if rootNode.data == nodeValue:
            print("Found")
        elif nodeValue <= rootNode.data:
            if rootNode.left == nodeValue:
                print("Found")
            else:
                search(rootNode.left, nodeValue)
        else:
            if rootNode.right == nodeValue:
                print("Found")
            else:
                search(rootNode.right, nodeValue)
    except (TypeError, SyntaxError, NameError, AttributeError) as err:
        print(f"Oops!, {err} \n")


# Iterative
# Average: O(log n) T | O(1)S
# Worse: O(n) T | O(1) S
def searchI(currentNode, value):
    rootNode = currentNode
    while rootNode is not None:
        if value < rootNode.data:
            rootNode = rootNode.left
        elif value > rootNode.data:
            rootNode = rootNode.right
        else:
            return True


def minValue(node):
    current = node
    while current.left is not None:
        current = current.left
    return current


# O(log N)T, S 
def deleteAny(rootNode, nodeValue):
    if rootNode is None:
        return rootNode
    # if you're deleting a leaf node
    if nodeValue < rootNode.data:
        rootNode.left = deleteAny(rootNode.left, nodeValue)
    elif nodeValue > rootNode.data:
        rootNode.right = deleteAny(rootNode.right, nodeValue)
    else:
        # if rootNode has only one child
        if rootNode.left is None:
            temp = rootNode.right
            rootNode.right = None
            return temp
        if rootNode.right is None:
            temp = rootNode.left
            rootNode.left = None
            return temp
        # if rootNode has two children
        temp = minValue(rootNode.right)
        rootNode.data = temp.data
        rootNode.right = deleteAny(rootNode.right, temp.data)
    return rootNode


# O(1) T, S 
def deleteAll(rootNode):
    rootNode.data = None
    rootNode.left = None
    rootNode.right = None


# FIND THE CLOSEST VALUE TO TARGET IN BST
# find_closest_value_in_BST_Helper = fCVHelper
# find_closest_value_in_BST = fCV
def fCV(rootNode, target):
    return fCVHelper(rootNode, target, math.inf)


def fCVHelper(rootNode, target, closest):
    currentNode = rootNode
    while currentNode is not None:
        if abs(target - closest) > abs(target - currentNode.data):
            closest = currentNode.data
        if target < currentNode.data:
            currentNode = currentNode.left
        elif target > currentNode.data:
            currentNode = currentNode.right
        else:
            break
    return closest


def kth_largest_value_BST(rootNode, k):
    result = in_order(rootNode)
    return result[len(result) - k]


def in_order(_root, result=None):
    if result is None:
        result = []
    if _root is None:
        return
    in_order(_root.left, result)
    result.append(_root.data)
    in_order(_root.right, result)
    return result


newBST = BST(None)
print("........insert........")
print(insert(newBST, 70))
print(insert(newBST, 50))
print(insert(newBST, 90))
print(insert(newBST, 30))
print(insert(newBST, 60))
print(insert(newBST, 80))
print(insert(newBST, 100))
print(insert(newBST, 20))
print(insert(newBST, 40))
print(insert(newBST, 20))
print(newBST.data)

print("......closest value to target 96...")
print(fCV(newBST, 96))
print("........preorder........")
preorder(newBST)
print("........inorder........")
inorder(newBST)
print("........postorder........")
postorder(newBST)
print("........level order........")
levelorder(newBST)

print("Kth Largest value in BST:......")
print(kth_largest_value_BST(newBST, k=3))
print(in_order(newBST))
print("........search......")
search(newBST, 100)
search(newBST, 130)
print(searchI(newBST, 400))
print(".......delete any node......")
deleteAny(newBST, 100)
levelorder(newBST)
print(".....delete tree....")
deleteAll(newBST)
levelorder(newBST)
