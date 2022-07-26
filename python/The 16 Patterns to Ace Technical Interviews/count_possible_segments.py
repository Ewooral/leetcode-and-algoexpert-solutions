"""
Amazon warehouse has a group of n items of various weights lined up in a row.
A segment of contiguously placed items can be shipped together if and only if
the difference between the weights of the heaviest and lightest item differs
by at most k to avoid load imbalance.

Given the weights of the n items and an integer k, find the number of
segments of items that can be shipped together.

Constraint = max[i] - min[i] <= k

E.g.
weights = [1, 3, 6]
k = 3

Output  1 - 1 = 0 < k
        3 - 1 = 2 < k
        3 - 3 = 0 < k
        6 - 3 = 3 == k
        6 - 1 = 5 > k
        6 - 6 = 0 < k


"""


# O(n) T, O(1) S
def countPossibleSegments1(w, k):
    balanced_weights = start = end = 0
    while start < len(w):
        max_weight = max(w[start], w[end])
        min_weight = min(w[start], w[end])
        difference = max_weight - min_weight
        if difference <= k:
            balanced_weights += 1
            end += 1
            if end == len(w):
                start += 1
                end = start
        else:
            start += 1
            end = start

    return balanced_weights


def main():
    weightsI = [1, 3, 6]
    weightsII = [1, 5, 9]
    weightsIII = [1, 10, 2]
    k = 3
    k1 = 9
    print(countPossibleSegments1(weightsI, k))
    print(countPossibleSegments1(weightsII, k))
    print(countPossibleSegments1(weightsIII, k1))


if __name__ == '__main__':
    main()
