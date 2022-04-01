""" create Head and Tail and assign null references to it
# O(1) T if more than one node is created O(N) S else O(1)S
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

# INSERTING INTO A SINGLY LINKED LIST
class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None


class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

        # the below code makes our list printable
    def __iter__(self):
        node = self.head;
        while node:
            yield node;
            node = node.next

# insert in linked list
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

# Traverse a singly linked list

singlyLinkedList = SLinkedList();
singlyLinkedList.insertSLL(1, 1)
singlyLinkedList.insertSLL(2, 1)
singlyLinkedList.insertSLL(3, 1)
singlyLinkedList.insertSLL(4, 1)  

#insert at the beginning 
singlyLinkedList.insertSLL(30, 0)

# insert in the middle
singlyLinkedList.insertSLL(9, 3)
print([node.value for node in singlyLinkedList])
    

