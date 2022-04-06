
from decimal import Inexact


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
        self.head = node
        self.tail = node
        return "Doubly linked list is created"

    def insertDLL(self, value, location):
        if self.head is None:
            print("the node cannot be inserted")
        else:
            newNode = Node(value);
            if location == 0:
                newNode.previous = None;
                newNode.next = self.head;
                self.head.previous = newNode
                self.head = newNode
            elif location == 1:
                newNode.next = None;
                newNode.previous = self.tail
                self.tail.next = newNode
                self.tail = newNode
    #         else:
    #             tempNode = self.head
    #             index = 0
    #             while index < location - 1:
    #                 tempNode = tempNode.next
    #                 index += 1;
    #             newNode.next = tempNode.next
    #             newNode.previous = tempNode
    #             newNode.next.previous = newNode
    #             tempNode.next = newNode

                


doublyLL = DoublyLinedList()
doublyLL.createDLL(5);
doublyLL.insertDLL(1, 0)
doublyLL.insertDLL(2, 1)
doublyLL.insertDLL(3, 2)
doublyLL.insertDLL(30, 3)

print([node.value for node in doublyLL])