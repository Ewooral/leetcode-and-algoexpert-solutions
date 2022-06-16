from dataclasses import dataclass
from typing import Any, Optional


@dataclass
class LinkedList:
    value: Any = None
    next: Optional[Any] = None

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end=" ")
            temp = temp.next
        print()



def remove_duplicates(linkedList):
    currentNode = linkedList
    while currentNode is not None:
        nextDistinctNode = currentNode.next
        while nextDistinctNode is not None and nextDistinctNode.value == currentNode.value:
            nextDistinctNode = nextDistinctNode.next 
        
        currentNode.next = nextDistinctNode
        currentNode = nextDistinctNode
    return LinkedList

def main():
    linkedlist = LinkedList(value=1)
    linkedlist.next = LinkedList(value= 2)
    linkedlist.next.next = LinkedList(value= 2)
    linkedlist.next.next.next = LinkedList(value= 3)
    linkedlist.next.next.next.next = LinkedList(value= 3)
    linkedlist.next.next.next.next.next = LinkedList(value= 4)
    print()
    print()
    print(".............")
    remove_duplicates(linkedlist)
    linkedlist.print_list()
    # print(linkedlist.value)

if __name__ == '__main__':
    main()