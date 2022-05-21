# O(1) T, O(N) S
class Binarytree:
    def __init__(self, size) -> None:
        self.customList = size * [None]
        self.lastUsedIndex = 0
        self.maxSize = size

    # O(1) T, S
    def insert(self, value):
        if self.lastUsedIndex + 1 == self.maxSize:
            return "List is full"
        self.customList[self.lastUsedIndex + 1] = value
        self.lastUsedIndex += 1
        return "Inserted"
     # O(N) T, O(1) S
    def search(self, nodeValue):
        for i in range(len(self.customList)):
            if self.customList[i] == nodeValue:
                return "success"
        return "Not found"
    # O(n) T, S
    def preorder(self, index):
        if index > self.lastUsedIndex:
            return
        print(self.customList[index])
        self.preorder(index * 2)
        self.preorder(index * 2 + 1)
    # O(n) T, S
    def inorder(self, index):
        if index > self.lastUsedIndex:
            return
        self.inorder(index * 2)
        print(self.customList[index])
        self.inorder(index * 2 + 1)
    # O(n) T, S
    def postorder(self, index):
        if index > self.lastUsedIndex:
            return
        self.postorder(index * 2)
        self.postorder(index * 2 + 1)
        print(self.customList[index])
    # O(n) T, O(1)S
    def levelorder(self, index):
        try:
            for i in range(index, self.lastUsedIndex + 1):
                print(self.customList[i])
        except (ValueError, RuntimeError, TypeError, NameError, SyntaxError, AttributeError) as err:
            print(f"Oops!... traversing failed. List is empty")
        # finally:
        #     print("These are all the elements in the list")

    # O(n) T, O(1) S
    def deleteAny(self, value):
        if self.lastUsedIndex == 0:
            return "There is not any node to delete"
        for i in range(1, self.lastUsedIndex + 1):
            if self.customList[i] == value:
                self.customList[i] = self.customList[self.lastUsedIndex]
                self.customList[self.lastUsedIndex] = None
                self.lastUsedIndex -= 1
                return "deleted"
    # O(1) T, S
    def deleteAll(self):
        self.customList = None
        return "deleted..."


newbt = Binarytree(8)
newbt.insert("Drinks")
newbt.insert("Hot")
newbt.insert("Cold")
newbt.insert("Tea")
newbt.insert("Coffee")

# print(newbt.customList)
# print(".............search.............")
# print(newbt.search("tae"))

print("......preorder......")
newbt.preorder(1)
print("......inorder.......")
newbt.inorder(1)
print(".......postorder.......")
newbt.postorder(1)
print("......levelorder.......")
newbt.levelorder(1)
print('......delete Any......')
newbt.deleteAny("Hot")
newbt.levelorder(1)
print("......delete All......")
print(newbt.deleteAll())
newbt.levelorder(1)
