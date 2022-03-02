class Solution:

    #Function to reverse words in a given string.
    # T = O(1), S = O(1)
    def reverse_words(self, S):
        #Split the string into words.
        words = S.split()
        #Reverse the words.
        words = words[::-1]
        #Join the words back into a string.
        return ' '.join(words)

reverse = Solution()
print(reverse.reverse_words("The quick brown fox jumps over the lazy dog"))