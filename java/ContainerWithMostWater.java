/**
 * You are given an integer array height of length n. There are n vertical lines
 * drawn such that the two endpoints of the ith line are (i, 0) and (i,
 * height[i]).
 * 
 * Find two lines that together with the x-axis form a container, such that the
 * container contains the most water.
 * 
 * Return the maximum amount of water a container can store.
 * 
 * Notice that you may not slant the container.
 
 
 * Input: height = [1,8,6,2,5,4,8,3,7]
 * Output: 49
 * Explanation: The above vertical lines are represented by array
 * [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the
 * container can contain is 49.
 * Example 2:
 * 
 * Input: height = [1,1]
 * Output: 1
 * 
 */


//Approach 1: Brute Force
// Algorithm
// In this case, we will simply consider the area for every possible pair of the lines and find out the maximum area out of those.
/**
 * Complexity Analysis
 * Time complexity : O(n^2)O(n2). Calculating area for all n(n-1)/2 height pairs.
 * Space complexity : O(1)O(1). Constant extra space is used.
 */
public class ContainerWithMostWater {
    public int maxArea(int[] height) {
        int maxarea = 0;
        for (int i = 0; i < height.length; i++)
            for (int j = i + 1; j < height.length; j++)
                maxarea = Math.max(maxarea, Math.min(height[i], height[j]) * (j - i));
        return maxarea;
    }
}
