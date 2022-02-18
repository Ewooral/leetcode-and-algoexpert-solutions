/*
Amazon warehouse has a group of n items of various weights lined 
up in a row. A segment of contiguously placed items can be shipped
together if and only if the difference between the weights of the 
heaviest and lightest item differs by at most k to avoid load imbalance.

Given the weights of the n items and an integer k, find the number
of segments of items that can be shipped together.

Note: A segment (I, r) is a subarray starting at index I and ending
at index r
where
I < or = r
*/
#include <vector>

long long int countPossibleSegments(vector<int> weights, int k)
{
    int left, right, minpos, maxpos;
    minpos = 0, maxpos = 0;
    long long int ans = 0;
    int wlen = weights.size();
    for (left = 0, right = 0; right < wlen; right++)
    {
        auto segmentMin = weights[minpos];
        auto segmentMax = weights[maxpos];
        auto currWeight = weights[right];
        if (currWeight > segmentMax)
        {
//             // assign new min
            maxpos = right;
            if ((currWeight - segmentMin) > k)
            {
                left = minpos;
                while (abs(currWeight - weights[left]) > k)
                    left++;
                minpos = left;
            }
        }
        else if (currWeight < segmentMin)
//         {
//             // assign new max
            minpos = right;
            if ((segmentMax - currWeight) > k)
//             {
                left = maxpos;
                while (abs(currWeight - weights[left]) > k)
//                     left++;
//                 maxpos = left;
//             }
//         }
//         // we can freely expand the window
//         ans += (right - left) + 1;
//     }
//     return ans;
}