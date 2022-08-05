''' 
You are given an array of strings products and a string searchWord.

Design a system that suggests at most three product names from products after each character of searchWord is typed.
Suggested products should have common prefix with searchWord. If there are more than
three products with a common prefix return the three lexicographically minimums products.

Return a list of lists of the suggested products after each character of searchWord is typed.

 

Example 1:

Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
Output: [
["mobile","moneypot","monitor"],
["mobile","moneypot","monitor"],
["mouse","mousepad"],
["mouse","mousepad"],
["mouse","mousepad"]
]
Explanation: products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"]
After typing m and mo all products match and we show user ["mobile","moneypot","monitor"]
After typing mou, mous and mouse the system suggests ["mouse","mousepad"]
Example 2:

Input: products = ["havana"], searchWord = "havana"
Output: [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]
Example 3:

Input: products = ["bags","baggage","banner","box","cloths"], searchWord = "bags"
Output: [["baggage","bags","banner"],["baggage","bags","banner"],["baggage","bags"],["bags"]]
 

Constraints:

1 <= products.length <= 1000
1 <= products[i].length <= 3000
1 <= sum(products[i].length) <= 2 * 104
All the strings of products are unique.
products[i] consists of lowercase English letters.
1 <= searchWord.length <= 1000
searchWord consists of lowercase English letters.
'''


class Solution(object):
    def suggested_products(self, products, search_word):
        products.sort()  # n(log n)
        res = []
        for i in range(len(search_word)):  # O(c)
            # products = [p for p in products if p[:i+1] == search_word[:i+1]]
            prod = []   # O(p)
            for p in products:  # O(w)
                s = p[:i + 1]
                y = search_word[:i + 1]
                if p[:i + 1] == search_word[:i + 1]:
                    prod.append(p)
            res.append(prod[:min(3, len(prod))])

        return res


# TEST
sol = Solution()
print(sol.suggested_products(["mobile", "mouse", "moneypot", "monitor", "mousepad"], "mouse"))
print(sol.suggested_products(["havana"], "havana"))
