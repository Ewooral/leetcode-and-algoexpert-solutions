# Python 3 program of the above approach
ROW = 3
COL = 3

# Initialize direction vectors
dRow = [0, 1, 0, -1]
dCol = [-1, 0, 1, 0]
vis = [[False for i in range(3)] for j in range(3)]

# Function to check if mat[row][col]
# is unvisited and lies within the
# boundary of the given matrix


def isValid(row, col):
    global ROW
    global COL
    global vis

    # If cell is out of bounds
    if (row < 0 or col < 0 or row >= ROW or col >= COL):
        return False

    # If the cell is already visited
    if (vis[row][col]):
        return False

    # Otherwise, it can be visited
    return True

# Function to perform DFS
# Traversal on the matrix grid[]


def DFS(row, col, grid):
    global dRow
    global dCol
    global vis

    # Initialize a stack of pairs and
    # push the starting cell into it
    st = []
    st.append([row, col])

    # Iterate until the
    # stack is not empty
    while (len(st) > 0):
        # Pop the top pair
        curr = st[len(st) - 1]
        st.remove(st[len(st) - 1])
        row = curr[0]
        col = curr[1]

        # Check if the current popped
        # cell is a valid cell or not
        if (isValid(row, col) == False):
            continue

        # Mark the current
        # cell as visited
        vis[row][col] = True

        # Print the element at
        # the current top cell
        print(grid[row][col], end=" ")

        # Push all the adjacent cells
        for i in range(4):
            adjx = row + dRow[i]
            adjy = col + dCol[i]
            st.append([adjx, adjy])


# Driver Code
if __name__ == '__main__':
    grid = [[-1, 2, 3],
            [0, 9, 8],
            [1, 0, 1]]

    # Function call
    DFS(0, 0, grid)


