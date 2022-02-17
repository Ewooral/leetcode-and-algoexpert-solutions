""" 
Given two strings s1 and s2, return true if s2 contains a 
permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

 

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false
 

Constraints:

1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters.
"""


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        d = {'a': 2, 'b': 3, 'c': 5, 'd': 7, 'e': 11, 'f': 13, 'g': 17, 'h': 19, 'i': 23, 'j': 29, 'k': 31, 'l': 37, 'm': 41,
             'n': 43, 'o': 47, 'p': 53, 'q': 59, 'r': 61, 's': 67, 't': 71, 'u': 73, 'v': 79, 'w': 83, 'x': 89, 'y': 97, 'z': 101}

        product = 1
        for x in s1:
            product *= d[x]

        windowProduct = 1
        for x in s2[:len(s1)]:
            windowProduct *= d[x]

        if windowProduct == product:
            return True

        nextchar = len(s1)
        firstchar = 0
        while nextchar < len(s2):
            windowProduct = windowProduct // d[s2[firstchar]]
            windowProduct *= d[s2[nextchar]]
            if windowProduct == product:
                return True
            nextchar += 1
            firstchar += 1
        return False

solution = Solution()
print(solution.checkInclusion("ab", "eidbaooo"))