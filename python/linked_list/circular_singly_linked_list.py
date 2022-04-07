from tkinter.messagebox import NO


class Node:
    def __init__(self, value = None):
        self.value = value;
        self.next = None;
    
class CircularSLL:
    def __init__(self) -> None:
        self.head = None;
        self.tail = None;

    def __iter__(self):
        node = self.head;
        while node:
            yield node;
            node = node.next
            if node == self.tail.next:  # if node references itself
                break;

    # O(1) T, O(1) S        
    def createSLL(self, nodeValue =None):
        node = Node(nodeValue);
        node.next = node;
        self.head = node;
        self.tail = node;
        return "Circular Singly linked list is created";

     # O(N) T, O(1) S
    def insertCSLL(self, value, location):
        if self.head is None:
            return "The head reference is None";
        else:
            newNode = Node(value);
            if location == 0:  
                newNode.next = self.head;
                self.head = newNode;
                self.tail.next = newNode;

                """
                The last step to make this circular is to connect
                last node to newNode. thus by saving newNode's memory address
                inside of lastNode's reference slot. self.tail.next is the memory 
                location of lastNode
                By connecting self.tail.next to our newNode we 
                are connecting our last node to 
                # """

            elif location == 1:
                newNode.next = self.tail.next;
                self.tail.next = newNode;
                self.tail = newNode;

            else:
                tempNode = self.head;
                index = 0;
                while index < location - 1:  # this will loop tilllast but one node
                    tempNode = tempNode.next; 
                    index += 1;
                nextNode = tempNode.next;
                newNode.next = nextNode;
                tempNode.next = newNode;
            return "The node has been successfully inserted!!";

    # O(N) T, O(1) S
    def traverseCSLL(self):
        if self.head is None:
            return "There is no element for traversal";
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value);
                tempNode = tempNode.next
                if tempNode == self.tail.next:
                    break    
                
     # O(N) T, O(1) S
    def searchCSLL(self, nodeValue):
        if self.head is None:
            print("list doesn't exit")
        else:
            node = self.head
            while node is not None:
                node = node.next
                if nodeValue == node.value:
                    return "searched value: ", node.value
                if node == self.tail.next:
                    return "Nothing..."

     # O(N) T, O(1) S
    def deleteCSLL(self, location):
        if self.head is None:
            print("Nothing to delete");
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None;
                    self.tail = None;
                else:
                    self.head = self.head.next
                    self.tail.next = self.head
                   
            elif location == 1:
                if self.head == self.tail:
                    self.head.next = None;
                    self.head = None;
                    self.tail = None;
                else:
                    node = self.head 
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next 
                    node.next = self.head
                    self.tail = node
            else:
                tempNode = self.head
                index = 0;
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next; 
                tempNode.next = nextNode.next

     # O(1) T, O(1) S
    def deleteEntireCSLL(self):
        self.head = None
        self.tail.next = None
        self.tail = None
            
                


                

     
newCircularSLL = CircularSLL();
print(".................................\n")
print(newCircularSLL.createSLL(1000));
print(newCircularSLL.createSLL(3000));
print(".................................\n")
newCircularSLL.insertCSLL(11, 0);
newCircularSLL.insertCSLL(1, 0);
newCircularSLL.insertCSLL("Jupiter", 0);
newCircularSLL.insertCSLL(False, 0);
newCircularSLL.insertCSLL(111, 2);
newCircularSLL.insertCSLL(11111, 1);

print([node.value for node in newCircularSLL])
print(".................................\n")

newCircularSLL.traverseCSLL()
print(".................................\n")

print(newCircularSLL.searchCSLL("Jupiter"))
print(".................................\n")
newCircularSLL.deleteCSLL(0)
newCircularSLL.deleteCSLL(0)
newCircularSLL.deleteCSLL(1)
print([node.value for node in newCircularSLL])
print(".................................\n")
newCircularSLL.deleteEntireCSLL()
print([node.value for node in newCircularSLL])
