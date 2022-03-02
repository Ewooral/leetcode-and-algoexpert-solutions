""" 
There are n workers. You are given two integer arrays quality and wage
where quality[i] is the quality of the ith worker and wage[i] is 
the minimum wage expectation for the ith worker.

We want to hire exactly k workers to form a paid group. To hire a 
group of k workers, we must pay them according to the following rules:

Every worker in the paid group should be paid in the ratio of their 
quality compared to other workers in the paid group.
Every worker in the paid group must be paid at least their 
minimum wage expectation.
Given the integer k, return the least amount of money needed 
to form a paid group satisfying the above conditions. 
Answers within 10-5 of the actual answer will be accepted.

=============================================================

Example 1:

Input: quality = [10,20,5], wage = [70,50,30], k = 2
Output: 105.00000
Explanation: We pay 70 to 0th worker and 35 to 2nd worker.
Example 2:

Input: quality = [3,1,10,10,1], wage = [4,8,2,2,7], k = 3
Output: 30.66667
Explanation: We pay 4 to 0th worker, 13.33333 to 2nd and 3rd workers 
separately.
 

Constraints:

n == quality.length == wage.length
1 <= k <= n <= 104
1 <= quality[i], wage[i] <= 104


=============================================================

Solution
Approach 1: Greedy
Intuition

At least one worker will be paid their minimum wage expectation. 
If not, we could scale all payments down by some factor and still 
keep everyone earning more than their wage expectation.

Algorithm

For each captain worker that will be paid their minimum wage 
expectation, let's calculate the cost of hiring K workers where 
each point of quality is worth wage[captain] / quality[captain] dollars.
With this approach, the remaining implementation is straightforward.

Note that this algorithm would not be efficient enough to pass 
larger test cases.
"""


class SolutionII(object):
    def mincostToHireWorkers(self, quality, wage, K):
        from fractions import Fraction
        ans = float('inf')

        N = len(quality)
        for captain in xrange(N):
            # Must pay at least wage[captain] / quality[captain] per qual
            factor = Fraction(wage[captain], quality[captain])
            prices = []
            for worker in xrange(N):
                price = factor * quality[worker]
                if price < wage[worker]:
                    continue
                prices.append(price)
            if len(prices) < K:
                continue
            prices.sort()
            ans = min(ans, sum(prices[:K]))

        return float(ans)

""" 
Complexity Analysis

Time Complexity: O(N^2log N) where N is the number of workers.

Space Complexity: O(N).
"""



""" 
Approach 2: Heap
Intuition

As in Approach #1, at least one worker is paid their minimum wage 
expectation.

Additionally, every worker has some minimum ratio of dollars to 
quality that they demand. For example, if wage[0] = 100 and quality[0] = 20, 
then the ratio for worker 0 is 5.0.

The key insight is to iterate over the ratio. Let's say we hire 
workers with a ratio R or lower. Then, we would want to know 
the K workers with the lowest quality, and the sum of that quality. 
We can use a heap to maintain these variables.

Algorithm

Maintain a max heap of quality. (We're using a minheap, with negative 
values.) We'll also maintain sumq, the sum of this heap.

For each worker in order of ratio, we know all currently considered 
workers have lower ratio. (This worker will be the 'captain', as 
described in Approach #1.) We calculate the candidate answer as this 
ratio times the sum of the smallest K workers in quality.
"""


class Solution(object):
    def mincost_to_hire_workers(self, quality, wage, K):
        from fractions import Fraction
        workers = sorted((Fraction(w, q), q, w)
                         for q, w in zip(quality, wage))
        
        ans = float('inf')
        pool = []
        sumq = 0
        for ratio, q, w in workers:
            heap_q.heappush(pool, -q)
            sumq += q

            if len(pool) > K:
                sumq += heapq.heappop(pool)
            
            if len(pool) == K:
                ans = min(ans, ratio * sumq)

        

        return float(ans)


            

        
