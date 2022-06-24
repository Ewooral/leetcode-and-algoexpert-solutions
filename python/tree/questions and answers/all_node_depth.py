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
from binarytree import Node

import queue


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
                return "..inserted!..."


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
                return "..inserted!..."


root = Node(1)

insertAtLeft(root, Node(2))
insertAtRight(root, Node(3))

insertAtLeft(root.left, Node(4))
insertAtRight(root.left, Node(5))

insertAtLeft(root.right, Node(6))
insertAtRight(root.right, Node(7))

insertAtLeft(root.left.left, Node(8))
insertAtRight(root.left.left, Node(9))

print(root)






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


def nodeDepths(node, depth=0):
    if node is None:
        return 0
    return depth + nodeDepths(node.left, depth + 1) + nodeDepths(node.right, depth + 1)


# recursively O(nlog(n)) T, O(h)S
# APPROACH TWO O(N) T, O(H) S
def allKindOfNodeDepthsII(rooty):
    if rooty is None:
        return 0
    else:
        return allKindOfNodeDepthsII(rooty.left) + allKindOfNodeDepthsII(rooty.right) + nodeDepths(rooty)


# depths of all nodes relative to each root of the tree
print("...all nodes depths...")
print(allKindOfNodeDepthsI(root))
print("all kinds of nodes depth: ", allKindOfNodeDepthsII(root))
print("node depths: ", nodeDepths(root, depth=0))


# APPROACH TWO O(N) T, O(H) S
def allKindsOfNodeDepthsIV(root):
    return [getTreeInfo(root).sum_of_all_depths, getTreeInfo(root.left)]


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


# depths of all nodes relative to each root of the tree
print("...depths of all nodes relative to each root node...")
print(allKindsOfNodeDepthsIV(root))