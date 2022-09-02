points = [2.3, 3.5, 4.4, 7.8]
boundary = [0, 5, 10]
p = [81, 15, 4, 12, 1]
b = [16, 20, 90]

def pbB(p, b):
    i = j = 0
    res, lengthP, lengthB = [], len(p), len(b)
    beg= b[j]
    while j < lengthB:
        count = 0
        poi, bou, nex = p[i], b[j], b[j+1]
        while p[i] < b[j] and p[i] < b[j+1]:
            i += 1
        while i < lengthP and b[j] < p[i] < b[j + 1]:
            count += 1
            i += 1
        while i < lengthP and p[i] < b[j] and p[i] < b[j + 1]:
            j += 1
        if not count == 0:
            res.append(count)
        j += 1

    return res

pbB(p, b)
