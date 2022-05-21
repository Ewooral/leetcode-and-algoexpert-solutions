class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class SinglyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def insert(self, value, location):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:
                newNode.next = self.head
                self.head = newNode
                return "Inserted successfully"

            elif location == 1:
                self.tail.next = newNode
                newNode.next = None
                self.tail = newNode
                return "Inserted successfully"

            else:
                index = 0
                prevNode = self.head
                while index < location - 1:
                    currentNode = prevNode.next
                    index += 1
                nextNode = currentNode.next
                newNode.next = nextNode
                currentNode.next = newNode
                return "Inserted successfully"

    def traverse(self):
        if self.head is None:
            return "Linked List is not available"
        node = self.head
        while node:
            print(node.value)
            node = node.next

    def search(self, value):
        if self.head is None:
            return "Linked List is not available"
        node = self.head
        while node:
            if node.value == value:
                return "Found Value"
            node = node.next
            return "Not found"

    def deleteNode(self, location):
        if self.head is None:
            return "linked list not available"

        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                    return "deleted successfully"
                else:
                    self.head = self.head.next
            elif location == 1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                    return
                else:
                    node = self.head
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next
                    elementBeforeLast = node
                    elementBeforeLast.next = None
                    self.tail = elementBeforeLast
                    return "deleted successfully"
            else:
                index = 0
                node = self.head
                while index < location - 1:
                    node = node.next
                    index += 1
                nextNode = node.next
                node.next = nextNode.next
                return "deleted successfully"


SLL = SinglyLinkedList()
print("...insert...")
SLL.insert(1, 1)
print(SLL.insert(100, 0))
SLL.insert(10, 0)
print(SLL.insert(103, 2))
SLL.insert("1034", 3)
print(SLL.insert("family", 3))

print("...traverse...")
SLL.traverse()

print("...search...")
print(SLL.search(1.2))


print("...Linked List...")
print([node.value for node in SLL])

print("...delete...")
print(SLL.deleteNode(0))
print(SLL.deleteNode(1))
print(SLL.deleteNode(2))

print("...Linked List...")
print([node.value for node in SLL])
