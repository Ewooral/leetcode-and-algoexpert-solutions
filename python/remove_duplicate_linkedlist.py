""" 
REMOVE DUPLICATES FROM LINKED LIST

You're given the head of a singly linked list whose nodes are in sorted order
with respect to their values. Write a function that returns a modified version of the
Linked list that doesn't contain any nodes with duplicate values.
The linked list should be modified in place(i.e. you shouldn't create
a brand new list), and the modified list should still have its nodes sorted with respect to
their values. 

Each Linked list node has an interger VALUE as well as a NODE pointer NEXT 
pointing to the next node in the linked list or NULL/None if there are no more nodes.

Sample Input:
1 -> 1 -> 2 -> 3 -> 3 -> 4 -> 4 -> 5

currentNode = head 
temp = currentNode.next.next
currentNode.next = temp

 
"""
class LinkeList:
    def __init__(self, value):
        self.value = value
        self.next = None
    
def remove_duplicates_from_linked_list(linkedlist):
    current_node = linkedlist
    while current_node is not None:
        next_distinct_node = current_node.next
        while next_distinct_node is not None and next_distinct_node.value == current_node.value
        # next_distinct_node = next_distinct_node.next
