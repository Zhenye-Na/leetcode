/*
 * @lc app=leetcode id=814 lang=java
 *
 * [814] Binary Tree Pruning
 *
 * https://leetcode.com/problems/binary-tree-pruning/description/
 *
 * algorithms
 * Medium (71.62%)
 * Likes:    1882
 * Dislikes: 61
 * Total Accepted:    114.4K
 * Total Submissions: 160K
 * Testcase Example:  '[1,null,0,0,1]'
 *
 * Given the root of a binary tree, return the same tree where every subtree
 * (of the given tree) not containing a 1 has been removed.
 * 
 * A subtree of a node node is node plus every node that is a descendant of
 * node.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: root = [1,null,0,0,1]
 * Output: [1,null,0,null,1]
 * Explanation: 
 * Only the red nodes satisfy the property "every subtree not containing a 1".
 * The diagram on the right represents the answer.
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: root = [1,0,1,0,0,0,1]
 * Output: [1,null,1,null,1]
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: root = [1,1,0,1,1,0,1,0]
 * Output: [1,1,0,1,1,null,1]
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * The number of nodes in the tree is in the range [1, 200].
 * Node.val is either 0 or 1.
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
    public TreeNode pruneTree(TreeNode root) {
        if (root == null) {
            return root;
        }

        boolean res = helper(root);
        if (res) {
            return null;
        }
        return root;
    }



    private boolean helper(TreeNode root) {
        if (root == null) {
            return true;
        }
        
        boolean left = helper(root.left);
        boolean right = helper(root.right);


        if (left) {
            root.left = null;
        }

        if (right) {
            root.right = null;
        }

        if (left && right && root.val == 0) {
            return true;
        }

        return false;
    }

}
// @lc code=end

// 30/30 cases passed (0 ms)
// Your runtime beats 100 % of java submissions
// Your memory usage beats 85.72 % of java submissions (36.4 MB)
