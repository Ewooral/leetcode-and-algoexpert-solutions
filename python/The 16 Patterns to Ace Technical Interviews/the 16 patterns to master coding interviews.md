# SLIDING WINDOW TECHNIQUE  

You can identify sliding technique when the question demands

    * Iteration over a continuous sequence of strings, arrays
    * min, max, longest, shortest, contains
    * if we need to calculate something

Question Variants

    * max sum subarray of size k

Dynamic Variant

    * smallest sum >= some value S

Dynamic Variant with Auxiliary Data structure like hash table

    * longest substring with no more than k distinct characters
    * string permutations


``` java
Find the max sum subarray of a fixed size k
  
Example input:
[4, 2, 1, 7, 8, 1, 2, 8, 1, 2, 8, 1, 0]

int maxValue = Integer.MIN_VALUE;
int currentRunningSum = 0;

```
# Basic template of such problems is basically 3 steps.

Step1: Have a counter or hash-map to count specific array input and keep on increasing the window toward right using outer loop.
Step2: Have a while loop inside to reduce the window side by sliding toward right. Movement will be based on constraints of problem. Go through few examples below
Step3: Store the current maximum window size or minimum window size or number of windows based on problem requirement.

Sharing sample solutions for some to understand above steps.