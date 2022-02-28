def solve(A, result=0):
    for i in range(len(A)):
        for j in range(len(A)):
            if A[i] == A[j]:
                result = max(result, abs(i - j))

    return result


print(solve([4, 6, 2, 2, 6, 6, 1]))


def solving(a, result = 0):
    hash = {}
    for i, j in range(len(a)):
        current = a[i]
        next_item = a[j] + 1

        hash[current] = True
        if current == hash[current]:
            result = max(result, abs(i - j))
        print(hash)
    return result
    

print(solving([4, 6, 2, 2, 6, 6, 1]))
