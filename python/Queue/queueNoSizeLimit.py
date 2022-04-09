class Queue:
    def __init__(self) -> None:
        self.items = []

    # O(1) T, O(1) S
    def __str__(self) -> str:
        values = [str(x) for x in self.items]
        return ' '.join(values)
    # O(1) T, O(1) S
    def isEmpty(self):
        if self.items == []:
            return True;
        else:
            return False; 
       # O(n) T, O(1) S
    def enqueue(self, value):
        self.items.append(value)
        return "The element is inserted at the end of queue"
        # O(n) T, O(1) S
    def dequeue(self):
        if self.isEmpty():
            return "Empty Queue "
        else:
            return self.items.pop(0)
        # O(1) T, O(1) S
    def peek(self):
        if self.isEmpty():
            return "empty list"
        else:
            return self.items[0]

        # O(1) T, O(1) S
    def delete(self):
        self.items.clear()
        print('all items cleared')

customQueue = Queue();
print(customQueue.isEmpty())
print("....................")
customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
print(customQueue)
print("....................")

print(customQueue.peek())
print("....................")

customQueue.dequeue()
print(customQueue)
print("....................")

customQueue.delete()
print(customQueue)
print("....................")
