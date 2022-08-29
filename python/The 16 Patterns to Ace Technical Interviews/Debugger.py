def setZeroes(matrix):
    rows_to_zero = set()  # set to keep track rows to make zeros
    cols_to_zero = set()  # set to keep track columns to make zeros
    m = len(matrix)  # height
    n = len(matrix[0])  # weight
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:  # found a zero keep adding row and column to sets
                rows_to_zero.add(i)
                cols_to_zero.add(j)
#     in iteration 2 if we find thozse rows and columns make then zero
    for i in range(m):
        for j in range(n):
            if i in rows_to_zero:
                matrix[i][j] = 0
            if j in cols_to_zero:
                matrix[i][j] = 0
    return matrix


def main():
    f = [[1, 1, 1],
         [1, 0, 1],
#          [1, 1, 1]]
#     input = [[0, 1, 1, 2],
#              [6, 6, 0, 7],
#              [1, 1, 1, 2]]

    # print(setZeroes(f))


main()


