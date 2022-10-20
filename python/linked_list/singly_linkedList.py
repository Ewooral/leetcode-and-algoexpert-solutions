""" 
  1. create Head and Tail and assign null references to it
  2. Complexity: O(1) T, O(1) S -> if only one node is created  else, O(N)S
"""

# create a singly linked list
from random import randint


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end=" ")
            temp = temp.next
        print()


class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

        # the below code makes our linked list printable

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def __str__(self):
        values = [str(x.value) for x in self]
        return '->'.join(values)

    # insert in linked list  -> O(N) T and O(1) S
    def insertSLL(self, value, location):
        newNode = Node(value)
        if self.head is None:  # if the list doesn't exit, create it
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
                temp_node = self.head
                while index < location - 1:
                    temp_node = temp_node.next
                    index += 1
                next_node = temp_node.next
                temp_node.next = newNode
                newNode.next = next_node

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
        count = 0
        if self.head is None:
            return
        else:
            while self.head is not None:
                self.head = self.head.next
                count += 1
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
                while index < location - 1:  # this loops till it gets to the node which is previous to the node to be deleted.
                    tempNode = tempNode.next
                    index += 1
                tempNode.next = tempNode.next.next

            # delete entire singly linked list -> O(1) T, O(1) S

    def deleteEntireSLL(self):
        if self.head is None:
            print("The Singly linked list does not exit")
        else:
            self.head = None
            self.tail = None

    def add(self, value):
        if self.head is None:
            newNode = Node(value)
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
        return self.tail

    def generate(self, n, minValue, maxValue):
        self.head = None
        self.tail = None
        for i in range(n):
            self.add(randint(minValue, maxValue))
        return self

    def detect_loop(self):
        node = self.head
        hash_t = {}
        while node is not None:
            if node.value in hash_t:
                return "Loop has been detected!"
            hash_t[node.value] = True
            node = node.next
        return hash_t

    def find_duplicate(self):
        node = self.head
        left_p, Len = 0, self.length()
        while left_p < Len:
            next_node = node.next
            right_p = left_p + 1
            while right_p < Len:
                if node.value == next_node.value:
                    return "Duplicates detected!"
                next_node = next_node.next
                right_p += 1
            node = node.next
            left_p += 1
        return "No duplicates detected"

    # O(n) time | O(1) space
    def reverse(self):
        previous, current, next = None, self.head, None
        while current is not None:
            next = current.next  # temporarily store the next node
            current.next = previous  # reverse the current node
            previous = current  # before we move to the next node, point previous to the current node
            current = next  # move on the next node
        print(previous)





singlyLinkedList = SLinkedList()

print("Generate LinkedList: ")
singlyLinkedList.generate(1, 2, 7)
print(singlyLinkedList)
# insert at the end
singlyLinkedList.insertSLL(9, 1)

# insert at the beginning
singlyLinkedList.insertSLL(-78, 0)
# singlyLinkedList.insertSLL(2, 8)

# insert in the middle -> O(N) T, O(1) S

singlyLinkedList.insertSLL(1, 3)
singlyLinkedList.insertSLL(29011993, 3)
singlyLinkedList.insertSLL(1, 4)

print("Print List...................................")
# print the linked list
print([node.value for node in singlyLinkedList])
print("Traverse ....................................")
# traverse a singly linked list -> O(N) T, O(1) S
singlyLinkedList.traverseSLL()

print("Detect Loop......................")
# find loop
print(singlyLinkedList.detect_loop())

print("Find Duplicates......................")
# find loop
print(singlyLinkedList.find_duplicate())

print("Reverse Linked List")
# lists = [node.value for node in singlyLinkedList]
# lists.reverse()
singlyLinkedList.reverse()



print("Search.......................................")
# search a node in a singly linked list -> O(N) T, O(1) S
print(singlyLinkedList.searchSLL(9))

print("Delete.......................................")
# delete a node

print([node.value for node in singlyLinkedList])
singlyLinkedList.deleteNode(3)
# singlyLinkedList.deleteNode(1)
print([node.value for node in singlyLinkedList])
singlyLinkedList.insertSLL(29011993, 2)
print([node.value for node in singlyLinkedList])

print("Length of List.......................................")
print(singlyLinkedList.length())
# delete the entire singly linked list -> O(1) T, O(1) S
# singlyLinkedList.deleteEntireSLL();

# print([node.value for node in singlyLinkedList])
