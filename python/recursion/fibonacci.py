def fibonacci(n):
    # n should be greater than or equals to 0 and a positive integer
    assert n >= 0 and int(n) == n, 'Only positive integers are accepted'
    if n in [0, 1]:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


# print(fibonacci(12))
# print(fibonacci(0))
# print(fibonacci(1))
