# Search O(N)Time, O(1) space
# insert O(n)Time, O(1) space -> worst case

from dataclasses import dataclass
from typing import Any


@dataclass
class Node:
    value: Any = None
    next: Any = None
    prev: Any = None


@dataclass
class DoublyLinkedList:
    head: Any = None
    tail: Any = None
    
    # def __iter__(self):
    #     node = self.head
    #     while node:
    #         yield node
    #         node = node.next

    def print_list(self):
        temp = self.head
        li = []
        while temp is not None:
            li.append(temp.value)
            # print(temp.value, end=" ")
            temp = temp.next
        print(li)

    def setHead(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            return
        self.insertBefore(self.head, node)

    def setTail(self, node):
        # if self.tail is None:
            self.head = node
            return
        self.insertAfter(self.tail, node)

    def length(self):
        count = 0;
        # node = self.head
        if self.head == None:
            return;
        else:
            while self.head is not None:
                self.head = self.head.next
                count += 1;
        return count

    def insertBefore(self, node, nodeToInsert):
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return
        self.remove(nodeToInsert)
        nodeToInsert.prev = node.prev # update the pointer
        nodeToInsert.next = node 
        if node.prev is None:
            self.head = nodeToInsert
        else:
            node.prev.next = nodeToInsert
        node.prev = nodeToInsert # overwriting the pointer

    def insertAfter(self, node, nodeToInsert):
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return
        self.remove(nodeToInsert)
        node.prev = nodeToInsert  # overwriting the pointer
        nodeToInsert.next = node.next
        if node.next is None:
            self.tail = nodeToInsert
        else:
            node.next.prev = nodeToInsert
        node.next = nodeToInsert # update

    def insertAtPosition(self, position, nodeToInsert):
        if position == 1:
            self.setHead(nodeToInsert)
            return
        node = self.head
        currentPosition = 1
        while node is not None and currentPosition != position:
            node = node.next
            currentPosition += 1
        if node is not None:
            self.insertBefore(node, nodeToInsert)
        else:
            self.setTail(nodeToInsert)

    def removeNodesWithValue(self, value):
        node = self.head
        while node is not None:
            nodeToRemove = node
            node = node.next
            if nodeToRemove.value == value:
                self.remove(nodeToRemove)

    def remove(self, node):
        if node == self.head:
            self.head = self.head.next
        if node ==self.tail:
            self.tail = self.tail.prev
        self.removeNodeBindings(node)

    def containsNodeWithValue(self, value):
        node = self.head
        while node is not None and node.value != value:
            node = node.next 
        return node is not None

    def removeNodeBindings(self, node):
        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev
        node.prev = None
        node.next = None 


def main():
    node = Node(value= 20)
    node1 = Node(value=30)
    node3 = Node(value = 89)

    linkedList = DoublyLinkedList()
    linkedList.setHead(node)

    print()
    print("......................")
    # print(linkedList.head)

    linkedList.insertBefore(node, Node(value=320) )
    linkedList.insertAfter(node, node1 )
    linkedList.insertAtPosition(4, node3)

    linkedList.print_list()
    print(linkedList.length())


if __name__ == "__main__":
    main()




