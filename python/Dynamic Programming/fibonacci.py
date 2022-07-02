from sys import getrecursionlimit, setrecursionlimit


# Top down Approach
def fibonacci(n, memo=None):
    if memo is None:
        memo = {}
    print("fibononacci", "(", n, ")", sep="", end=", ")
    if n == 1:
        return 0
    if n == 2:
        return 1
    if n not in memo:
        memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    return memo[n]


# bottom up Approach
def fibonacci_I(n):
    tb = [0, 1]
    for i in range(2, n + 1):
        tb.append(tb[i - 1] + tb[i - 2])
    return tb[n - 1]


def main():
    print(fibonacci(5, memo={}))
    print(fibonacci_I(5))
    # 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 
    # 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229


if __name__ == '__main__':
    main()