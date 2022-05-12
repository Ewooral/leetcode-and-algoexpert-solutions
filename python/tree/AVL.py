import queue
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


newAVL = AVL(10)
 