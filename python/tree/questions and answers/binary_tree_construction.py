from dataclasses import dataclass
from collections import deque as que
from binarytree import Node
import queue


@dataclass
class BinaryTree:
    value: int = None
    left: int = None
    right: int = None


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
                return "...Inserted!..."


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
                return "...Inserted!..."


print("...Insert Nodes...")
root = Node(1)

insertAtLeft(root, Node(2))
insertAtRight(root, Node(3))

insertAtLeft(root.left, Node(4))
insertAtRight(root.left, Node(5))

insertAtLeft(root.right, Node(6))
insertAtRight(root.right, Node(7))

insertAtLeft(root.left.left, Node(8))
insertAtRight(root.left.left, Node(9))

print("This is a binary search tree, True/False?: ", root.is_bst)


def level_order(rootNode):
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


def search(rootNode, value):
    if rootNode is None:
        return
    else:
        q = queue.Queue()
        q.put(rootNode)
        while not q.empty():
            root = q.get()
            if root.value == value:
                return f"Found {value}"
            if root.left is not None:
                q.put(root.left)
            if root.right is not None:
                q.put(root.right)
        return "Not Found!"


print("...search...")
print(search(root, 10))

print(root)
level_order(root)


# TWO APPROACHES TO FIND ALL NODE DEPTH
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
        return allKindOfNodeDepthsII(rooty.left) + allKindOfNodeDepthsII(rooty.right) + nodeDepthsI(rooty)


def nodeDepthsI(node, depth=0):
    print("node", "(", node, ")")
    if node is None:
        return 0
    return depth + nodeDepths(node.left, depth + 1) + nodeDepths(node.right, depth + 1)


# depths of all nodes relative to each root of the tree
print("...all nodes depths...")
print(allKindOfNodeDepthsI(root))
print("nodes depths: ", nodeDepths(root, depth=0))


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


def zigzag_level_order(root):
    if root is None:
        return []
    else:
        result = []
        zigzag = False
        q = que()
        q.append(root)
        while q:
            level = []
            for _ in range(len(q)):
                if zigzag:
                    node = q.pop()
                    level.append(node)
                    if node.right:
                        q.appendleft(node.right)
                    if node.left:
                        q.appendleft(node.left)
                else:
                    node = q.popleft()
                    level.append(node.value)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            result.append(level)
            zigzag = not zigzag
        return result

@dataclass
class TreeInfo:
    num_nodes_in_tree: int = 0
    sum_of_depths: int = 0
    sum_of_all_depths: int = 0


# depths of all nodes relative to each root of the tree
print("...depths of all nodes relative to each root node...")
print(allKindsOfNodeDepthsIV(root))
print(allKindOfNodeDepthsII(root))
