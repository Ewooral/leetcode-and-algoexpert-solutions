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
        if self.head is None: # if the list doesn't exit, create it
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
                # insert at/in the middle
                index = 0
                prevNode = self.head
                while index < location - 1:
                    currentNode = prevNode.next
                    index += 1
                nextNode = currentNode.next
                newNode.next = nextNode
                currentNode.next = newNode

# Traverse a singly linked list  -> O(N) T, O(1) S
    def traverseSLL(self):
        if self.head is None:
            return
        node = self.head
        while node is not None:
            print(node.value)
            node = node.next


# Seaarch for a node in a given singly linked list -> O(N) T, O(1) S

    def searchSLL(self, nodeValue):
        if self.head is None:
            return "List doesn't exit"
        else:
            node = self.head
            while node is not None:
                if node.value == nodeValue:
                    return node.value
                node = node.next
            return "node value not found"
   
   
# count the number of values in the list
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


# delete a node from a singly linked list -> O(N) T, O(1) S

    def deleteNode(self, location):
        if self.head is None:
            print("List doesn't exit")

        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
            elif location == 1:  # the end of list
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    prevNode = self.head
                    while prevNode is not None:
                        if prevNode.next == self.tail:
                            break
                        prevNode = prevNode.next
                    prevNode.next = None
                    self.tail = prevNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1: # this loops till it gets to the node which is previous to the node to be deleted. 
                    tempNode = tempNode.next
                    index += 1
                tempNode.next = tempNode.next.next

# delete entire singly linked list -> O(1) T, O(1) S
    def deleteEntireSLL(self):
        if self.head is None:
            print("The Singly linked list does not exit")
        else:
            self.head = None;
            self.tail = None;

singlyLinkedList = SLinkedList();

#insert at the end
singlyLinkedList.insertSLL(1, 1)


#insert at the beginning 
singlyLinkedList.insertSLL(-78, 0)
singlyLinkedList.insertSLL(2, 8)

# insert in the middle -> O(N) T, O(1) S

singlyLinkedList.insertSLL(9, 3)
singlyLinkedList.insertSLL(29011993, 3)
singlyLinkedList.insertSLL(False, 4)

print("Print List...................................")
# print the linked list
print([node.value for node in singlyLinkedList])

print("Traverse ....................................")
# traverse a singly linked list -> O(N) T, O(1) S
singlyLinkedList.traverseSLL()

print("Search.......................................")
# search a node in a singly linked list -> O(N) T, O(1) S
print(singlyLinkedList.searchSLL(9));

print("Delete.......................................")
# delete a node
singlyLinkedList.deleteNode(0)
singlyLinkedList.deleteNode(1)
print([node.value for node in singlyLinkedList])

print("Length of List.......................................")
print(singlyLinkedList.length())
# delete the entire singly linked list -> O(1) T, O(1) S
# singlyLinkedList.deleteEntireSLL();

# print([node.value for node in singlyLinkedList])

