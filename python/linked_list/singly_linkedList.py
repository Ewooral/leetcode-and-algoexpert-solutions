# create Head and Tail and assign null references to it
# O(1) T if more than one node is created O(N) S else O(1)S

# CREATING A SINGLY LINKED LIST
class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class SListList:
    def __init__(self):
        self.head = None;
        self.tail = None;


singlyListList = SListList();  
node1 = Node(1);
node2 = Node(2)

singlyListList.head = node1;
singlyListList.head.next = node2;
singlyListList.tail = node2



"""
1. Insertion can be done at the begining
   of the linked list
2. After a node in the middle of linked list
3. At the end of the linked list.
"""

# INSERTING INTO A SINGLY LINKED LIST
class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class SListList:
    def __init__(self):
        self.head = None
        self.tail = None
    def __iter__(self):
        node = self.head;
        while node:
            yield node;
            node = node.next

