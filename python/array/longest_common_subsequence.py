""" 
Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.

 

Example 1:

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.
Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.
 

Constraints:

1 <= text1.length, text2.length <= 1000
text1 and text2 consist of only lowercase English characters.
"""


def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    text1 = "0" + text1
    text2 = "0" + text2

    dp = [[0] * len(text2) for i in range(0, len(text1))]
    max_value = 0

    for i in range(1, len(text1)):
        for j in range(1, len(text2)):
            if text1[i] == text2[j]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

            max_value = max(max_value, dp[i][j])

    return max_value


# # Solution 1 (Recursive - Top Down - Memoization)


class Solution:
    def dp(self, text1, text2, s1, s2, lookup):
        if s1 == len(text1) or s2 == len(text2):
            return 0
        if lookup[s1][s2] == -1:
            if text1[s1] == text2[s2]:
                lookup[s1][s2] = 1 + self.dp(text1, text2, s1+1, s2+1, lookup)
            else:
                lookup[s1][s2] = max(self.dp(
                    text1, text2, s1+1, s2, lookup), self.dp(text1, text2, s1, s2+1, lookup))
        return lookup[s1][s2]

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        return self.dp(text1, text2, 0, 0, [[-1 for _ in range(len(text2))] for _ in range(len(text1))])


# # Solution 2 (Iterative - Bottom Up - Tabulation)


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[-1 for _ in range(len(text2) + 1)]
              for _ in range(len(text1) + 1)]
        for i in range(len(text1)+1):
            dp[i][0] = 0
        for j in range(len(text2)+1):
            dp[0][j] = 0
        for i in range(1, len(text1)+1):
            for j in range(1, len(text2)+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
#                 else:
#                     dp[i][j] = max(dp[i][j-1], dp[i-1][j])
#         return dp[-1][-1]
