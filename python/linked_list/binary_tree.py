# # O(1) T, O(1) S
class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.leftChild = None
        self.rightChild = None

newBT = TreeNode("Drinks") # instance of the TreeNode class with a value

leftChild = TreeNode("Hot")
rightChild = TreeNode("Cold")

# # hot 
tea = TreeNode("tea")
coffee = TreeNode("coffee")

# # cold
fanta = TreeNode("fanta")
cola = TreeNode("cola")

leftChild.leftChild = tea
# leftChild.rightChild = coffee

# # rightChild.leftChild = fanta
# # rightChild.rightChild = cola

# newBT.leftChild = leftChild
# newBT.rightChild = rightChild

# # O(n) T, O(n) S
# def preOrderTraversal(rootNode):
#     if not rootNode: #........> O(1)
#         return
#     print(rootNode.data) # .......> O(1)
#     preOrderTraversal(rootNode.leftChild) # ......> o(n/2)
#     preOrderTraversal(rootNode.rightChild) # ......> o(n/2)


# preOrderTraversal(newBT)
# print("..................................")

# # ........> O(n)T, S
# def inOrderTraversal(rootNode):
#     if not rootNode:  # ........> O(1)
#         return
#     inOrderTraversal(rootNode.leftChild)  # ........> O(n/2)
#     print(rootNode.data)  # ........> O(1)
#     inOrderTraversal(rootNode.rightChild)  # ........> O(n/2)

# inOrderTraversal(newBT)
 
# # ........> O(n)T, S
# def postOrderTraversal(rootNode):
#     if not rootNode:  # ........> O(1)
#         return
#     postOrderTraversal(rootNode.leftChild)  # ........> O(n/2)
#     postOrderTraversal(rootNode.rightChild)  # ........> O(n/2)
#     print(rootNode.data)  # ........> O(1)

# postOrderTraversal(newBT)