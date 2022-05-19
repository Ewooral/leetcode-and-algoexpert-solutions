class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.endOfString = False

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()
    # O(N) T, S
    def insertString(self, word):
        current = self.root
        for i in word:
            ch = i
            node = current.children.get(ch)
            if node == None:
                node = TrieNode()
                current.children.update({ch:node}) 
            current = node
        current.endOfString = True
        print("Successfully inserted!")
    # O(m) T, O(1) S
    def searchString(self, word):
        currentNode = self.root
        for i in word:
            node = currentNode.children.get(i)
            if node == None:
                return False
            currentNode = node
        if currentNode.endOfString == True:
            return True
        else:
            return False 


def deleteString(root, word, index):
    ch = word[index]
    currentNode = root.children.get(ch)
    cannotDelete = False

    if len(currentNode.children) > 1:
        deleteString(currentNode, word, index + 1)
        return False

    if index == len(word) - 1:
        if len(currentNode.children) >= 1:
            currentNode.endOfString = False
            return False
        else:
            root.children.pop(ch)
            return True

    if currentNode.endOfString == True:
        deleteString(currentNode, word, index + 1)
        return False
    
    cannotDelete = deleteString(currentNode, word, index + 1)
    if cannotDelete == True:
        root.children.pop(ch)
        return True
    else:
        return False



newTrie = Trie()

print("...create...")
newTrie.insertString("App")
newTrie.insertString("Appl")
print("...delete...")
deleteString(newTrie.root, "App", 0)
print("...search...")
print(newTrie.searchString("Appl"))
print(newTrie.searchString("App"))