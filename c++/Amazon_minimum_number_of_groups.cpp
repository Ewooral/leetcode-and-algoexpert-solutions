/*
Amazon Prime Video is a subscription video-on-demand over-the-top 
streaming and rental service. The team at Prime Video is developing 
a method to divide movies into groups based on the number of awards 
they have won. A group can consist of any number of movies, but the 
difference in the number of awards won by any two movies in the group 
must not exceed k.
The movies can be grouped together irrespective of their initial order.
 Determine the minimum number of groups that can be formed such that 
 each movie is in exactly orly group.
Example
The numbers of awards per movie are awards = [1, 5, 4, 6, 8, 9, 21, and 
the maximum allowed difference is k = 3.

One way to divide the movies into the minimum number of groups is:

The first group can contain [2, 1], The maximum difference between
 awards of any two movies is 1 which does not exceed K.
The second group can contain [5, 4, 6], The maximum difference between
 awards of any two movies is 2 which does not exceed k.
The third group can contain [8,9]. The maximum difference between 
awards of any two movies is 1 which does not exceed k.
The movies can be divided into a minimum of 3 groups.

Function Description
Complete the function minimumGroups in the
editor below.
minimum Groups has the following parameters:
int awards[n]; the number of awards each movie has earned
int k: the maximum difference in awards counts
*/

function minGroupDifferK(arr, k)
{
    arr.sort();
    let start = 0;
    if (arr.length == 0)
        return 0;
    // // If arr has some value then at least can form 1 group
    let count = 1;
    for (let i = 0; i < arr.length; i++)
    // {
    //     if (arr[i] - arr[start] > k)
    //     {
    //         count++;
    //         start = i;
    //     }
    // }
    // return count;
};