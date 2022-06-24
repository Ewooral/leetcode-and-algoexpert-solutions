from sys import getrecursionlimit, setrecursionlimit



def fibonacci(n, memo={}):
    print("fibononacci", "(", n, ")", sep="", end=", ")
    def setLimit():
        return setrecursionlimit(200000)
    setLimit()
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n not in memo:
        memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    return memo[n]
    


def main():
    print(fibonacci(8, memo={}))
    # 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 
    # 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229
if __name__ == '__main__':
    main()