from typing import List


print("..........")
class Solution:
    def remove_duplicate(self, s): # where s is a string 
        c = []
        for i in s:
            if i not in c: 
                c.append(i)
        return "".join(c)

# T = O(n), S = O(n)
dupSol = Solution()
print(dupSol.remove_duplicate("GodisGoodAlltheTime Yesa Sir!"))


# Example of using the string join method or function
Languages = ['Python', 'CSharp', 'JavaScript', 'AngularJS']
token = ', '
print(token.join(Languages))

Chars = ['a', 'g', 'i', 'l', 'e', ' ', 's', 'c', 'r', 'u', 'm']
token = ''
print(token.join(Chars))



print("............")
def remove_dup(string):
    already_added = {}
    for char in string:
        if already_added.__contains__(char):
            continue
        already_added[char] = 0
    return "".join(already_added.keys())

print(remove_dup("abedipeleisalegend"))


print(".............")
def has_duplicates(integers: list[int]) -> str:
    already_added = {}
    if len(integers) < 1:
        return "Integer list is empty"
    for elem in integers:
        if type(elem) == str:
            return "Strings are not allowed!"
        if elem in already_added:
            return "YES!"
        else:
            already_added[elem] = True
    return "NO!"

print(has_duplicates([2, 4, "2", 5]))
print(has_duplicates([2, 4, 5, 1, 3, 4, 9]))
print(has_duplicates([]))


def freqElem(nums: List[int]) -> dict:
    frequency = 0
    counted = {}
    nums.sort()
    print(nums.count(6))
    for num in nums:
        if num in counted:
            frequency += 1
        else:
            frequency = 1
        counted[num] = frequency
        print(num, frequency)
    return counted


print(freqElem([1, 3, 2, 1, 1, 3, 3, 5, 1, 1, 5, 1]))

'''
Frequency{1: 6, 2: 1, 3: 3, 5: 2} 
'''