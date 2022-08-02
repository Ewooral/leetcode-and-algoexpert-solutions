"""
# FIND POINT
for i in range(int(raw_input())):
    px, py, qx, qy = map(int, raw_input().split())
    print("{0} {1}".format(2*qx-px, 2*qy-py))

* Another Solution
for i in range(int(input())):
    x1,y1,x2,y2 = (map(int, input().split()))
    print(x1+(x2-x1)*2, y1+(y2-y1)*2)

* C++ Code
The midPoint formula is the (first coordinate + second coordinate)
 divided by 2. So for example to find the mid-point between R(2, 2)
and P(0, 0) you have to use the formula separately for X and Y. So the
middle for X is (Mx = (Rx + Px) / 2 ) and for Y is (My = (Ry + Py) / 2)

Mx = (2 + 0) / 2 = 2 / 2 = 1

My = (2 + 0) / 2 = 2 / 2 = 1

so MidPoint is at coordinates M(1, 1).

What if the MidPoint is given and we have to calculate the point
at the other half of the line. Then we use the formula above.
So for example if we are given P(0, 0) and the midpoint M(1, 1) you should find R(x, y).

Mx = (Rx + Px) / 2 => Rx = 2Mx - Px

My = (Ry + Py) / 2 => Ry = 2My - Py

And thats how you find the coordinates for R.

"""

