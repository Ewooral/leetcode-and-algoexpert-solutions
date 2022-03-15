def frequencySort(s):
#     """
#         :type s: str
#         :rtype: str
#         """
    dic = {}
    re = ""
    for i in s:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1

    out = sorted(dic, key=dic.get, reverse=True)

    for i in out:
        re += i*(dic[i])

    return re

print(frequencySort("tree"))
