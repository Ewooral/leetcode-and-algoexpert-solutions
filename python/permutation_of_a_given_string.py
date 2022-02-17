import itertools

# T = O(n), S = O(n)
class Solution:
    def find_permutation(self, s):

        # Code here
        lst = []

        for i in itertools.permutations(s, len(s)):
            lst.append("".join(map(str, i)))
            lst.sort()

        return lst

Find_Permutation = Solution()
print(Find_Permutation.find_permutation("ABSG"))
print(len(Find_Permutation.find_permutation("ABSG")))

