'''
Design a data structure that supports adding new words and finding if 
a string matches any previously added string.

Implement the WordDictionary class:

WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can be matched 
later.
bool search(word) Returns true if there is any string in the data
structure that matches word or false otherwise. word may contain
dots '.' where dots can be matched with any letter.


Example:

Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
[null,null,null,null,false,true,true,true]

Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True

Constraints:

1 <= word.length <= 500
word in addWord consists lower-case English letters.
word in search consist of  '.' or lower-case English letters.
At most 50000 calls will be made to addWord and search.

Data Structure Trie
This article introduces the data structure trie. 
It could be pronounced in two different ways: as 
"tree" or "try". Trie which is also called a digital
 tree or a prefix tree is a kind of search ordered tree data structure 
 mostly used for the efficient dynamic add/search operations with the 
 strings.

Trie is widely used in real life: autocomplete search, spell checker, 
T9 predictive text, IP routing (longest prefix matching), some GCC 
containers.

'''

'''
There are two main types of trie interview questions:

S1. tandard Trie. Design a structure to dynamically add and search 
strings, for example

Add and Search Word.

Word Search II.

Design Search Autocomplete System.

2. Bitwise Trie. Design a structure to dynamically add binary strings 
and compute maximum/minimum XOR/AND/etc, for example

Maximum XOR of Two Number in an Array.


Why Trie and not HashMap

It's quite easy to write the solution using such data structures as 
hashmap or balanced tree.
'''

from collections import defaultdict
class WordDictionary:
    def __init__(self):
        self.d = defaultdict(set)

    def add_word(self, word: str) -> None:
        self.d[len(word)].add(word)
        return word

    def search(self, word: str) -> bool:
        m = len(word)
        for dict_word in self.d[m]:
            i = 0
            while i < m and (dict_word[i] == word[i] or word[i] == '.'):
                i += 1
            if i == m:
                return True
        return False


''' This solution passes all leetcode test cases, and formally has 
O(M⋅N) time complexity for the search, where M
is a length of the word to find, and N is the number of words. Although
this solution is not efficient for the most important practical use cases:

1. Finding all keys with a common prefix.
2. Enumerating a dataset of strings in lexicographical order.
3. Scaling for the large datasets. 
Once the hash table increases in size, there are a lot of hash collisions and the search 
time complexity could degrade to O(N2.M), where NN is the number of the inserted keys.
'''

# Trie could use less space compared to hashmap when storing 
# many keys with the same prefix. In this case, using trie has
#  only O(M⋅N) time complexity, 
# where M is the key length, and NN is the number of keys.

class WordDictionaries:
    def __init__(self):
         """
        Initialize your data structure here.
        """
         self.trie = {}
    def add_word(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        node = self.trie
        for ch in word:
            if not ch in node:
                node[ch] = {}
            node = node[ch]
        node['$'] = True

new_wordA = WordDictionaries()
new_wordB = WordDictionary()
A = new_wordB.add_word("samaritan")

print(A)
print(new_wordA.add_word('dad'))
print(new_wordB.add_word('.ad'))
print(new_wordB.add_word('b..') )

print(new_wordA.trie)
print(new_wordB.d)


