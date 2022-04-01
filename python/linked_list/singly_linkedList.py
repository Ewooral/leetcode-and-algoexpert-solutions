""" 
  1. create Head and Tail and assign null references to it
  2. Complexity: O(1) T, O(1) S -> if only one node is created  else, O(N)S
"""
# create a singly linked list

class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None


class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

        # the below code makes our linked list printable
    def __iter__(self):
        node = self.head;
        while node:
            yield node;
            node = node.next

# insert in linked list  -> O(N) T and O(1) S
    def insertSLL(self, value, location):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:
                newNode.next = self.head
                self.head = newNode
            elif location == 1:
                newNode.next = None 
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next 
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode

# Traverse a singly linked list  -> O(N) T, O(1) S
    def traverseSLL(self):
        if self.head is None:
            print("The Singly Linked List does not exist");
        else:
            node = self.head
            while node is not None:
                print(node.value)
                node = node.next


# Seaarch for a node in a given singly linked list -> O(N) T, O(1) S
    def searchSLL(self, nodeValue) -> None:
        if self.head is None:
            return "The list does not exit"
        else:
            node = self.head
            while node is not None:
                if node.value == nodeValue:
                    return node.value
                node = node.next
            return "The value does not exist in this list"

# delete a node from a singly linked list -> O(N) T, O(1) S
    def deleteNode(self, location):
        if self.head is None:
            print('the singly linked list does not exist');
        else:
            if location == 0: # deleting from the begining
                if self.head == self.tail: # if we have only one node
                    self.head = None;
                    self.tail = None;
                else: # if we have more than one node
                    self.head = self.head.next;
            elif location == 1:
                if self.head == self.tail:  # if we have only one node
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next 
                    node.next = None
                    self.tail = node;
            else:
                tempNode = self.head
                index = 0
                while index < location - 1: 
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = nextNode.next

# delete entire singly linked list -> O(1) T, O(1) S
    def deleteEntireSLL(self):
        if self.head is None:
            print("The Singly linked list does not exit")
        else:
            self.head = None;
            self.tail = None;

singlyLinkedList = SLinkedList();
singlyLinkedList.insertSLL(1, 1)
singlyLinkedList.insertSLL(2, 1)
singlyLinkedList.insertSLL(3, 1)
singlyLinkedList.insertSLL(4, 1)  

#insert at the beginning 
singlyLinkedList.insertSLL(30, 0)

# insert in the middle -> O(N) T, O(1) S
singlyLinkedList.insertSLL(9, 3)
print([node.value for node in singlyLinkedList])

# traverse a singly linked list -> O(N) T, O(1) S
singlyLinkedList.traverseSLL();

# search a node in a singly linked list -> O(N) T, O(1) S
print("node exits and it is: ", singlyLinkedList.searchSLL(30));
    
# delete a node
singlyLinkedList.deleteNode(1)
print([node.value for node in singlyLinkedList])

# delete the entire singly linked list -> O(1) T, O(1) S
singlyLinkedList.deleteEntireSLL();
print([node.value for node in singlyLinkedList])
