import queue
from binarytree import Node

node = Node(1)

level_2_left = Node(2)
level_2_right = Node(3)
node.left = level_2_left
node.right = level_2_right

level_3_leftA = Node(4)
level_3_leftB = Node(5)
node.left.left = level_3_leftA
node.left.right = level_3_leftB

level_3_rightA = Node(6)
level_3_rightB = Node(7)
node.right.left = level_3_rightA
node.right.right = level_3_rightB




def insertAtLeft(root, node):
    if root is None:
        return
    else:
        q = queue.Queue()
        q.put(root)
        while not q.empty():
            rooty = q.get()
            if rooty.left is not None:
                q.put(rooty.left)
            else:
                rooty.left = node


def insertAtRight(root, node):
    if root is None:
        return
    else:
        q = queue.Queue()
        q.put(root)
        while not q.empty():
            rooty = q.get()
            if rooty.right is not None:
                q.put(rooty.right)
            else:
                rooty.right = node

insertAtLeft(node.left, Node(8))
insertAtRight(node.left.left, Node(9))
def printLeftTree(root):
    if root is None:
        return
    else:
        q = queue.Queue()
        q.put(root)
        while not q.empty():
            rooty = q.get()
            if rooty.left is not None:
                print(rooty.left)

                
def printRightTree(root):
    if root is None:
        return
    else:
        q = queue.Queue()
        q.put(root)
        while not q.empty():
            rooty = q.get()
            if rooty.right is not None:
                print(rooty.right)

                


            
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






print(node)
print(node.is_balanced)
print(node)
print(node.leaf_count)
print(node.height)
print(allKindOfNodeDepthsI(node))

print("...Left sub tree...")
printLeftTree(node)
print("...right sub tree...")
printRightTree(node)

