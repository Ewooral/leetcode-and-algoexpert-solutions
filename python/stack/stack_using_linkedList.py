"""
1. Create a blank stack
2. Create an object of linked list class
 
"""

class Node:
    def __init__(self, value = None) -> None:
        self.value = value
        self.next = next;

class LinkedList:
    def __init__(self):
        self.head = None;

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

class Stack:
    def __init__(self):
        self.LinkedList = LinkedList();
    
    def __str__(self):
        
        values = [str(x.value) for x in self.LinkedList]
        return ' '.join(values)   

    # O(1) T, O(1) S
    def isEmpty(self):
        if self.LinkedList.head is None:
            return True;
        else:
            return False;

     # O(1) T, O(1) S
    def push(self, value):
        node = Node(value)
        node.next = self.LinkedList.head
        self.LinkedList.head = node
            
        

    # O(1) T, O(1) S
    def pop(self):
        if self.isEmpty():
            return "There is no element in the stack"
        else:
            nodeValue = self.LinkedList.head.value
            self.LinkedList.head = self.LinkedList.head.next
            return nodeValue

    # O(1) T, O(1) S
    def peek(self):
        if self.isEmpty(): 
            return "There is no element in the stack"
        else:
            nodeValue = self.LinkedList.head.value
            return nodeValue

    # O(1) T, O(1) S
    def delete(self):
        self.LinkedList.head = None

customStack = Stack()
customStack.push(1)
customStack.push(2)
customStack.push(3)
print(customStack)
print(".......................")
customStack.pop()
print(customStack)

print("......................")
print(customStack.peek())

print(".......................")
print(customStack.isEmpty())

print(".......................")
customStack.delete()
print(customStack)
