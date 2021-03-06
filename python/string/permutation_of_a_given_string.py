""" 
Given a string S. The task is to print all permutations of a given string in lexicographically sorted order.

 

Example 1:

Input: ABC
Output:
ABC ACB BAC BCA CAB CBA
Explanation:
Given string ABC has permutations in 6 
forms as ABC, ACB, BAC, BCA, CAB and CBA .
Example 2:

Input: ABSG
Output:
ABGS ABSG AGBS AGSB ASBG ASGB BAGS 
BASG BGAS BGSA BSAG BSGA GABS GASB 
GBAS GBSA GSAB GSBA SABG SAGB SBAG 
SBGA SGAB SGBA
Explanation:
Given string ABSG has 24 permutations.
 

Your Task:  
You don't need to read input or print anything. Your task is to complete the function find_permutaion() which takes the string S as input parameter and returns a vector of string in lexicographical order.

 

Expected Time Complexity: O(n! * n)

Expected Space Complexity: O(n)

 

Constraints:
1 <= length of string <= 5
"""

import itertools

# T = O(n), S = O(n)
class Solution:
    def find_permutation(self, s, p):

        # Code here
        lst = []
        P = " ".join(p)
        for i in itertools.permutations(s, len(s)):
            print(itertools.permutations(s, len(s)))
            lst.append("".join(map(str, i)))
            lst.sort()
        if s not in lst:
            print(False, "") 
        else:
            print(True, "", s)
     

        return lst

Find_Permutation = Solution()
print(Find_Permutation.find_permutation("ab", "eidboaoo"))
# print(len(Find_Permutation.find_permutation("ABSG")))
# print(len(Find_Permutation.find_permutation("STACK")))
# print(Find_Permutation.find_permutation("ab"))
# print(len(Find_Permutation.find_permutation("ab")))



