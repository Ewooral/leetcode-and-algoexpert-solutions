class Solution:
    def remove_duplicate(self, s): # where s is a string 
        c = []
        for i in s:
            if i not in c: 
                c.append(i)
        return " ".join(c)

# T = O(n), S = O(n)



# Example of using the string join method or function
Languages = ['Python', 'CSharp', 'JavaScript', 'AngularJS']
token = ', '
print(token.join(Languages))

Chars = ['a', 'g', 'i', 'l', 'e', ' ', 's', 'c', 'r', 'u', 'm']
token = ''
print(token.join(Chars))
