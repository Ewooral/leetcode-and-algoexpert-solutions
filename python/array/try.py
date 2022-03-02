def solve(A, result=0):
    for i in range(len(A)):
        for j in range(len(A)):
            if A[i] == A[j]:
                result = max(result, abs(i - j))

    return result


print(solve([4, 6, 2, 2, 6, 6, 1]))





