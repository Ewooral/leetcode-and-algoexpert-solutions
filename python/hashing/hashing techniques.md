# Hashing is a searching technique

    We already know there are two types of searching techniques
        1. Linear O(n)
        2. Binary Search O(log n). Binary search is only effective if 
        extra effort is made by sorting the list or array.

        3. Hashing is also a searching Technique.
 
## The drawback for hashing is space problem

* Hashing use two mapping functions

      keys (8, 3, 6, 10, 15, 9, 4)

      1. one to one. (Ideal Hash function) 
        => h(x) = x
           
        The draw back is that, the space needed is huge. Huge space could
        be resolved using the modulus hashing technique

      2. many to one (Modulus Hash function)
        => h(x) = x % len(arr)

        The draw back is that collision may be achieved

* Two methods used to solve collision problem

      1. Open Hashing
        - Chaining
          With chaining, if there is a collision, the keys are chained using a linked list in a sorting order

      2. closed Hashing
        - linear probing
        - quadratic probiing 
        - double probing


# Properties of a good Hash function
1. It distributes hash values uniformly across hash tables

2. It has to use all the input data

# Collision Resolution Techniques

