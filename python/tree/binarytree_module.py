from BT import Node, get_parent, _get_tree_properties, NodeValue, 

root = Node("Drink")

root.left = Node("Hot")
root.right = Node("Cold")
leftChild = root.left
rightChild = root.right
leftChild.left = Node("tea")
leftChild.right = Node("coffee")
rightChild.left = Node("Cola")
rightChild.right = Node("Akpeteshie")
leftChild.left.left = Node("Gari")
leftChild.left.right = Node("Orange")



root.validate()
root.pprint()
print(root.preorder)

print(get_parent(root, rightChild))
print(_get_tree_properties(root).is_complete)

print("................")
Coach = Node("Carlo Ancelotti")
player1 = Node("Cristiano Ronaldo")
player2 = Node("Marcus RashFord")
player3 = Node("Bruno Fernandes")
player4 = Node("Juan Marta")

Coach.left = player1
Coach.right = player2
player1.left = player3
player1.right = player4



def preOrder(rootNode):
    if not rootNode:
        return
    print(rootNode.value)
    preOrder(rootNode.left)
    preOrder(rootNode.right)
preOrder(Coach)
print("..............")
print(Coach.preorder)
Coach.pprint()

def inOrder(rootNode):
    if not rootNode:
        return 
    inOrder(rootNode.left)
    print(rootNode.value)
    inOrder(rootNode.right)

print("..............")
inOrder(Coach)
print(str(Coach.inorder))


