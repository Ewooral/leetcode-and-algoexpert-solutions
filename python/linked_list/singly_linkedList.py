""" 
  1. create Head and Tail and assign null references to it
  2. Complexity: O(1) T, O(N) S -> if more than one node is created  else O(1)S
"""
# CREATING A SINGLY LINKED LIST
# class Node:
#     def __init__(self, value=None):
#         self.value = value
#         self.next = None


# class SListList:
#     def __init__(self):
#         self.head = None;
#         self.tail = None;


# singlyListList = SListList();  
# node1 = Node(1);
# node2 = Node(2)

# singlyListList.head = node1;
# singlyListList.head.next = node2;
# singlyListList.tail = node2



"""
1. Insertion can be done at the begining
   of the linked list
2. After a node in the middle of linked list
3. At the end of the linked list.
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
    

