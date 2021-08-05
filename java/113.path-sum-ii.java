/*
 * @lc app=leetcode id=113 lang=java
 *
 * [113] Path Sum II
 *
 * https://leetcode.com/problems/path-sum-ii/description/
 *
 * algorithms
 * Medium (50.73%)
 * Likes:    3398
 * Dislikes: 93
 * Total Accepted:    466.8K
 * Total Submissions: 909K
 * Testcase Example:  '[5,4,8,11,null,13,4,7,2,null,null,5,1]\n22'
 *
 * Given the root of a binary tree and an integer targetSum, return all
 * root-to-leaf paths where each path's sum equals targetSum.
 * 
 * A leaf is a node with no children.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
 * Output: [[5,4,11,2],[5,8,4,5]]
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: root = [1,2,3], targetSum = 5
 * Output: []
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: root = [1,2], targetSum = 0
 * Output: []
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * The number of nodes in the tree is in the range [0, 5000].
 * -1000 <= Node.val <= 1000
 * -1000 <= targetSum <= 1000
 * 
 * 
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public List<List<Integer>> pathSum(TreeNode root, int targetSum) {
        List<List<Integer>> ret = new ArrayList<List<Integer>>();
        if (root == null) {
            return ret;
        }

        List<Integer> curr = new ArrayList<Integer>();
        curr.add(root.val);
        dfs(root, targetSum - root.val, curr, ret);

        return ret;
    }


    private void dfs(TreeNode root, int target, List<Integer> curr, List<List<Integer>> ret) {

        if (root.left == null && root.right == null && target == 0) {
            ret.add(new ArrayList(curr));
            return;
        }

        if (root.left == null && root.right == null) {
            return;
        }

        if (root.left != null) {
            curr.add(root.left.val);
            dfs(root.left, target - root.left.val, curr, ret);
            curr.remove(curr.size() - 1);
        }

        if (root.right != null) {
            curr.add(root.right.val);
            dfs(root.right, target - root.right.val, curr, ret);
            curr.remove(curr.size() - 1);
        }
    }

}
// @lc code=end

