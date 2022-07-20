def search_in_sorted_matrix(arr, num):
    row = 0
    col = len(arr[0]) - 1
    while not_out_of_bounds(row, col, arr):
        # print(arr[row][col])
        if arr[row][col] > num:
            col -= 1
        elif arr[row][col] < num:
            row += 1
        else:
            return [row, col]
    return [-1, -1]


def not_out_of_bounds(row, col, arr):
    return row < len(arr) and col >= 0


def main():
    arr = [
        [1, 4, 7, 12, 15, 1000],
        [2, 5, 19, 31, 32, 1001],
        [3, 8, 24, 33, 35, 1002],
        [40, 41, 42, 44, 45, 1003],
        [99, 100, 103, 106, 128, 1004]
    ]
    num = 44
    num1 = 1004
    num2 = 2000
    print(search_in_sorted_matrix(arr, num))
    print(search_in_sorted_matrix(arr, num1))
    print(search_in_sorted_matrix(arr, num2))


if __name__ == '__main__':
    main()
