class Solution:

    #Function to reverse words in a given string.
    def reverse_words(self, S):
       l = []
       l = S.split('.')
       l = l[::-1]
       l = '.'.join(l)
       return l

first_solution = Solution()
print(first_solution.reverse_words("The cat in the hat"))
