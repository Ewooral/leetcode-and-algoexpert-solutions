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

     # O(1) T, O(1) S
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
                
             


                

     
newCircularSLL = CircularSLL();
print(newCircularSLL.createSLL(1111));
newCircularSLL.insertCSLL(11, 0);
newCircularSLL.insertCSLL(1, 0);
newCircularSLL.insertCSLL(111, 2);
newCircularSLL.insertCSLL(11111, 1);
newCircularSLL.traverseCSLL();

print([node.value for node in newCircularSLL])