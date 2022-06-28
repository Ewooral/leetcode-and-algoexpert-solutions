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
            zigzag = not zigzag
        return result


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
print("zigzag_level_order Traversal: ", zigzag_level_order(root))