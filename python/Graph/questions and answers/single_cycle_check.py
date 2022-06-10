def hasSingleCycle(array):
    currentIndex = 0
    elementsVisited = 0
    while elementsVisited < len(array):
        if elementsVisited > 0 and currentIndex == 0:
            return False
        elementsVisited += 1
        currentIndex = getNextIndex(currentIndex, array)
    return currentIndex == 0


def getNextIndex(currentIndex, array):
    jump = array[currentIndex]
    nextIndex = (currentIndex + jump) % len(array)
    return nextIndex if nextIndex >= 0 else nextIndex + len(array)


# BRUTE FORCE APPROACH
def circularArrayLoop(nums):
    n, visited = len(nums), set()
    for i in range(n):
        if i not in visited:
            local_s = set()
            while True:
                if i in local_s:
                    return True
                if i in visited:
                    break
                visited.add(i)
                local_s.add(i)
                prev, i = i, (i + nums[i]) % n
                if prev == i or (nums[i] > 0) != (nums[prev] > 0):
                    break
    return False


def main():
    custom_list = [2, 3, 1, -4, -4, -1]
    cl = [1, 2, 1, -3]
    ku = [2, -1, 1, 2, 2]
    nums = [-1, 2]
    print(hasSingleCycle(custom_list))
    print(hasSingleCycle(cl))
    print(hasSingleCycle(ku))
    print()
    print(circularArrayLoop(ku))
    print(circularArrayLoop(nums))


if __name__ == "__main__":
    main()
