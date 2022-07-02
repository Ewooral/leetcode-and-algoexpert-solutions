class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.endOfString = False


# O(N) T, S
def insertString(current, word):
    for ch in word:
        node = current.children.get(ch)
        if node is None:
            node = TrieNode()
            current.children.update({ch: node})
        current = node
    current.endOfString = True
    print("Successfully inserted!")


# O(m) T, O(1) S
def searchString(currentNode, word):
    for ch in word:
        node = currentNode.children.get(ch)
        if node is None:
            return False
        currentNode = node
    # return True if currentNode.endOfString else False
    return currentNode.endOfString


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

    if currentNode.endOfString is True:
        deleteString(currentNode, word, index + 1)
        return False

    cannotDelete = deleteString(currentNode, word, index + 1)
    if cannotDelete is True:
        root.children.pop(ch)
        return "Cannot Delete"
    else:
        return "Deleted Successfully!"


nTrie = TrieNode()


print("...create...")
insertString(nTrie,"App")
insertString(nTrie, "Appl")
print("...delete...")
print(deleteString(nTrie, "App", 0))
print("...search...")
print(searchString(nTrie, "Appl"))
print(searchString(nTrie, "App"))
print(nTrie)


