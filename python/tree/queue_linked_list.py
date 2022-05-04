# Created by Elijah Owusu Boahen on 09th April, 2022
# Copyright 2020 Optimize Code. All rights reserved.


class Node:
    def __init__(self, value = None) -> None:
        self.value = value;
        self.next = None;

    def __str__(self) -> str:
        return str(self.value)

class LinkedList:
    def __init__(self) -> None:
        self.head = None;
        self.tail = None;

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next 

class Queue:
    def __init__(self) -> None:
        self.linkedlist = LinkedList()
    
    def __str__(self) -> str:
        values = [str(x) for x in self.linkedlist]
        return " ".join(values)

    # O(1) T, O(1) S
    def enqueue(self, value):
        node = Node(value);
        if self.linkedlist.head == None:
            self.linkedlist.head = node;
            self.linkedlist.tail = node;

        else:
            self.linkedlist.tail.next = node
            self.linkedlist.tail = node
    '''
    
    '''
    # O(1) T, O(1) S
    def isEmpty(self):
        if self.linkedlist.head == None:
            return True
        else:
            False;

     # O(1) T, O(1) S
    def dequeue(self):
        if self.isEmpty():
            return "No node in the queue"
        else:
            temp_node = self.linkedlist.head
            if self.linkedlist.head == self.linkedlist.tail:
                self.linkedlist.head = None;
                self.linkedlist.tail = None
            else:
                self.linkedlist.head = self.linkedlist.head.next
            return temp_node

     # O(1) T, O(1) S
    def peek(self):
        if self.isEmpty():
            return "Queue is empty"
        else:
            return self.linkedlist.head

     # O(1) T, O(1) S
    def delete(self):
        self.linkedlist.head = None;
        self.linkedlist.tail = None;
       
customQueue = Queue()
customQueue.enqueue(9)
customQueue.enqueue(2)
customQueue.enqueue(3)
print(customQueue)
print("dequeue: ", customQueue.dequeue())
print(customQueue)
print("Peek: ", customQueue.peek())

customQueue.delete()
print("queue deleted", customQueue)

