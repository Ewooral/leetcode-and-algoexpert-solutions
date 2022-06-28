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

root = Node(1)

insertAtLeft(root, Node(2))
insertAtRight(root, Node(3))

insertAtLeft(root.left, Node(4))
insertAtRight(root.left, Node(5))

insertAtLeft(root.right, Node(6))
insertAtRight(root.right, Node(7))

insertAtLeft(root.left.left, Node(8))
insertAtRight(root.left.left, Node(9))

insertAtRight(root.left.right, Node(10))

# print(root)


def branch_sums(root):
    sums = []
    calculate_branch_sums(root, 0, sums)
    return sums


def calculate_branch_sums(node, runningSum, sums):
    if node is None:
        return
    newRunningSum = runningSum + node.value
    if node.left is None and node.right is None:
        sums.append(newRunningSum)
        return
    calculate_branch_sums(node.left, newRunningSum, sums)
    calculate_branch_sums(node.right, newRunningSum, sums)
    return newRunningSum


print(branch_sums(root))


