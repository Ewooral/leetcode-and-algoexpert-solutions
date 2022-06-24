# Python program for Boggle game
class TrieNode:

    # Trie node class
    def __init__(self):
        self.children = [None] * 26

        # isEndOfWord is True if node represent the end of the word
        self.isEndOfWord = False


M = 3
N = 3


class Boogle:

    # Trie data structure class
    def __init__(self):
        self.root = self.getNode()

    def getNode(self):

        # Returns new trie node (initialized to NULLs)
        return TrieNode()

    def _charToIndex(self, ch):

        # private helper function
        # Converts key current character into index
        # use only 'A' through 'Z' and upper case
        return ord(ch) - ord('A')

    def insert(self, key):

        # If not present, inserts key into trie
        # If the key is prefix of trie node,
        # just marks leaf node
        pCrawl = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])

            # if current character is not present
            if not pCrawl.children[index]:
                pCrawl.children[index] = self.getNode()
            pCrawl = pCrawl.children[index]
        # print('h', self.root.children)

        # mark last node as leaf
        pCrawl.isEndOfWord = True


def is_Safe(i, j, vis):
    return 0 <= i < M and 0 <= j < N and not vis[i][j]


def search_word(root, boggle, i, j, vis, string):
    if root.isEndOfWord:
        print(string)

    if is_Safe(i, j, vis):
        vis[i][j] = True
        for K in range(26):
            if root.children[K] is not None:
                ch = chr(K + ord('A'))

                # Recursively search reaming character of word
                # in trie for all 8 adjacent cells of boggle[i][j]
                if is_Safe(i + 1, j + 1, vis) and boggle[i + 1][j + 1] == ch:
                    search_word(root.children[K], boggle,
                                i + 1, j + 1, vis, string + ch)
                if is_Safe(i, j + 1, vis) and boggle[i][j + 1] == ch:
                    search_word(root.children[K], boggle,
                                i, j + 1, vis, string + ch)
                if is_Safe(i - 1, j + 1, vis) and boggle[i - 1][j + 1] == ch:
                    search_word(root.children[K], boggle,
                                i - 1, j + 1, vis, string + ch)
                if is_Safe(i + 1, j, vis) and boggle[i + 1][j] == ch:
                    search_word(root.children[K], boggle,
                                i + 1, j, vis, string + ch)
                if is_Safe(i + 1, j - 1, vis) and boggle[i + 1][j - 1] == ch:
                    search_word(root.children[K], boggle,
                                i + 1, j - 1, vis, string + ch)
                if is_Safe(i, j - 1, vis) and boggle[i][j - 1] == ch:
                    search_word(root.children[K], boggle,
                                i, j - 1, vis, string + ch)
                if is_Safe(i - 1, j - 1, vis) and boggle[i - 1][j - 1] == ch:
                    search_word(root.children[K], boggle,
                                i - 1, j - 1, vis, string + ch)
                if is_Safe(i - 1, j, vis) and boggle[i - 1][j] == ch:
                    search_word(root.children[K], boggle,
                                i - 1, j, vis, string + ch)
                vis[i][j] = False


def char_int(ch):
    # private helper function
    # Converts key current character into index
    # use only 'A' through 'Z' and upper case
    return ord(ch) - ord('A')


def findWords(boggle, root):
    # Mark all characters as not visited
    visited = [[False for i in range(N)] for i in range(M)]

    pChild = root

    string = ""

    # traverse all matrix elements
    for i in range(M):
        for j in range(N):
            # we start searching for word in dictionary
            # if we found a character which is child
            # of Trie root
            if pChild.children[char_int(boggle[i][j])]:
                # print('h')
                string = string + boggle[i][j]
                search_word(pChild.children[char_int(boggle[i][j])],
                            boggle, i, j, visited, string)
                string = ""


dictionary = ["GEEKS", "FOR", "QUIZ", "GEE"]

# root Node of trie
t = Boogle()

# insert all words of dictionary into trie
n = len(dictionary)
for i in range(n):
    t.insert(dictionary[i])
root = t.root
boggle = [['G', 'I', 'Z'],
          ['U', 'E', 'K'],
          ['Q', 'S', 'E']]

# print(root.children)
findWords(boggle, root)

