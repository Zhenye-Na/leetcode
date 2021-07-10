/*
 * @lc app=leetcode id=718 lang=java
 *
 * [718] Maximum Length of Repeated Subarray
 *
 * https://leetcode.com/problems/maximum-length-of-repeated-subarray/description/
 *
 * algorithms
 * Medium (50.94%)
 * Likes:    2640
 * Dislikes: 63
 * Total Accepted:    123.6K
 * Total Submissions: 241K
 * Testcase Example:  '[1,2,3,2,1]\n[3,2,1,4,7]'
 *
 * Given two integer arrays nums1 and nums2, return the maximum length of a
 * subarray that appears in both arrays.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]
 * Output: 3
 * Explanation: The repeated subarray with maximum length is [3,2,1].
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]
 * Output: 5
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= nums1.length, nums2.length <= 1000
 * 0 <= nums1[i], nums2[i] <= 100
 * 
 * 
 */

// @lc code=start
class Solution {
    public int findLength(int[] nums1, int[] nums2) {
        int res = 0;
        int l1 = nums1.length, l2 = nums2.length;
        int[][] f = new int[l1 + 1][l2 + 1];

        for (int i = 0; i < l1; i++) {
            for (int j = 0; j < l2; j++) {
                f[i + 1][j + 1] = 0;
                if (nums1[i] == nums2[j])
                    f[i + 1][j + 1] = f[i][j] + 1;
                res = Math.max(res, f[i + 1][j + 1]);
            }
        }

        return res;
    }
}
// @lc code=end

