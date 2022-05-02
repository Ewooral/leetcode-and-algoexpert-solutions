import queue_linked_list as queue
# # O(1) T, O(1) S
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


# # O(n) T, O(n) S
# def preOrderTraversal(rootNode):
    if not rootNode: #........> O(1)
        return
    print(rootNode.data) # .......> O(1)
    preOrderTraversal(rootNode.leftChild) # ......> o(n/2)
    preOrderTraversal(rootNode.rightChild) # ......> o(n/2)


preOrderTraversal(newBT)
print("..................................")

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
                return "Inserted successfully"
            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)
            else:
                root.value.rightChild = newNode
                return "Inserted successfully"

newNode = TreeNode("Cola")
newNode1 = TreeNode("Apketeshie")
print(insertBT(newBT, newNode))
print(insertBT(newBT, newNode1))
levelOrderTraversal(newBT)
