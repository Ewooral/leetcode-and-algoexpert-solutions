def diagonal_sum( mat):
    n = len(mat)

    mid = n // 2

    summation = 0

    for i in range(n):
        # primary diagonal
        summation += mat[i][i]

        # secondary diagonal
        summation += mat[n-1-i][i]

    if n % 2 == 1:
        # remove center element (repeated) on odd side-length case
        summation -= mat[mid][mid]

    return summation


# Driver code
a = [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [1, 2, 3, 4],
     [5, 6, 7, 8]]

# 1 + 6 + 3 + 8 + 4 + 7 + 7 = 36


b = [[1, 2, 3],
     [5, 6, 7],
     [1, 2, 3]
     ]
# 1 + 6 + 3 + 3 + 1 = 14

print(diagonal_sum(a))
print(diagonal_sum(b))
