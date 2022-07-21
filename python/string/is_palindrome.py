def is_palindrome(s):
    l = 0
    r = len(s) - 1
    while l < r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True


def is_palindrome1(s):
    n = len(s)
    if n <= 1:
        return True
    else:
        return (s[0] == s[n - 1]) and is_palindrome(s[1:n - 1])


s = "abcdcba"
b = "dwufjkuw"
print(is_palindrome("bab"))
print(is_palindrome(b))
print(is_palindrome(s))
