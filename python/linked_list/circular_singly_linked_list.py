class Node:
    def __init__(self, value = None):
        self.value = value;
        self.next = None;
    
class CircularSLL:
    def __init__(self) -> None:
        self.head = None;
        self.tail = None;

    def __iter__(self):
        node = self.head
        while node:
            yield node
            if node == self.head.next:  # if node references itself
                break;
            node = node.next
    def createSLL(self, nodeValue):
        node = Node(nodeValue)
        node.next = node;
        self.head = node
        self.tail = node;
        return "circular Singly linked list is created";

     
    def  insertCSLL(self, value, location):
        if self.head is None:
            print("List doesn't exit")
        else:
            newNode = Node(value)
            if location == 0:
                newNode.next = self.head;
                self.head = newNode
                self.tail.next = newNode 
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
                
          
                
                


                

     
newCircularSLL = CircularSLL()
newCircularSLL.createSLL(21)
newCircularSLL.insertCSLL(100, 0)
print([node.value for node in newCircularSLL])