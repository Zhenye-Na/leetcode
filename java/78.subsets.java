/*
 * @lc app=leetcode id=78 lang=java
 *
 * [78] Subsets
 *
 * https://leetcode.com/problems/subsets/description/
 *
 * algorithms
 * Medium (67.09%)
 * Likes:    8103
 * Dislikes: 133
 * Total Accepted:    947.8K
 * Total Submissions: 1.4M
 * Testcase Example:  '[1,2,3]'
 *
 * Given an integer array nums of unique elements, return all possible subsets
 * (the power set).
 * 
 * The solution set must not contain duplicate subsets. Return the solution in
 * any order.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: nums = [1,2,3]
 * Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: nums = [0]
 * Output: [[],[0]]
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= nums.length <= 10
 * -10 <= nums[i] <= 10
 * All the numbers of nums are unique.
 * 
 * 
 */

// @lc code=start
// Runtime: 0 ms
// Memory Usage: 39.7 MB
class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> res = new ArrayList<List<Integer>>();
        if (nums == null || nums.length == 0) {
            return res;
        }

        for (int i = 0; i < (1 << nums.length); i++) {
            List<Integer> curr = new ArrayList<>();

            for (int b = 0; b < nums.length; b++) {
                if (((i >> b) & 1) == 1) {
                    curr.add(nums[b]);
                }
            }
            res.add(curr);
        }

        return res;
    }
}
// @lc code=end

