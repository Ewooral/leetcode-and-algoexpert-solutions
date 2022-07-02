# A simple Python program to
# find sum of diagonals
# This code takes O(n ^ 2) time and O(1) auxiliary space
# ................................................

def printDiagonalSums(mat, n):
    principal = 0
    secondary = 0
    for i in range(0, n):
        for j in range(0, n):

            # Condition for principal diagonal
            if i == j:
                principal += mat[i][j]

            # Condition for secondary diagonal
            if (i + j) == (n - 1):
                secondary += mat[i][j]

    print("Principal Diagonal:", principal)
    print("Secondary Diagonal:", secondary)


# ................................................


# Driver code
a = [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [1, 2, 3, 4],
     [5, 6, 7, 8]]
printDiagonalSums(a, 4)

# This code is contributed
# by ihritik

# SECOND APPROACH 
# This code takes O(n) time and O(1) auxiliary space
# A simple Python3 program to find
# sum of diagonals


def printDiagonalSums2(mat, n):
    principal = 0
    secondary = 0
    for i in range(0, n):
        principal += mat[i][i]
        secondary += mat[i][n - i - 1]

    print("Principal Diagonal:", principal)
    print("Secondary Diagonal:", secondary)


# Driver code
a = [[1, 2, 3],
     [5, 6, 7],
     [1, 2, 3]
     ]
printDiagonalSums2(a, 3)

# This code is contributed
# by ihritik
