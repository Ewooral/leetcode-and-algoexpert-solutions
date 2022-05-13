import queue
from bt_module import Node


class AVL:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1


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
        elif nodeValue < rootNode.data:
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


def getHeight(rootNode):
    if rootNode is None:
        return 0
    return rootNode.height


# O(1) T, S
def rightRotate(imbalancedNode):
    new_root = imbalancedNode.left
    imbalancedNode.left = imbalancedNode.left.right
    new_root.right = imbalancedNode
    imbalancedNode.height = 1 + max(getHeight(imbalancedNode.left), getHeight(imbalancedNode.right))
    new_root.height = 1 + max(getHeight(new_root.left), getHeight(new_root.right))
    return new_root


# O(1) T, S
def leftRotate(imbalancedNode):
    new_root = imbalancedNode.right
    imbalancedNode.right = imbalancedNode.right.left
    new_root.left = imbalancedNode
    imbalancedNode.height = 1 + max(getHeight(imbalancedNode.left), getHeight(imbalancedNode.right))
    new_root.height = 1 + max(getHeight(new_root.left), getHeight(new_root.right))
    return new_root


# O(1) T, S
def get_balance(rootNode):
    if not rootNode:
        return 0
    return getHeight(rootNode.left) - getHeight(rootNode.right)


# O(log N) T, S
def insert(rootNode, nodeValue):
    if rootNode is None:
        return AVL(nodeValue)
    elif nodeValue < rootNode.data:
        rootNode.left = insert(rootNode.left, nodeValue)
    else:
        rootNode.right = insert(rootNode.right, nodeValue)

    rootNode.height = 1 + max(getHeight(rootNode.left), getHeight(rootNode.right))
    balance = get_balance(rootNode)
    if balance > 1 and nodeValue < rootNode.left.data:
        return rightRotate(rootNode)
    if balance > 1 and nodeValue > rootNode.left.data:
        rootNode.left = leftRotate(rootNode.left)
        return rightRotate(rootNode)
    if balance < -1 and nodeValue > rootNode.right.data:
        return leftRotate(rootNode)
    if balance < -1 and nodeValue < rootNode.right.data:
        rootNode.right = rightRotate(rootNode.right)
        return leftRotate(rootNode)
    return rootNode


def getMinimumValue(rootNode):
    if rootNode is None or rootNode.left is None:
        return rootNode
    return getMinimumValue(rootNode.left)


# O(log N) T, S
def delete(rootNode, nodeValue):
    # 1st case: if rootNode is None
    if not rootNode:
        return rootNode
    elif nodeValue < rootNode.data:
        rootNode.left = delete(rootNode.left, nodeValue)
    elif nodeValue > rootNode.data:
        rootNode.right = delete(rootNode.right, nodeValue)
    else:
        # 2nd case: if rotation is not required
        if rootNode.left is None:
            temp = rootNode.right
            rootNode = None
            return temp
        if rootNode.right is None:
            temp = rootNode.left
            rootNode = None
            return temp
        temp = getMinimumValue(rootNode.right)
        rootNode.data = temp.data
        rootNode.right = delete(rootNode.right, temp.data)

        # 3rd case: if rotation is required
        balance = get_balance(rootNode)
        if balance > 1 and get_balance(rootNode.left) >= 0:
            return rightRotate(rootNode)
        if balance < -1 and get_balance(rootNode.right) <= 0:
            return leftRotate(rootNode)
        if balance > 1 and get_balance(rootNode.left) < 0:
            rootNode.left = leftRotate(rootNode.left)
            return rightRotate(rootNode)
        if balance < -1 and get_balance(rootNode.right) > 0:
            rootNode.right = rightRotate(rootNode.right)
            return leftRotate(rootNode)
    return rootNode


# O(1) T, S
def deleteTree(rootNode):
    rootNode.data = None
    rootNode.left = None
    rootNode.right = None


newAVL = AVL(5)
newAVL = insert(newAVL, 10)
newAVL = insert(newAVL, 15)
newAVL = insert(newAVL, 20)

print("....preorder....")
preorder(newAVL)

print("....inorder....")
inorder(newAVL)

print("....postorder....")
postorder(newAVL)

print("...level order....")
levelorder(newAVL)
print("....search....")
search(newAVL, 30)
print("....get height....")
print(getHeight(newAVL))
print(".....delete a node......")
newAVL = delete(newAVL, 15)
levelorder(newAVL)
print(".....delete AVL tree.....")
deleteTree(newAVL)
levelorder(newAVL)