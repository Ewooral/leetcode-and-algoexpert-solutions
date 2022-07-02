"""
You're given an array of products and a string searchWord.
Design a system that suggests at most three products names from products
after each character of searchWord is typed. 
Proposed products should have common prefix with searchWord. If there are more than
three products with a common prefix return the three lexicographically minimums products.
Return a list of lists of the suggested products after each character of searchWord is typed

Example 1
input : products = ["mobile", "mouse", "moneypot", "monitor", "mousepad"], searchWord = "mouse"
Output: [
["mobile", "moneypot", "monitor"],
["mobile", "moneypot", "monitor"],
["mouse", "mousepad"],
["mouse", "mousepad"],
["mouse", "mousepad"]
]
"""
# With two pointers, we always sort the list


def suggestedProducts(products, searchWord):
    res = []
    products.sort()
    l, r = 0, len(products) - 1
    for i in range(len(searchWord)):
        c = searchWord[i]

        # while still looping and the current product doesn't match the current prefix, i or
        # the current character in our current product doesn't match the
        # current character in the searchWord, ignore it and move to the next product

        while l <= r and len(products[l]) <= i or products[l][i] != c:
            l += 1
        while l <= r and len(products[r]) <= i or products[r][i] != c:
            r -= 1

        res.append([])

        # the number of words with a matching prefix
        remain = r - l + 1

        # iterate through the remaining words
        for j in range(min(3, remain)):
            res[-1].append(products[l + j])
    return res


def main():
    products = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
    searchWord = "mouse"
    print(suggestedProducts(products, searchWord))


if __name__ == '__main__':
    main()