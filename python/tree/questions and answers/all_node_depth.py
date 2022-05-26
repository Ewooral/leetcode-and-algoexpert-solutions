'''
Notes
There's an additional, cleaner and more clever way of solving this 
question with the same time and space time complexities as the 
optimal solution covered in the video explanation.

Realize that a given node in the input tree has:

a depth of 1 with respect to its parent node
a depth of 2 with respect to its parent's parent node
a depth of 3 with respect to its parent's parent's node
...
a depth of d with respect to the root node
Since these depths are captured in each subtree's nodes' depths, which we sum up to get the final answer, we can deduce that each node in the input tree contributes 1 + 2 + 3 + ... + d - 1 + d to the final answer.

Thus, we can solve this question with a simple recursive function that takes in the running depthSum and adds the current node's depth to it at every call. See Solution 5 for the implementation of this algorithm.

We can go one step further by realizing that the sum 1 + 2 + 3 + ... + n - 1 + n can be calculated with the formula (n * (n + 1)) / 2, which eliminates the need to pass the running depthSum to each recursive function call. See Solution 6 for this implementation.

Note that these two extra solutions are very clever and wouldn't be expected of you in an interview (especially Solution 6, which takes advantage of a math formula). That being said, if you were able to come up with either of these two solutions, that certainly wouldn't be bad!
'''