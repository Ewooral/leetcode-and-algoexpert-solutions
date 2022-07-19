# Brute Force Approach
# O(n^2)T, O(n)S
def right_smaller_than(arr):
    result = []
    for i in range(len(arr)):
        count = 0
        current = arr[i]
        for j in range(i + 1, len(arr)):
            Next = arr[j]
            if current > Next:
                count += 1
        result.append(count)
    return result


# Optimal Approach
# O(NlogN)T, O(N)S
def rightSmallerThan(arr):
    if len(arr) == 0:
        return []
    rightSmallerCounts = arr[:]
    lastIdx = len(arr) - 1
    rightSmallerCounts[lastIdx] = 0
    for i in reversed(range(len(arr) - 1)):
        insert(BST, arr[i], i, rightSmallerCounts, nS=0)
    return rightSmallerCounts


class SpecialBST:
    def __init__(self, value=None):
        self.value = value
        self.leftSubtreeSize = 0
        self.left = None
        self.right = None


BST = SpecialBST(0)


# log(n)T, S
def insert(BST, value, Idx, rightSmallerCounts, nS=0):
    # nS = number smaller at insert time
    if value < BST.value:
        BST.leftSubtreeSize += 1
        if BST.left is None:
            BST.left = SpecialBST(value)
            rightSmallerCounts[Idx] = nS
        else:
            insert(BST.left, value, Idx, rightSmallerCounts, nS)
    else:
        nS += BST.leftSubtreeSize
        if value > BST.value:
            nS += 1
        if BST.right is None:
            BST.right = SpecialBST(value)
            rightSmallerCounts[Idx] = nS
        else:
            insert(BST.right, value, Idx, rightSmallerCounts, nS)


def main():
    arr4 = [8, 5, 11, -1, 3, 4, 2]
    print(right_smaller_than(arr4))
    print(rightSmallerThan(arr4))


if __name__ == '__main__':
    main()
