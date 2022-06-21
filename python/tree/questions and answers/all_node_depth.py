'''
Notes
There's an additional, cleaner and more clever way of solving this 
question with the same time and space time complexities as the 
optimal solution covered in the video explanation.

Realize that a given node in the input tree has:

a depth of 1 with respect to its parent node
a depth of 2 with respect to its parent's parent node
a depth of 3 with respect to its parent's parent's node
...
a depth of d with respect to the root node
Since these depths are captured in each subtree's nodes' depths, which we sum up to get the final answer, we can deduce that each node in the input tree contributes 1 + 2 + 3 + ... + d - 1 + d to the final answer.

Thus, we can solve this question with a simple recursive function that takes in the running depthSum and adds the current node's depth to it at every call. See Solution 5 for the implementation of this algorithm.

We can go one step further by realizing that the sum 1 + 2 + 3 + ... + n - 1 + n can be calculated with the formula (n * (n + 1)) / 2, which eliminates the need to pass the running depthSum to each recursive function call. See Solution 6 for this implementation.

Note that these two extra solutions are very clever and wouldn't be expected of you in an interview (especially Solution 6, which takes advantage of a math formula). That being said, if you were able to come up with either of these two solutions, that certainly wouldn't be bad!
'''
from dataclasses import dataclass
from typing import Tuple, List, Optional

import queue


@dataclass
class BinaryTree:
    value: int = None
    left: int = None
    right: int = None

    

bt = BinaryTree(1)

left1 = BinaryTree(2)
right1 = BinaryTree(3)

bt.left = left1
bt.right = right1

# children of the left subtree from the root
lL = BinaryTree(4)
lR = BinaryTree(5)
# children of the right subtree from the root
rL = BinaryTree(6)
rR = BinaryTree(7)

left1.left = lL
left1.right = lR

right1.left = rL
right1.right = rR


def preorderTraversal(root):
    if root is None:
        return
    print(root.value)
    preorderTraversal(root.left)
    preorderTraversal(root.right)


print("pre order")
preorderTraversal(bt)


def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.value)
    inorder(root.right)


print("in order")
inorder(bt)


def postorder(root):
    if root is None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.value)


print("post order")
postorder(bt)


def levelorder(rootNode):
    if rootNode is None:
        return
    else:
        q = queue.Queue()
        q.put(rootNode)
        while not q.empty():
            root = q.get()
            print(root.value)
            if root.left is not None:
                q.put(root.left)
            if root.right is not None:
                q.put(root.right)

print("level order")
levelorder(bt)


def insertAtLeft(rootNode, nodeValue):
    if rootNode is None:
        rootNode = nodeValue
    else:
        q = queue.Queue()
        q.put(rootNode)
        while not q.empty():
            root = q.get()
            if root.left is not None:
                q.put(root.left)
            else:
                root.left = nodeValue
                return "inserted!"
            # if root.right is not None:
            #     q.put(root.right)
            # else:
            #     root.right = nodeValue
            #     return "inserted!"


def insertAtRight(rootNode, nodeValue):
    if rootNode is None:
        rootNode = nodeValue
    else:
        q = queue.Queue()
        q.put(rootNode)
        while not q.empty():
            root = q.get()
            if root.right is not None:
                q.put(root.right)
            else:
                root.right = nodeValue
                return


print("insert at left")
level3 = BinaryTree(8)
insertAtLeft(bt, level3)

print("insert at right")
level3_r = BinaryTree(9)

print("level order")
levelorder(bt)




# APPROACH ONE
# iteratively
def allKindOfNodeDepthsI(root):
    sumOfAllDepths = 0
    stack = [root]
    while len(stack) > 0:
        node = stack.pop()
        if node is None:
            continue
        sumOfAllDepths += nodeDepths(node)
        stack.append(node.left)
        stack.append(node.right)
    return sumOfAllDepths


# recursively O(nlog(n)) T, O(h)S
def allKindOfNodeDepthsII(root):
    if root is None:
        return allKindOfNodeDepthsII(root.left) + allKindOfNodeDepthsII(root.right) + nodeDepths(root)


def nodeDepths(node, depth=0):
    if node is None:
        return 0
    return depth + nodeDepths(node.left, depth + 1) + nodeDepths(node.right, depth + 1)


# APPROACH TWO
# O(N) T, O(N)S
def allKindsOfNodeDepthsIII(root):
    nodeCounts = {}
    addNodeCounts(root, nodeCounts)
    nodeDepthsA = {}
    addNodeDepths(root, nodeDepthsA, nodeCounts)
    return sumAllNodeDepths(root, nodeDepthsA)


def sumAllNodeDepths(node, nodeDepthsA):
    if node is None:
        return 0
    return sumAllNodeDepths(node.left, nodeDepthsA) + sumAllNodeDepths(node.right, nodeDepthsA) + nodeDepthsA[node]


def addNodeDepths(node, nodeDepthsA, nodeCounts):
    nodeCounts[node] = 0
    if node.left is not None:
        addNodeDepths(node.left, nodeDepthsA, nodeCounts)
        nodeDepthsA[node] += nodeDepthsA[node.left] + nodeCounts[node.left]
    if node.right is not None:
        addNodeDepths(node.right, nodeDepthsA, nodeCounts)
        nodeDepthsA[node] += nodeDepthsA[node.right] + nodeCounts[node.right]


def addNodeCounts(node, nodeCounts):
    nodeCounts[node] = 1
    if node.left is not None:
        addNodeCounts(node.left, nodeCounts)
        nodeCounts[node] += nodeCounts[node.left]
    if node.right is not None:
        addNodeCounts(node.right, nodeCounts)
        nodeCounts[node] += nodeCounts[node.right]


# APPROACH THREE O(N) T, O(H) S
def allKindsOfNodeDepthsIV(root):
    return getTreeInfo(root).sum_of_all_depths


def getTreeInfo(tree):
    if tree is None:
        return TreeInfo()
    leftTreeInfo = getTreeInfo(tree.left)
    rightTreeInfo = getTreeInfo(tree.right)

    sumOfLeftDepths = leftTreeInfo.sum_of_depths + leftTreeInfo.num_nodes_in_tree
    sumOfRightDepths = rightTreeInfo.sum_of_depths + rightTreeInfo.num_nodes_in_tree

    numNodesInTree = 1 + leftTreeInfo.num_nodes_in_tree + rightTreeInfo.num_nodes_in_tree
    sumOfDepths = sumOfLeftDepths + sumOfRightDepths
    sumOfAllDepths = sumOfDepths + leftTreeInfo.sum_of_all_depths + rightTreeInfo.sum_of_all_depths
    return TreeInfo(numNodesInTree, sumOfDepths, sumOfAllDepths)


@dataclass
class TreeInfo:
    num_nodes_in_tree: int = 0
    sum_of_depths: int = 0
    sum_of_all_depths: int = 0
