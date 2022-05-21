# O(1) T, O(n) S
class Queue:
    def __init__(self, maxSize) -> None:
        self.items = maxSize * [None]
        self.maxSize = maxSize # analogous to length of the array
        self.start = -1
        self.end = -1 
        

    def __str__(self) -> str:
        values = [str(x) for x in self.items]
        return " ".join(values)
    
    # O(1) T, O(1) S
    def isFull(self):
        if self.end + 1 == self.start:
            return True
        elif self.start == 0 and self.end + 1 == self.maxSize:
            return True;
        else:
            return False;
    
    # O(1) T, O(1) S
    def isEmpty(self):
        if self.end == -1:
            return True;
        else:
            return False


    """
    ENQUEUING ALGORITHM

    1. Check if the queue is full. if it is, print
    queue is full else:

    2. Check if the element at the end of the queue
    is the same as the max size of the queue. If it is,
    set the last element's index to zero

    3. else: increment the last element's index by 1
    and check if the first element's index is set to -1

    4. after that enqueue the element at the end of 
    the queue using the index 
    """

    # O(1) T, O(1) S
    def enqueue(self, value):
        if self.isFull():
            print ("The queue is full")
        else:
            if self.end + 1 == self.maxSize:    
                self.end = 0
            else:
                self.end += 1
                if self.start == -1:
                    self.start = 0
            self.items[self.end] = value
            return "The element is inserted at the end of Queue"
   
    # O(1) T, O(1) S
    def dequeue(self):
        if self.isEmpty():
            print("queue is empty")
        else:
            firstElement = self.items[self.start]
            start = self.start
            if self.start == self.end: # if only one item is in the queue
                self.start = -1
                self.end = -1
            elif self.start + 1 == self.maxSize: # if the start index points to the last element
                self.start = 0
            else:
                self.start += 1
            self.items[start] = None;
            print("Dequeued: ", firstElement)

    # O(1) T, O(1) S
    def peek(self):
        if self.isEmpty():
            print("queue is empty")
        else:
            return self.items[self.start]

        # O(1) T, O(1) S
    def delete(self):
        self.items = self.maxSize * [None]  
        self.start = -1
        self.end = -1


customQueue = Queue(3) # A queue with maxsize of 3
customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
print("elements in the queue:\n",  customQueue.items)

print(customQueue.enqueue(4))


customQueue.dequeue()
print("elements after dequeuing:\n",  customQueue.items)

print("Peek: ", customQueue.peek())


print("isFull: ", customQueue.isFull())

customQueue.delete()
print("Queue after deletion: ", customQueue.items)