"""
considering two points p =(px, py) and q = (qx, qy). We consider the
inversion or point reflection r = (rx, ry), of point p across point
q to be 180 deg rotation of point p around q. Given n sets of points
p and q, find r for each pair of points and print two space-separated
integers denoting the respective values of rx and ry on a new line.

function Description
complete the findPoint function in an editor
findPoint has the following parameters:
* int px, py, qx, qy: x and y coordinates for pints p and q

Returns
* int[2]: x and y coordinates of the reflected point r

Input format
The first line contains an integer n, denoting the number of sets of points
Each of the n subsequent lines contains four space-separated integers
that describe the respective values of px, py, qx and qy defining
points p = (px, py) and q = (qx, qy)



SOLUTION
The midPoint formula is the (first coordinate + second coordinate)
 divided by 2. So for example to find the mid-point between R(2, 2)
and P(0, 0) you have to use the formula separately for X and Y. So the
middle for X is (Mx = (Rx + Px) / 2 ) and for Y is (My = (Ry + Py) / 2)

Mx = (2 + 0) / 2 = 2 / 2 = 1

My = (2 + 0) / 2 = 2 / 2 = 1

so MidPoint is at coordinates M(1, 1).

What if the MidPoint is given and we have to calculate the point
at the other half of the line. Then we use the formula above.
So for example if we are given P(0, 0) and the midpoint M(1, 1)
you should find R(x, y).

Mx = (Rx + Px) / 2 => Rx = 2Mx - Px

My = (Ry + Py) / 2 => Ry = 2My - Py

And thats how you find the coordinates for R.
"""

# first approach
# def findPoint():
#     for i in range(int(input())):
#         px, py, qx, qy = map(int, input().split())
#         print("{0} {1}".format(2*qx-px, 2*qy-py))
# findPoint()


# second approach
def findPoint(n, arr):
    for i in range(n):
        px, py, qx, qy = map(int, arr[i])
        # print("{0} {1}".format(2 * qx - px, 2 * qy - py))
        print(f"{2 * qx - px} {2 * qy - py}")


def main():
    # find_point()
    findPoint(2, [[0, 0, 1, 1], [1, 1, 2, 2]])


if __name__ == '__main__':
    main()
