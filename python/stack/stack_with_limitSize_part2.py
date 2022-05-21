# O(1) T, O(n)
class Stack:
    def __init__(self, maxSize=None) -> None:
        try:
            self.maxSize = maxSize
            self.list = []
        except (TypeError, NameError, AttributeError) as err:
            return f"Oops...{err}"

    def __str__(self):
        try:
            values = self.list.reverse()
            values = [str(x) for x in self.list]
            return '\n'.join(values)
        except (TypeError, NameError, AttributeError) as err:
            return f"Oops...{err}"
    # O(1) T, 0(1)

    def isEmpty(self):
        if len(self.list) == 0:
            return True
        return False
     # O(1) T, 0(1)

    def isFull(self):
        if len(self.list) == self.maxSize:
            return True
        return False
    # O(1) T, 0(1)

    def push(self, value):
        if self.isFull():
            return "List is Full"
        self.list.append(value)
        return "item inserted successfully"

    def pop(self):
        if self.isEmpty():
            return "List is empty"
        self.list.pop()
        return "last item is popped off the stack"

    def peekright(self):
        if self.isEmpty():
            return "List is empty"
        return self.list[len(self.list) - 1]

    def peekleft(self):
        if self.isEmpty():
            return "List is empty"
        return self.list[0]

    def delete(self):
        try:
            self.list = None
        except (TypeError, NameError, AttributeError) as err:
            return f"Oops...{err}"


stack = Stack(maxSize=3)
print(stack.push(1))
print(stack.push(11))
print(stack.push(12))
# print(stack.push(152))
print(stack.pop())
# print(stack.pop())
print(stack)
print(stack.isEmpty())
print(stack.isFull())
print(stack.peekleft())
print('peek: ', stack.peekright())
print(stack.delete())
print(stack)
