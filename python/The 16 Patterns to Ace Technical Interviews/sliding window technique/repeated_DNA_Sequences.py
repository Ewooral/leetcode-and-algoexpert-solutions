"""
The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C',  and 'T'

For example, 'ACGAATTCCG' IS A DNA sequence

When studying DNA, it is useful to identify repeated sequences within the DNA. Given a string
's' that represents a DNA sequence, return all the 10-letter-long sequences(substrings that occur more
than once in a DNA molecule. You may return the answer in any order

E.g. Input: s = AAAAACCCCCAAAAACCCCCAAAAAGGGTTT'
Output: ['AAAAACCCCC', 'CCCCCAAAAA]

"""
from collections import Counter


def repeatedDNASequence(s):
    res, visited = set(), set()

    for i in range(len(s) - 10):
        first_10_subS = s[i:i + 10]
        if first_10_subS in visited:
            res.add(first_10_subS)
        visited.add(first_10_subS)

    return list(res)


def main():
    s = 'AAAAACCCCCAAAAACCCCCAAAAAGGGTTT'
    print(repeatedDNASequence(s))


if __name__ == '__main__':
    main()
