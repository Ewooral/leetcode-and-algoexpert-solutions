from BT import Node, get_parent, _get_tree_properties, NodeValue

root = Node("Drink")

root.left = Node("Hot")
root.right = Node("Cold")
# leftChild = root.left
rightChild = root.right
leftChild.left = Node("tea")
leftChild.right = Node("coffee")
rightChild.left = Node("Cola")
rightChild.right = Node("Akpeteshie")


root.validate()
root.pprint()
print(root.levelorder)

print(get_parent(root, rightChild))
print(_get_tree_properties(root).is_complete)
