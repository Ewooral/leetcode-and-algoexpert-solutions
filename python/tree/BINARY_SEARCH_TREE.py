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
    
    except (TypeError, SyntaxError, NameError, AttributeError ) as err:
        print(f"Oops!, {err} \n")


def minValue(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

# O(log N)T, S 
def deleteAny(rootNode, nodeValue):
    if rootNode is None:
        return rootNode
    if nodeValue < rootNode.data:
        rootNode.left = deleteAny(rootNode.left, nodeValue)
    elif nodeValue > rootNode.data:
        rootNode.right = deleteAny(rootNode.right, nodeValue)
    else:
        if rootNode.left is None:
            temp = rootNode.left
            rootNode = None;
            return temp
        if rootNode.right is None:
            temp = rootNode.left
            rootNode = None
            return temp
        temp = minValue(rootNode.right)
        rootNode.data = temp.data
        rootNode.right = deleteAny(rootNode.right, temp.data)
    return rootNode
# O(1) T, S 
def deleteAll(rootNode):
    rootNode.data = None
    rootNode.left = None
    rootNode.right = None

   
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
print(insert(newBST, 40))
print(newBST.data)
print("........preorder........")
preorder(newBST)
print("........inorder........")
inorder(newBST)
print("........postorder........")
postorder(newBST)
print("........levelorder........")
levelorder(newBST)
print("........search......")
search(newBST,  100)
search(newBST,  130)
print(".......delete any node......")
deleteAny(newBST, 70)
levelorder(newBST)
print(".....delete tree....")
deleteAll(newBST)
levelorder(newBST)