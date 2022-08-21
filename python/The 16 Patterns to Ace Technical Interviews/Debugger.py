def findContentChildren( g, s):
    g = sorted(g)
    s = sorted(s)
    ans, i, j = 0, 0, 0
    while i < len(s) and j < len(g):
        if s[i] >= g[i]:
            ans += 1
            i += 1
            j += 1
        else:
            i += 1
    return ans

print(findContentChildren([1,2,3], [1,1]))
print(findContentChildren([1,2], [1,2,3]))