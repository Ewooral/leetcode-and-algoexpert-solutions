class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))

    # O(v + e) T, O(v) S
    def breadthFirstSearch(self, array):
        queue = [self]
        while len(queue) > 0:
            current = queue.pop(0)
            array.append(current.name)
            for child in current.children:
                queue.append(child)
        return array


node = Node(0)
node.addChild(1)
node.addChild(2)
node.addChild(3)

print(node.breadthFirstSearch([]))