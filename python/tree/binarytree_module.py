from BT import Node, get_parent, _get_tree_properties
import queue as q


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


print(".........PreOrder.........")


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

print(".........InOrder.........")


def inOrder(rootNode):
    if not rootNode:
        return
    inOrder(rootNode.left)
    print(rootNode.value)
    inOrder(rootNode.right)


print("..............")
inOrder(Coach)
print(str(Coach.inorder))

print(".........PostOrder.........")


def postOrder(rootNode):
    if not rootNode:
        return
    postOrder(rootNode.left)
    postOrder(rootNode.right)
    print(rootNode.value)


postOrder(Coach)
print(Coach.postorder)

print("............LevelOrder.................")


def levelOrder(rootNode):
    if not rootNode:
        return
    else:
        customQueue = q.Queue()
        # customQueue = deque()
        # customQueue =  q.LifoQueue()
        customQueue.put(rootNode)
        # print("get: ", customQueue.get())
        # customQueue.put(rootNode)
        while not customQueue.empty():
            root = customQueue.get()
            print(root.value)
            if root.left is not None:
                customQueue.put(root.left)
            if root.right is not None:
                customQueue.put(root.right)


levelOrder(Coach)
print(Coach.levelorder)

print(".........Search.............")


def search(rootNode, nodeValue):
    if rootNode is None:
        return
    else:
        customQ = q.Queue()
        customQ.put(rootNode)
        while not customQ.empty():
            root = customQ.get()
            if root.value == nodeValue:
                return True
            if root.left is not None:
                customQ.put(root.left)
            if root.right is not None:
                customQ.put(root.right)

        return False


print(search(Coach, "Cristiano Ronaldo"))

print(".........Insert...............")
def insert(rootNode, newNode):
    if rootNode is None:
        rootNode = newNode
    else:
        customQ = q.Queue()
        customQ.put(rootNode)
        while not customQ.empty():
            root = customQ.get()
            if root.left is not None:
                customQ.put(root.left)
            else:
                root.left = newNode
                return 

            if root.right is not None:
                customQ.put(root.right)
            else:
                root.right = newNode
                return


newPlayer = Node("Luca Modrich")
newPlayer2 = Node("Tony kroos")
insert(Coach, newPlayer)
insert(Coach, newPlayer2)
levelOrder(Coach)

print("......Deepest Node......")


def getDeepestnode(rootNode):
    if rootNode is None:
        return
    else:
        customQueue = q.Queue()
        # customQueue = deque()
        # customQueue =  q.LifoQueue()
        customQueue.put(rootNode)
        # print("get: ", customQueue.get())
        customQueue.put(rootNode)
        while not customQueue.empty():
            root = customQueue.get()
            if root.left is not None:
                customQueue.put(root.left)
            if root.right is not None:
                customQueue.put(root.right)
        DeepestNode = root.value
        return DeepestNode


dp = getDeepestnode(root)
dp1 = getDeepestnode(Coach)
print(dp1)

print(".........delete DeepestNode.........")
def deleteDeepestnode(rootNode, dNode):
    if rootNode is None:
        return 
    else:
        Q = q.Queue()
        Q.put(rootNode)
        while not Q.empty():
            root =  Q.get()
            if root.value == dNode:
                root.value == None;
                return
            if root.right is not None:
                if root.right is dNode:
                    root.right = None;
                    return
                else:
                    Q.put(root.right)
            
            if root.left is not None:
                if root.left is dNode:
                    root.left = None
                    return
                else:
                    Q.put(root.left)


newNode = getDeepestnode(Coach)
deleteDeepestnode(Coach, newNode)
levelOrder(Coach)
