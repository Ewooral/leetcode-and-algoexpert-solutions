"""
# Line Through Points
Given an input points which is a list of lists that
represents the points on the [x, y] plane. Determine
the list that passes through the most points

points = [
[1, 1], [2, 2],
[3, 3], [0, 4],
[-2, 6], [4, 0],
[2, 1]
]

* Generate every single possible line from two points
  using `y = mx + b` where `m` is the `slope` or
  `gradient` and `b` is the `y-intercept`

* slope = (change in y or rise)/ (change in x or run)
  - `run` is how far we go on the `x-axis`
  - `rise` is how far we go up on the `y-axis`
  - slope = rise/run

* Keep track of max points line passes through. maxPoint = 1
* loop through all points and keept track of current and next point (p1 = points[i], p2 = points[i+1])
* find the slope between two points. e.g p1 = [1, 1], p2 = [2, 2]
* store all slopes in a hash table
* With the slope we might get decimal numbers which are similar, so we cannot store slopes as decimals in
  our hash table because of floating point in precision error. E.g. 0.1 and 0.10001 will be rounded as 0.1 which might alter
  our slope on the graph, so we will use rational(a no. over another no. 2/5)/fraction to represent our slope in the hash table
* keep track of both rise and run values of the slope
* get a slope key in order to store the slope value in the hash table
* if slope key is not in hash table, set its value to 1
* go ahead to increment value by 1
*  find the max number between initial maxNum and slope values in the hash table
"""

import math


# O(n^2) T, O(n) S
def line_through_points(points):
    maxNum = 1
    # for Idx1, p1 in enumerate(points):
    for Idx1 in range(len(points)):
        p1 = points[Idx1]
        slopes = {}
        for Idx2 in range(Idx1 + 1, len(points)):
            p2 = points[Idx2]
            rise, run = get_slope_of_line_between_points(p1, p2)
            slopeKey = createHashableKeyForRational(rise, run)
            if slopeKey not in slopes:
                slopes[slopeKey] = 1
            slopes[slopeKey] += 1
        maxNum = max(maxNum, max(slopes.values(), default=0))
    return maxNum


def get_slope_of_line_between_points(p1, p2):
    p1x, p1y = p1
    p2x, p2y = p2
    slope = [1, 0]
    if p1x != p2x:
        xDiff = p1x - p2x  # numerator
        yDiff = p1y - p2y  # denominator
        # find the greatest common divisor and divide both the numerator and denominator by it
        gcd = _gcd(abs(xDiff), abs(yDiff))
        xDiff = xDiff // gcd
        yDiff = yDiff // gcd
        if xDiff < 0:
            xDiff *= -1
            yDiff *= -1
        slope = [yDiff, xDiff]
    return slope


def createHashableKeyForRational(numerator, denominator):
    return str(numerator) + ":" + str(denominator)


# greatest common divisor I
def greatest_common_divisor(a, b):
    while True:
        if a == 0:
            return b
        if b == 0:
            return a

        a, b = b, a % b


# greatest common divisor II
def _gcd(a, b):
    return math.gcd(a, b)


def main():
    points = [
        [1, 1], [2, 2],
        [3, 3], [0, 4],
        [-2, 6], [4, 0],
        [2, 1]
    ]
    print(line_through_points(points))


if __name__ == '__main__':
    main()
