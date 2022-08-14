"""
Algorithm

    Initialize some variables:
        n as the length of s.
        k as the length of words
        wordLength as the length of each word in words.
        substringSize as wordLength * k, which represents the size of each valid substring.
        wordCount as a hash table that tracks how many times a word occurs in words.

    Create a function check that takes a starting index i and returns if a valid substring starts at index i:
        Create a copy of wordCount to make use of for this particular index. Let's call it remaining. Also, initialize an integer wordsUsed which tracks how many matches we have found so far.
        Iterate starting from i. Iterate until i + substringSize - we know that each valid substring will have this size, so we don't need to go further. At each iteration, we will be checking for a word - and we know each word has a length of wordLength, so increment by wordLength each time.
        If the variable we are iterating with is j, then at each iteration, check for a word sub = s.substring(j, j + wordLength).
        If sub is in remaining and has a value greater than 0, then decrease its count by 1 and increase wordsUsed by 1. Otherwise, break out of the loop.
        At the end of it all, if wordsUsed == k, that means we used up all the words in words and have found a valid substring. Return true if so, false otherwise.

    Now that we have this function check, we can just check all possible starting indices. Because a valid substring has a length of substringSize, we only need to iterate up to n - substringSize. Build an array with all indices that pass check and return it.

Implementation

"""

import collections

def findSubstring( s, words):
    n = len(s)
    k = len(words)
    word_length = len(words[0])
    substring_size = word_length * k
    word_count = collections.Counter(words)

    def check(i):
        # Copy the original dictionary to use for this index
        remaining = word_count.copy()
        words_used = 0

        # Each iteration will check for a match in words
        for j in range(i, i + substring_size, word_length):
            sub = s[j: j + word_length]
            if remaining[sub] > 0:
                remaining[sub] -= 1
                words_used += 1
            else:
                break

        # Valid if we used all the words
        return words_used == k

    answer = []
    for i in range(n - substring_size + 1):
        if check(i):
            answer.append(i)

    return answer
def main():
    words = [["foo", "bar"], ["word", "good", "best", "word"], ['bar','foo', 'the']]
    s = ["barfoothefoobarman", "wordgoodgoodgoodbestword", "barfoofoobarthefoobarman"]
    print(findSubstring(s[0], words[0]))
    print(findSubstring(s[1], words[1]))
    print(findSubstring(s[2], words[2]))


if __name__ == '__main__':
    main()


