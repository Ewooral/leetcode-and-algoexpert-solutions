def factorial(n):
    assert n >= 0 and int(n) == n, 'Only positive integers are accepted'
    if n in [0, 1]:
        return 1
    else:
        return n * factorial(n-1)


print(factorial(4))
# print(factorial(0))
# print(factorial(1))
# # print(factorial(-10))
