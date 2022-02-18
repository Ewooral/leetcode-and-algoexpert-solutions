import json
def stringToListNode(input):
    # Generate list from the input
    numbers = json.loads(input)

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr


def prettyPrintLinkedList(node):
    import sys
    while node and node.next:
        sys.stdout.write(str(node.val) + "->")
        node = node.next

    if node:
        print(node.val)
    else:
        print("Empty LinkedList")


def main():
    import sys

    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            node = stringToListNode(line)
            prettyPrintLinkedList(node)
        except StopIteration:
            break


# if __name__ == '__main__':
#     main()
main()