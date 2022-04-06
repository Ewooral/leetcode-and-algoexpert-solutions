
class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.previous = None


class DoublyLinedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            

    # O(1) T, O(1) S
    def createDLL(self, nodeValue):
        node = Node(nodeValue)
        node.previous = None;
        node.next = None
        self.head = node
        self.tail = node
        return "Doubly linked list is created"

    # O(N) T, O(1) S
    def insertDLL(self, value, location):
        if self.head is None:
            print("the node cannot be inserted")
        else:
            newNode = Node(value);
            if location == 0:
                newNode.previous = None;
                newNode.next = self.head;
                self.head.previous = newNode
                self.head = newNode
            elif location == 1:
                newNode.next = None;
                newNode.previous = self.tail
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1;
                newNode.next = tempNode.next
                newNode.previous = tempNode
                newNode.next.previous = newNode
                tempNode.next = newNode
     
     # O(N) T, O(1) S
    def traverseDLL(self):
        if self.head is None:
            print("Nothing to traverse");
        else:
            node = self.head
            while node is not None:
                print(node.value)
                node = node.next
    
     # O(N) T, O(1) S
    def reverseTraverseDLL(self):
        if self.head is None:
            print("Nothing to traverse")
        else:
            node = self.tail
            while node is not None:
                print(node.value)
                node = node.previous

     # O(N) T, O(1) S
    def searchDLL(self, nodeValue):
        if self.head is None:
            print("Nothing to search");
        else:
            node = self.head
            while node is not None:
                if node.value == nodeValue:
                     print(node.value)
                node = node.next
                    
    def deleteNode(self, location):
        if self.head is None:
            print("There is not any element in DLL")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.previous = None
            elif location == 1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.previous
                    self.tail.next = None
            else:
                curNode = self.head
                index = 0
                while index < location - 1:
                    curNode = curNode.next
                    index += 1
                curNode.next = curNode.next.next
                curNode.next.previous = curNode
            print("The node has been successfully deleted")


                
                    

doublyLL = DoublyLinedList()
doublyLL.createDLL(5);
doublyLL.insertDLL(1, 0)
doublyLL.insertDLL(2, 1)
doublyLL.insertDLL(3, 2)



print([node.value for node in doublyLL])
doublyLL.traverseDLL()

print("Reverse Traversal.......................")
doublyLL.reverseTraverseDLL()

print("Search.......................")
doublyLL.searchDLL(30)

print("Delete.......................")
# doublyLL.deleteNodeDLL(2)
doublyLL.deleteNode(0)
print([node.value for node in doublyLL])
