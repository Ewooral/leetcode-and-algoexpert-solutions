
# created by Elijah Owusu Ewooral Boahen
# copyright 2020 Optmize Code. All rights reserved

# O(1) T, O(1) S
class Stack:
    def __init__(self, maxSize):
        self.maxSize = maxSize
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

      
    def isFull(self):
        if len(self.list) == self.maxSize:
            return True
        else: return False;

      # Amortised constant time,O(1)/O(n^2),  O(1) S
    def push(self, value):
        if self.isFull():
            return "Stack is full";
        else:
            self.list.append(value)
            return "inserted successfully"
    
    # O(1) T, O(1) S
    def pop(self):
        if self.isEmpty():
            return "There is no element in the stack"
        else:
            return self.list.pop()

    # O(1) T, O(1) S
    def peek(self):
        if self.isEmpty():
            return "There is no element in the stack"
        else:
            # print("The current top element")
            return self.list[len(self.list) - 1]

     # O(1) T, O(1) S
    def delete(self):
        self.list = None

customStack = Stack(4)
print(customStack.isEmpty())
print(customStack.isFull())
customStack.push(1)
customStack.push(2)
customStack.push(3)
customStack.delete()
print(customStack)

# customStack.delete()
# print(customStack.isFull())

 