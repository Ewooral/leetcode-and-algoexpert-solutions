# #   Created by Boahen Owusu-Ewooral Elijah.
# #   Copyright © 2022 Optimize Code. All rights reserved.

class Node:
    def __init__(self, value = None) -> None:
        self.value = value;
        self.next = None;
        self.previous = None;

class circularDoublyLinkedList:
    def __init(self):
        self.head = None;
        self.tail = None;

    def __iter__(self):
        node = self.head;
        while node:
            yield node;
            node = node.next;
            if node == self.tail.next:
                break;
    def createCircularDLL(self, nodeValue):
        node = Node(nodeValue);
        self.head = node;
        self.tail = node;
        node.previous = node;
        node.next = node
        print("Circular doubly linked list has been successfully created!!"); 

    def insertCircularDLL(self, value, location):
        if self.head is None:
            print("Nothing to insert because head is not available");
        else:
            node = Node(value);
            if location == 0:
               node.next = self.head
               node.previous = self.tail
               self.head.previous = node
               self.head = node;
               self.tail.next = node
            elif location == 1:
                node.next = self.head
                node.previous = self.tail
                self.head.previous = node
                self.tail.next = node
                self.tail = node;
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1;
                node.next = tempNode.next
                node.prev = tempNode
                node.next.prev = node
                tempNode.next = node
            return "The node has been successfully inserted"



    def traverseCircularDLL(self):
          if self.head is None:
              print("Head doesn'nt exit");
          else:
              node = self.head;
              while node:
                  print(node.value)
                  node = node.next;
                  if node == self.tail.next:
                      break;
    
    def reverseTraverseCDLL(self):
        if self.head is None:
            print("head doesn't exist");
        else:
            node = self.tail
            while node:
                print(node.value)
                if node == self.head:
                    break
                node = node.previous
                



circularDLL = circularDoublyLinkedList();
circularDLL.createCircularDLL(1);
circularDLL.insertCircularDLL(2, 0);
circularDLL.insertCircularDLL(3, 1);
# circularDLL.insertCircularDLL(30, 2);
# circularDLL.insertCircularDLL(4000, 3);

# print([node.value for node in circularDLL]);

# circularDLL.traverseCircularDLL()
# circularDLL.reverseTraverseCDLL()