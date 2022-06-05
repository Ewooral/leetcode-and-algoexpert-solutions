'''
you're given two non empty strings.

'''
# O(n^2 + m) time | O(n + m) space

def pattern_matcher(pattern, string):
    if len(pattern) > len(string):
        return []
    # newPattern = getNewPattern(pattern)
    didSwitch = newPattern[0] != pattern[0]
    counts = {"X": 0, "y": 0}
    firstYpos = getCountsAndFirstYPos(newPattern, counts)

