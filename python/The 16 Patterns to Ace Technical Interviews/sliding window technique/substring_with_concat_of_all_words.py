"""
SUBSTRING WITH CONCATENATION OF ALL WORDS
Hard
You are given a string s and an array of strings words of the same length.
Return all starting indices of substring(s) in s that is a concatenation of
each word in words exactly once, in any order, and without any intervening characters.
You can return the answer in any order.
Example 1:
Input: s = “barfoothefoobarman”, words = [“foo”,“bar”] Output: [0,9] Explanation:
Substrings starting at index 0 and 9 are “barfoo” and “foobar” respectively.
The output order does not matter, returning [9,0] is fine too.
Example 2:
Input: s = “wordgoodgoodgoodbestword”, words = [“word”,“good”,“best”,“word”] Output: []
Example 3:
Input: s = “barfoofoobarthefoobarman”, words = [“bar”,“foo”,“the”] Output: [6,9,12]
Constraints:
1 <= s.length <= 104
1 <= words.length <= 5000
1 <= words[i].length <= 30
s and words[i] consist of lowercase English letters.
"""

from typing import List


# Approach 1
def findSubstring(s: str, words: List[str]) -> List[int]:
    # join words together, find length of total
    lenWords = len("".join(words))
    # empty array
    ansArr = []

    # loop thru words- skip last bit, coz words can't fit if len of rem string is less than words
    for i in range((len(s) - lenWords) + 1):
        # clumsy chunking method
        # don't think i need to change it to string first
        str = s[i:i + lenWords]
        n = len(words[0])
        chunk = [str[i:i + n] for i in range(0, len(str), n)]
        # new empty array
        tempArr = []
        # loop thru words
        for j in words:
            # if the word is not in chunk
            if j not in chunk:
                # clear the temp array
                tempArr.clear()
                # next iteration (all words must be in chunk)
                break
            # add i to tempArr once only
            if j in chunk and len(tempArr) < 1:
                tempArr.append(i)
                # remove j (to check for dups)
                chunk.remove(j)
            # no point adding i to temp arr again
            elif j in chunk and len(tempArr) >= 1:
                # just remove the chunk
                chunk.remove(j)

        if len(tempArr) > 0:
            ansArr.append(tempArr[0])
    return ansArr


words = ["foo", "bar"]
s = "barfoothefoobarman"
print(findSubstring(s, words))


# Python3 program to calculate the starting indices
# of substrings inside S which contains all the
# words present in List L.

# Returns an integer vector consisting of starting
# indices of substrings present inside the string S
def findSubStringIndices(s, L):
    # Number of a characters of a word in list L.
    size_word = len(L[0])

    # Number of words present inside list L.
    word_count = len(L)

    # Total characters present in list L.
    size_L = size_word * word_count

    # Resultant vector which stores indices.
    res = []

    # If the total number of characters in list L
    # is more than length of string S itself.
    if size_L > len(s):
        return res

    # Map stores the words present in list L
    # against it's occurrences inside list L
    hash_map = dict()

    for i in range(word_count):
        if L[i] in hash_map:
            hash_map[L[i]] += 1
        else:
            hash_map[L[i]] = 1

    for i in range(0, len(s) - size_L + 1, 1):
        temp_hash_map = hash_map.copy()
        j = i
        count = word_count

        # Traverse the substring
        while j < i + size_L:

            # Extract the word
            word = s[j:j + size_word]

            # If word not found or if frequency of
            # current word is more than required simply break.
            if (word not in hash_map or
                    temp_hash_map[word] == 0):
                break

            # Else decrement the count of word
            # from hash_map
            else:
                temp_hash_map[word] -= 1
                count -= 1
            j += size_word

        # Store the starting index of that substring
        # when all the words in the list are in substring
        if count == 0:
            res.append(i)
    return res


# Driver Code
if __name__ == "__main__":
    s = "barfoothefoobarman"
    L = ["foo", "bar"]
    indices = findSubStringIndices(s, L)

    print(*indices)

# This code is contributed by
# sanjeev2552
