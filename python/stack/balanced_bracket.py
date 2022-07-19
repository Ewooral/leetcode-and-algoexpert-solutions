from collections import deque

print(".....APPROACH I")


def balancedBrackets(string):
    openingBrackets = "([{"
    closingBrackets = ")]}"
    matchingBrackets = {")": "(", "]": "[", "}": "{"}
    stack = []
    for char in string:
        if char in openingBrackets:
            stack.append(char)
        elif char in closingBrackets:
            if len(stack) == 0:
                return False
            if stack[-1] == matchingBrackets[char]:
                stack.pop()
            else:
                return False

    return len(stack) == 0


print(balancedBrackets("(abc)"))
print(balancedBrackets("(abc"))
print(balancedBrackets(""))
print(balancedBrackets("{(abc}"))

print(".....APPROACH II")


# Approach II
def isBalanced(someString):
    if len(someString) < 1:
        return True
    stack = deque()
    for c in someString:
        if c == "(":
            stack.appendleft(c)
        elif c == ")":
            if len(stack) < 1 or stack[0] != "(":
                return False
            else:
                stack.popleft()
    if len(stack) > 0:
        return False
    return True


print(isBalanced("(abc)"))
print(isBalanced("{(abc"))
print(isBalanced(""))
print(isBalanced("{(abc}"))
