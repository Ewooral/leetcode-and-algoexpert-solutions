class SolutionI {
    public double mincostToHireWorkers(int[] quality, int[] wage, int K) {
        int N = quality.length;
        double ans = 1e9;

        for (int captain = 0; captain < N; ++captain) {
            // Must pay at least wage[captain] / quality[captain] per qual
            double factor = (double) wage[captain] / quality[captain];
            double prices[] = new double[N];
            int t = 0;
            for (int worker = 0; worker < N; ++worker) {
                double price = factor * quality[worker];
                if (price < wage[worker])
                    continue;
                prices[t++] = price;
            }

            if (t < K)
                continue;
            Arrays.sort(prices, 0, t);
            double cand = 0;
            for (int i = 0; i < K; ++i)
                cand += prices[i];
            ans = Math.min(ans, cand);
        }

        return ans;
    }
}





class SolutionII {
    public double mincostToHireWorkers(int[] quality, int[] wage, int K) {
        int N = quality.length;
        Worker[] workers = new Worker[N];
        for (int i = 0; i < N; ++i)
            workers[i] = new Worker(quality[i], wage[i]);
        Arrays.sort(workers);

        double ans = 1e9;
        int sumq = 0;
        PriorityQueue<Integer> pool = new PriorityQueue();
        for (Worker worker: workers) {
            pool.offer(-worker.quality);
            sumq += worker.quality;
            if (pool.size() > K)
                sumq += pool.poll();
            if (pool.size() == K)
                ans = Math.min(ans, sumq * worker.ratio());
        }

        return ans;
    }
}

/**
 * Time Complexity: O(NlogN), where N is the number of workers.
   Space Complexity: O(N).
 */

class Worker implements Comparable<Worker> {
    public int quality, wage;
    public Worker(int q, int w) {
        quality = q;
        wage = w;
    }

    public double ratio() {
        return (double) wage / quality;
    }

    public int compareTo(Worker other) {
        return Double.compare(ratio(), other.ratio());
    }
}



/**
 * EXPLANATION
 * 
 * ook me a really long time to understand the optimal solution so here is my attempt at
 *  explaining it in an easier-to-understand way:

The major insight that they don't explain clearly is as follows. We want to figure out which worker 
is the one who is supposed to be paid their minimum wage. We know that at least one person is getting paid minimum wage,
 and so we want to be able to easily say if we pay one person minimum wage, who are the other people that we can afford.

We do this by computing the ratio of price to quality, or essentially computing the price per unit of quality. 

Then if we compare the ratios, we know that if we hire a person with ratio X at minimum wage, we can hire anyone 
with a ratio <= X while paying the person minimum wage.

Why is this the case? We can pretty clearly logic our way through this. If one person charges less for the same amount 
of quality and we're paying each person relative to their amount of quality, then the person who charges less is happier 
getting paid relative to the person who charges more. A simple example:

person1: wage = 10, quality = 5, ratio = 10/5 = 2
person2: wage = 5, quality = 10, ratio = 5/10 = 0.5
If we pay person1 their minimum wage, then they earn 10 and person2 earns 20. That's fine. However, if we pay person2 their
 minimum wage, they earn 5 and person1 only earns 2.5, which is not allowed. Note how the ratios basically reflect this.

So that's how the ratios affect things here. Now how do we use this?

Well as long as we are paying everyone their minimum wage, we know we want to hire the lowest quality people possible. Since
 we're paying in proportion to quality, the lower quality the people, the cheaper they will be for us to actually hire.

So our basic approach is to say, for each person, assume we're paying them minimum wage and then use the ratios to quickly
 find everyone we can hire for a rate proportional to their minimum wage. Then of that group of people, find the K-1 people 
 with the lowest quality because that will be the cheapest configuration with that initial person getting their minimum wage.

If you read the code for their solution, they optimize all of this stuff. We use a heap to maintain a set of the K lowest-quality
 workers that we've seen so far and then we iterate over the workers in order of ratio from lowest to highest.

That means that for each worker in our list, if there are K-1 workers in the heap, we instantly have the K-1 lowest quality workers 
that we can hire where the current worker can be paid their minimum wage. We're just going to look at each of these combinations.

Finally, they do one more optimization. If you just did what I described, it would take you O(K) to compute the total amount you need 
to pay each time. However, by tracking the sum of the quality of the K-1 lowest quality workers, you are able to compute the total amount
 in constant time. Remember that everyone needs to be getting paid the same amount per unit of quality, and we have the ratio that that 
 should be, so we just have to pay maxRatio * totalQuality.
 */