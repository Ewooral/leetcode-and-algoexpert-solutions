import queue as q
class BinaryTree:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


root = BinaryTree("Aps. Nyamekye")
GS = BinaryTree("Aps. K-Larbi")
IMD = BinaryTree("Aps. G.Addo")
Rcc = BinaryTree("Pr. Kankam")
EM = BinaryTree("Aps. Etrue")
root.left = GS
root.right = IMD
root.left.left = Rcc
root.left.right = EM

print(".............Preorder.........")


def preorder(rootNode):
    if rootNode is None:
        return
    print(rootNode.data)
    preorder(rootNode.left)
    preorder(rootNode.right)


preorder(root)

print(".............Inorder.........")


def inorder(rootNode):
    if rootNode is None:
        return
    inorder(rootNode.left)
    print(rootNode.data)
    inorder(rootNode.right)


inorder(root)

print(".............Postorder.........")
def postorder(rootNode):
    if rootNode is None:
        return
    else:
        postorder(rootNode.left)
        postorder(rootNode.right)
        print(rootNode.data)

postorder(root)


print(".............Levelorder.........")

def levelorder(rootNode):
    if rootNode is None:
        return
    else:
        MyQueue = q.Queue();
        MyQueue.put(rootNode)
        while not MyQueue.empty():
            root = MyQueue.get()
            print(root.data)
            if root.left is not None:
                MyQueue.put(root.left)
            if root.right is not None:
                MyQueue.put(root.right)

levelorder(root)
print("............Search...............")
def search(rootNode, nodeValue):
    if rootNode is None:
        return 
    else:
        customQ = q.Queue();
        customQ.put(rootNode);
        while not customQ.empty():
            root = customQ.get()
            if root.data == nodeValue:
                return "Success"
            if root.left is not None:
                customQ.put(root.left)
            if root.right is not None:
                customQ.put(root.right)
        return "Not Found!"

print(search(root, "Aps. Etrue"))

print(".........Insert.........")
def insert(rootNode, newNode):
    if rootNode is None:
        rootNode = newNode
    else:
        customQueue = q.Queue()
        customQueue.put(rootNode);
        while not customQueue.empty():
            root = customQueue.get();
            if root.left is not None:
                customQueue.put(root.left);
            else:
                root.left = newNode
                return 
            if root.right is not None:
                customQueue.put(root.right)
            else:
                root.right = newNode
                return 

# overseer = BinaryTree("Ovr. Prosper")
# overseer1 = BinaryTree("Ovr. Fred")
# insert(root, overseer)
# insert(root, overseer1)
# levelorder(root)

print("..........Deepest Node............")

# O(n)T, S 
def getDeepestNode(rootNode):
    if rootNode is None:
        return
    else:
        cQ = q.Queue()
        cQ.put(rootNode)
        while not cQ.empty():
            root = cQ.get()
            if root.left is not None:
                cQ.put(root.left)
            if root.right is not None:
                cQ.put(root.right)
            
        deepestNode = root.data
        return deepestNode

dp = getDeepestNode(root)
print(dp)

# O(N) T and S
print(".........delete DeepestNode.........")
def deleteDeepestNode(rootNode, dNode):
    if not rootNode:
        return 
    else:
        cQ = q.Queue()
        cQ.put(rootNode)
        while not cQ.empty():
            root = cQ.get()
            if root.data == dNode:
                root.data = " ";
                return
            if root.right is not None:
                if root.right is dNode:
                    root.right = None;
                    return
                else:
                    cQ.put(root.right) 
            if root.left is not None:
                if root.left is dNode:
                    root.left = None;
                    return
                else:
                    cQ.put(root.left) 

# newNode = getDeepestNode(root)
# deleteDeepestNode(root, newNode)
# levelorder(root)

print("............delete any Node...........")
# O(N) T and S
def deleteNode(rootNode, node):
    if rootNode is None:
        return
    else:
        cQ = q.Queue()
        cQ.put(rootNode)
        while not cQ.empty():
            root = cQ.get()
            if root.data == node:
                dNode = getDeepestNode(rootNode)
                deleteDeepestNode(rootNode, dNode)
                root.data = dNode
                return "deleted!!!!!!"
            if root.left is not None:
                cQ.put(root.left)
            if root.right is not None:
                cQ.put(root.right)
        return "Failed to delete"
            

deleteNode(root, "Aps. G.Addo")
levelorder(root)