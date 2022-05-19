# Binary Tree

import queue_linked_list as qu
# import queue


class BT:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


root = BT("Dickson")
L = BT("Georgina")
R = BT("Emmanuel")
# L_s = BT("Georgina's Son")
# R_s = BT("Emma's Son")
#
# L.left = L_s
# L.right = R_s

root.left = L
root.right = R


def preorder(rootNode):
    if rootNode is None:
        return
    print(rootNode.data)
    preorder(rootNode.left)
    preorder(rootNode.right)


print("...preorder...")
preorder(root)


def inorder(rootNode):
    if rootNode is None:
        return
    inorder(rootNode.left)
    print(rootNode.data)
    inorder(rootNode.right)


print("...inorder...")
inorder(root)


def postorder(rootNode):
    if rootNode is None:
        return
    postorder(rootNode.left)
    postorder(rootNode.right)
    print(rootNode.data)


print("...postorder...")
postorder(root)


def levelorder(rootNode):
    if rootNode is None:
        return
    else:
        q = qu.Queue()
        q.enqueue(rootNode)
        while not q.isEmpty():
            root = q.dequeue()
            print(root.value.data)
            if root.value.left is not None:
                q.enqueue(root.value.left)
            if root.value.right is not None:
                q.enqueue(root.value.right)


print("...levelorder...")
levelorder(root)


def search(rootNode, nodevalue):
    if not rootNode:
        return
    else:
        q = qu.Queue()
        q.enqueue(rootNode)
        while not q.isEmpty():
            root = q.dequeue()
            if root.value.data == nodevalue:
                return "Found"
            if root.value.left is not None:
                q.enqueue(root.value.left)
            if root.value.right is not None:
                q.enqueue(root.value.right)
        return "not found"


print("...search...")
print(search(root, "Elisha"))


def insert(rootNode, nodeValue):
    if rootNode is None:
        rootNode = nodeValue
    else:
        q = qu.Queue()
        q.enqueue(rootNode)
        while not q.isEmpty():
            root = q.dequeue()
            if root.value.left is not None:
                q.enqueue(root.value.left)
            else:
                root.value.left = nodeValue
                return
            if root.value.right is not None:
                q.enqueue(root.value.right)
            else:
                root.value.right = nodeValue
                return


print("...insert...")
Mary = BT("Mary")
Elijah = BT("Elijah")
Elisha = BT("Elisha")
insert(root, Mary)
insert(root, Elijah)
insert(root, Elisha)
levelorder(root)


def getDeepestNode(rootNode):
    if rootNode is None:
        return
    else:
        q = qu.Queue()
        q.enqueue(rootNode)
        while not q.isEmpty():
            root = q.dequeue()
            if root.value.left is not None:
                q.enqueue(root.value.left)
            if root.value.right is not None:
                q.enqueue(root.value.right)

        deepestNode = root.value
        return deepestNode


print("...deepest node...")
dNode = getDeepestNode(root)
print(dNode.data)


def deleteDNode(rootNode, dNode):
    if rootNode is None:
        return
    else:
        q = qu.Queue()
        q.enqueue(rootNode)
        while not q.isEmpty():
            root = q.dequeue()
            if root.value is dNode:
                root.value = None

            if root.value.left is not None:
                if root.value.left is dNode:
                   root.value.left = None

                else:
                    q.enqueue(root.value.left)

            if root.value.right is not None:
                if root.value.right is dNode:
                   root.value.right = None

                else:
                    q.enqueue(root.value.right)


print("...delete deepest node...")
deleteDNode(root, getDeepestNode(root))
levelorder(root)


def deleteAnyNode(rootNode, node):
    if rootNode is None:
        return
    else:
        q = qu.Queue()
        q.enqueue(rootNode)
        while not q.isEmpty():
            root = q.dequeue()
            if root.value.data is node:
                deepNode = getDeepestNode(rootNode)
                root.value.data = deepNode.data
                deleteDNode(rootNode, deepNode)
                return
            if root.value.left is not None:
                q.enqueue(root.value.left)
            if root.value.right is not None:
                q.enqueue(root.value.right)


print("...delete any node...")
deleteAnyNode(root, "Georgina")


# deleteAnyNode(root, "Mary")
levelorder(root)
