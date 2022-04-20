""" 
Given four integer arrays nums1, nums2, nums3, 
and nums4 all of length n, return the number 
of tuples (i, j, k, l) such that:

0 <= i, j, k, l < n
nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0
 

Example 1:

Input: nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]
Output: 2
Explanation:
The two tuples are:
1. (0, 0, 0, 1) -> nums1[0] + nums2[0] + nums3[0] + nums4[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> nums1[1] + nums2[1] + nums3[0] + nums4[0] = 2 + (-1) + (-1) + 0 = 0
Example 2:

Input: nums1 = [0], nums2 = [0], nums3 = [0], nums4 = [0]
Output: 1
 

Constraints:

n == nums1.length
n == nums2.length
n == nums3.length
n == nums4.length
1 <= n <= 200
-228 <= nums1[i], nums2[i], nums3[i], nums4[i] <= 228

=========================================================================


This problem is a variation of 4Sum, and we recommend checking that problem first. 
The main difference is that here we pick each element from a different array, while in 4Sum 
all elements come from the same array. For that reason, we cannot use the Two Pointers approach, 
where elements must be in the same sorted array.

On the bright side, we do not need to worry about using the same element twice - we pick 
one element at a time from each array. As you will see later, this help reduce the time complexity.

Finally, we do not need to return actual values and ensure they are unique; we just count each 
combination of four elements that sums to zero.


===============================================================================

A brute force solution will be to enumerate all combinations of elements using four nested loops, which results in O(n4) time complexity.
A faster approach is to use three nested loops, and, for each sum a + b + c, search for a complementary value d == -(a + b + c) in the 
fourth array. We can do the search in O(1) if we populate the fourth array into a hashmap.

Note that we need to track the frequency of each element in the fourth array. If an element 
is repeated multiple times, it will form multiple quadruples. Therefore, we will use hashmap values to store counts.
Building further on this idea, we can observe that a + b == -(c + d). First, we will count sums of elements a + b from
the first two arrays using a hashmap. Then, we will enumerate elements from the third and fourth arrays, and search
for a complementary sum a + b == -(c + d) in the hashmap.


===========================================================================================

Algorithm

For each a in A.

For each b in B.
If a + b exists in the hashmap m, increment the value.
Else add a new key a + b with the value 1.
For each c in C.

For each d in D.
Lookup key -(c + d) in the hashmap m.
Add its value to the count cnt.
Return the count cnt.
"""
import collections


class Solution:
    def four_sum_count(self, A, B, C, D):
        cnt = 0
        m = collections.defaultdict(int)
        print(m)
        for a in A:
            for b in B:
                m[a + b] += 1

        for c in C:
            for d in D:
                cnt += m[-c + d]
        print(m)
        return cnt


_four_sum = Solution()
_four_sum.four_sum_count([1, 2], [-2, -1], [-1, 2], [0, 2])
# print(_four_sum.four_sum_count([0], [0], [0], [0]))


"""
Approach 2: kSum II
After you solve 4Sum II, an interviewer can follow-up with 5Sum II, 6Sum II, and so on. What they 
are really expecting is a generalized solution for k input arrays. Fortunately, the hashmap 
approach can be easily extended to handle more than 4 arrays.

===========================================================================================================================

Above, we divided 4 arrays into two equal groups, and processed each group independently. 
Same way, we will divide k arrays into two groups. For the first group, we will have k/2
nested loops to count sums. Another k/2 nested loops will enumerate arrays in the second group and search for complements.

==============================================================================================================================

Algorithm

We can implement k/2 nested loops using a recursion, passing the index i of the current list as the parameter.
The first group will be processed by addToHash recursive function, which accumulates sum and terminates when adding the final sum to a hashmap m.

The second function, countComplements, will process the other group, accumulating the complement value.
 In the end, it searches for the final complement value in the hashmap and adds its count to the result.
"""


class SolutionII:
    def four_sum_count(self, A, B, C, D):
        m = collections.defaultdict(int)
        lists = [A, B, C, D]

        def n_sum_count():
            add_to_hash(0, 0)
            return count_complements(len(lists) // 2, 0)

        def add_to_hash(i, total):
            if i == len(lists) // 2:
                m[total] += 1
            else:
                for a in lists[i]:
                    add_to_hash(i + 1, total + a)

        def count_complements(i, complement):
            if i == len(lists) // 2:
                return m[complement]
            cnt = 0
            for a in lists[i]:
                cnt += count_complements(i + 1, complement - a)
            return cnt

        return n_sum_count()


""" 
Complexity Analysis

Time Complexity: O(n^1/2) or O(n^2) for 4Sum II. We have k/2 nested loops to count
sums, and another k/2 nested loop to find complements.

If the number of arrays is odd, the time complexity will be O(n^[k+1]/2).
We will pass k/2 arrays to addToHash, and k+2/2 arrays to kSumCount to keep
the space complexity O(n^k/2).

Space Complexity: O(n^k/2) for the hashmap. The space needed for the recursion will not 
exceed k/2.

======================================================================================

Further Thoughts
For an interview, keep in mind the generalized implementation. 
Even if your interviewer is OK with a simpler code, you'll get some 
extra points by describing how your solution can handle more than 4 arrays.

It's also important to discuss trade-offs with your interviewer. 
If we are tight on memory, we can move some arrays from the first group
to the second. This, of course, will increase the time complexity.
In other words, the time complexity can range from O(n^k) to O(n^k/2), and
the memory complexity ranges from O(1) to O(n^k/2) accordingly.

"""
