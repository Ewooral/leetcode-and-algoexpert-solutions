from binarytree import Node

root = Node("Drink")

root.left = Node("Hot")
root.right = Node("Cold")
leftChild = root.left
rightChild = root.right
leftChild.left = Node("tea")
leftChild.right = Node("coffee")
rightChild.left = Node("Cola")
rightChild.right = Node("Akpeteshie")


root.validate()
root.pprint()