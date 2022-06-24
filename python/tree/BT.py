import queue_linked_list as queue
#  O(1) T, O(1) S


class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.leftChild = None
        self.rightChild = None

# instance of the TreeNode class with a value
newBT = TreeNode("Drinks")

LeftChild = TreeNode("Hot")
# hot
tea = TreeNode("tea") 
coffee = TreeNode("coffee")

LeftChild.leftChild = tea
LeftChild.rightChild = coffee

RightChild = TreeNode("Cold")


# cold
# fanta = TreeNode("fanta")
# cola = TreeNode("cola")

# rightChild.leftChild = fanta
# rightChild.rightChild = cola

newBT.leftChild = LeftChild
newBT.rightChild = RightChild

print(".................PreOrder.................")

# # O(n) T, O(n) S
def preOrderTraversal(rootNode):
    if not rootNode: #........> O(1)
        return
    print(rootNode.data) # .......> O(1)
    preOrderTraversal(rootNode.leftChild) # ......> o(n/2)
    preOrderTraversal(rootNode.rightChild) # ......> o(n/2)


preOrderTraversal(newBT)
print("...............InOrder...................")

# # ........> O(n)T, S
def inOrderTraversal(rootNode):
    if not rootNode:  # ........> O(1)
        return
    inOrderTraversal(rootNode.leftChild)  # ........> O(n/2)
    print(rootNode.data)  # ........> O(1)
    inOrderTraversal(rootNode.rightChild)  # ........> O(n/2)

inOrderTraversal(newBT)
print("...............postOrder...................")
 
# # ........> O(n)T, S
def postOrderTraversal(rootNode): 
    if not rootNode:  # ........> O(1)
        return
    postOrderTraversal(rootNode.leftChild)  # ........> O(n/2)
    postOrderTraversal(rootNode.rightChild)  # ........> O(n/2)
    print(rootNode.data)  # ........> O(1)

postOrderTraversal(newBT)
print("..............levelOrder....................")

def levelOrderTraversal(rootNode): # O(n)T, O(n)S
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not customQueue.isEmpty():
            root = customQueue.dequeue()
            print(root.value.data)
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)
            
            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)
    
levelOrderTraversal(newBT)

print("...............Search...................")
def searchBT(rootNode, nodeValue): # O(n)T and S
    if not rootNode:
        return "The BT does not exit"
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue();
            if root.value.data == nodeValue:
                return "Found!"
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)
            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)
        return "Not found"
print(searchBT(newBT, "tea"))
print(".................insert.......................")

# O(n)T, S
def insertBT(rootNode, newNode): 
    if not rootNode:
        rootNode = newNode
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue();
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)
            else:
                root.value.leftChild = newNode
                return 
            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)
            else:
                root.value.rightChild = newNode
                return 

newNode = TreeNode("Cola")
newNode1 = TreeNode("Tekela")
insertBT(newBT, newNode)
insertBT(newBT, newNode1)
levelOrderTraversal(newBT)


print(".........Get Deepest Node...........")
# # O(n)T, S
def getDeepestNode(rootNode):
    if rootNode is None:
        return
    else:
        customQ = queue.Queue();
        customQ.enqueue(rootNode);
        while not customQ.isEmpty():
            root = customQ.dequeue();
            if root.value.leftChild is not None:
                customQ.enqueue(root.value.leftChild)
            if root.value.rightChild is not None:
                customQ.enqueue(root.value.rightChild)
        
        DeepestNode = root.value
        return DeepestNode

deepestNode = getDeepestNode(newBT)
print(deepestNode.data)

print("..........delete deepest node.....................")
def deleteDeepestNode(rootNode, dNode):
    if rootNode is None:
        return
    else:
        customQ = queue.Queue()
        customQ.enqueue(rootNode)
        while not customQ.isEmpty():
            root = customQ.dequeue()
            if root.value is dNode:
                root.value = None;
                return 
            if root.value.rightChild is not None:
                if root.value.rightChild is dNode:
                    root.value.rightChild = None;
                    return
                else:
                    customQ.enqueue(root.value.rightChild)

            if root.value.leftChild is not None:
                if root.value.leftChild is dNode:
                    root.value.leftChild = None;
                    return
                else:
                    customQ.enqueue(root.value.leftChild)

deleteDeepestNode(newBT, getDeepestNode(newBT))
levelOrderTraversal(newBT)

print("..............delete any node....................")

def deleteAnyNode(rootNode, node):
    if rootNode is None:
        return
    else:
        customQ = queue.Queue()
        customQ.enqueue(rootNode)
        while not customQ.isEmpty():
            root = customQ.dequeue()
            if root.value.data is node:
                dNode = getDeepestNode(rootNode)
                root.value.data = dNode.data
                deleteDeepestNode(rootNode, dNode)
                return 
            if root.value.leftChild is not None:
                customQ.enqueue(root.value.leftChild)
                 
            if root.value.rightChild is not None:
                customQ.enqueue(root.value.rightChild)
                 
        print("Failed to delete node")


deleteAnyNode(newBT, "Drinks")
deleteAnyNode(newBT, "Hot")
levelOrderTraversal(newBT)


# O(1) T, S
print("........delete Binary Tree........")
def deleteTree(rootNode):
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    return "suceessfully deleted!"

deleteTree(newBT)
levelOrderTraversal(newBT)




