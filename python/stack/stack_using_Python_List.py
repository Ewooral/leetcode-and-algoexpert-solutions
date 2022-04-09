# created by Elijah Owusu Ewooral Boahen
# copyright 2020 Optmize Code. All rights reserved

# A stack using python list without size limit

# O(1) T, O(1) S
class Stack:
    def __init__(self):
        self.list = []

    
    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return '\n'.join(values)

    # O(1) T, O(1) S
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False

    # Amortised constant time,O(1)/O(n^2),  O(1) S
    def push(self, value):
        self.list.append(value)
        return "element has been inserted"

    # O(1) T, O(1) S
    def pop(self):
        if self.isEmpty():
            return "There is no element in the stack"
        else: 
             return self.list.pop()
            #  return "The top element has been deleted"
    # O(1) T, O(1) S
    def peek(self):
        if self.isEmpty():
            return "There is no element in the stack"
        else:
            # print("The current top element")
            return self.list[len(self.list) - 1]
    
    # O(1) T, O(1) S
    def delete(self):
        self.list = None;


customStack = Stack()
customStack.push(1)
customStack.push(2)
customStack.push(3)
print(customStack)
print(".......................")
customStack.pop()
print(customStack)

print(".......................")
print(customStack.isEmpty())
