
class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.previous = None


class DoublyLinedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            

    # O(1) T, O(1) S
    def createDLL(self, nodeValue=None):
        node = Node(nodeValue)
        node.next = None
        node.previous = None;
#         self.head = node
#         self.tail = node
#         return "Doubly linked list is created"

# doublyLL = DoublyLinedList()
# doublyLL.createDLL(5);

# print([node.value for node in doublyLL])