""" 
Notes
In the video explanation of this question, we explain that we need to handle negative values for the nextIdx calculated in our helper method.

nextIdx = (currentIdx + jump) % len(array)
return nextIdx if nextIdx >= 0 else nextIdx + len(array)
In most programming languages, this is necessary because, if currentIdx + jump is negative, then (currentIdx + jump) % len(array) will also be negative.

In Python, however, "the modulo operator always yields a 
result with the same sign as its second operand (or zero)" [Python Docs].
In other words, in Python, the modulo operation to compute the nextIdx will always return a number with the sign of len(array), which is naturally positive.

More specifically, the modulo operator in Python behaves as follows when used with a negative first operand:

-x % y == -(x % y) + y
The Python modulo operator effectively does, by default, what we do in our code to handle negative values.

Thus, in Python, we can just return (currentIdx + jump) % len(array) for the nextIdx, without needing to handle negative values.
"""
