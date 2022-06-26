def zigzagTraverse(arr):
    height = len(arr) - 1
    width  = len(arr) - 1
    result = []
    row = 0
    col = 0
    goingDown = True
    while not isOutOfBounds(row, col, height, width):
        result.append(arr[row][col])
        if goingDown:
            if col == 0 or row == height:
                goingDown = False
                if row == height: # last row
                    col += 1
                else:
                    row += 1
            else:
                row += 1
                col -= 1
        else:
            if row == 0 or col == width:
                goingDown = True
                if col == width:
                    row += 1
                else:
                    col += 1
            else:
                row -= 1
                col += 1
    return result


def isOutOfBounds(row, col, height, width):
    return row < 0 or row > height or col < 0 or col > width


def main():
    _2d_array = [
        [1, 3, 4, 10],
        [2, 5, 9, 11],
        [6, 8, 12, 15],
        [7, 13, 14, 16],
    ]
    _2d_arrayA = [
        [1, 3, 4],
        [2, 5, 8],
        [6, 7, 9]
    ]
    print(zigzagTraverse(_2d_array))
    print(zigzagTraverse(_2d_arrayA))


if __name__ == '__main__':
    main()