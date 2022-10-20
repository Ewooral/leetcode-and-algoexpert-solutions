# Queue Data structure
# Queue class
# Linked list class
# Node class 

class Node:
    def __int__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)


class SinglyLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next


class Stack:
    def __init__(self):
        self.sll = SinglyLL()

    def __str__(self):
        values = [str(x) for x in self.sll]
        return "->".join(values)

    def push(self, value):
        node = Node(value)
        if self.sll.head is None:
            self.sll.head = node
            self.sll.tail = node
        else:
            node.next = self.sll.head
            self.sll.head = node

    def is_empty(self):
        if self.sll.head is None:
            return True
        else:
            return False

    def pop(self):
        if self.is_empty():
            return "SLL is empty"
        else:
            temp_node = self.sll.head
            if self.sll.head == self.sll.tail:
                self.sll.head = None
                self.sll.tail = None
            else:
                self.sll.head = self.sll.head.next
                return temp_node
