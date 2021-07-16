/*
 * @lc app=leetcode id=611 lang=java
 *
 * [611] Valid Triangle Number
 *
 * https://leetcode.com/problems/valid-triangle-number/description/
 *
 * algorithms
 * Medium (49.73%)
 * Likes:    1857
 * Dislikes: 129
 * Total Accepted:    109.5K
 * Total Submissions: 222.7K
 * Testcase Example:  '[2,2,3,4]'
 *
 * Given an integer array nums, return the number of triplets chosen from the
 * array that can make triangles if we take them as side lengths of a
 * triangle.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: nums = [2,2,3,4]
 * Output: 3
 * Explanation: Valid combinations are: 
 * 2,3,4 (using the first 2)
 * 2,3,4 (using the second 2)
 * 2,2,3
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: nums = [4,2,3,4]
 * Output: 4
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= nums.length <= 1000
 * 0 <= nums[i] <= 1000
 * 
 * 
 */

// @lc code=start
class Solution {
    public int triangleNumber(int[] nums) {
        if (nums == null || nums.length < 3) return 0;

        Arrays.sort(nums);
        int count = 0;

        for (int i = 2; i < nums.length; i++) {
            int j = 0, k = i - 1;
            while (j < k) {
                if (nums[j] + nums[k] > nums[i]) {
                    count += k - j;
                    k--;
                } else {
                    j++;
                }
            }
        }

        return count;
    }
}
// @lc code=end

