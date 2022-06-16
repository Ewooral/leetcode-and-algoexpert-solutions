from functools import reduce
from sys import setrecursionlimit


def reLimit():
    return setrecursionlimit(200000)


def count_down(n):
    print(n)
    if n == 0:
        return
    else:
        count_down(n - 1)
count_down(10)


print("...........")
def countDown(n):
    while n >= 0:
        print(n)
        n -= 1
countDown(10)


print("........")
def factorial(n):
    return_value = 1
    for i in range(2, n + 1):
        return_value *= i
    return return_value
print(factorial(15))


print("........")
def factorial(n):
    return reduce(lambda x, y: x * y, range(1, n + 1) or [1])
print(factorial(15))


print("........")
def fact(n, hash_table={}):
    reLimit()  # this sets the recursive limit to 200
    if n <= 0:
        return 1
    if n not in hash_table:
        hash_table[n] = n * fact(n - 1)
    return hash_table[n]
print(fact(15))


# NB... Check for the RUNTIME of the three factorial functions above, in the test package

names = [
    "Adam",
    ["Bob",["Chet", "Cat",],"Barb","Bert"],
    "Alex",
    ["Bea","Bill"],
    {"Elijah": 20},
    "Ann"
]
print(names)

print("..........")
def Prin(name):
    count = 0
    for i in name:
        if isinstance(i, list):
            count += Prin(i)
        else:
            count += 1
    return count
print(Prin(names))



# print(isinstance(names[0], list))
print(".................")
def traverse(names):
    for name in names:
        # if isinstance(name, list): OR
        if type(name) is list or type(name) is dict:
            traverse(name)
        else: print(name)

traverse(names)

