from collections import deque as que
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


def invert_binarytree(root):
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
                    level.append(node.value)
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
            zigzag = True
        return result

# O(N)T, S
def invertBT(tree):
    queue = [tree]
    result = []
    while len(queue):
        level = []
        current = queue.pop(0)
        level.append(current)
        if current is None:
            continue
        swapLeftAndRight(current)
        queue.append(current.left)
        queue.append(current.right)
        result.append(level)
    return result


def invertBT2(tree):
    if tree is None:
        return
    swapLeftAndRight(tree)
    invertBT2(tree.left)
    invertBT2(tree.right)


def swapLeftAndRight(tree):
    tree.left, tree.right = tree.right, tree.left


print("...................................................................")
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

print(root)
print("invert tree approach 1: ", invert_binarytree(root))
print("invert tree Approach 2: ", invertBT(root))
