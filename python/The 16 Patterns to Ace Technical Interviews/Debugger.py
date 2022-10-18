from random import randint


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

        # the below code makes our linked list printable

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def __str__(self):
        values = [str(x.value) for x in self]
        return '->'.join(values)

    def add(self, value):
        if self.head is None:
            newNode = Node(value)
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
        return self.tail

    def generate(self, n, minValue, maxValue):
        self.head = None
        self.tail = None
        for i in range(n):
            self.add(randint(minValue, maxValue))
        return self

    def length(self):
        count = 0
        if self.head is None:
            return
        else:
            while self.head is not None:
                self.head = self.head.next
                count += 1
        return count

    def detect_loop(self):
        node = self.head
        hash_t = {}
        while node is not None:
            if node.value in hash_t:
                return "Loop has been detected!"
            hash_t[node.value] = True
            node = node.next
        return hash_t

    def find_duplicate(self):
        node = self.head
        left_p, Len = 0, self.length()
        while left_p < Len:
            next_node = node.next
            right_p = left_p + 1
            while right_p < Len:
                if node.value == next_node.value:
                    return "Duplicates detected!"
                next_node = next_node.next
                right_p += 1
            node = node.next
            left_p += 1
        return "No duplicates detected"


def main():
    ...


if __name__ == '__main__':
    main()
