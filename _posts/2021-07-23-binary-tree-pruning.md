---
layout: post
title: "814. Binary Tree Pruning"
category: divide-and-conquer
---


## Problem Description

Given the root of a binary tree, return the same tree where every subtree (of the given tree) not containing a 1 has been removed.

A subtree of a node node is node plus every node that is a descendant of node.

Example 1:

![](https://raw.githubusercontent.com/Zhenye-Na/img-hosting-picgo/master/img/1028_2.png)

```
Input: root = [1,null,0,0,1]
Output: [1,null,0,null,1]
Explanation: 
Only the red nodes satisfy the property "every subtree not containing a 1".
The diagram on the right represents the answer.
```


Example 2:

![](https://raw.githubusercontent.com/Zhenye-Na/img-hosting-picgo/master/img/1028_1.png)

```
Input: root = [1,0,1,0,0,0,1]
Output: [1,null,1,null,1]
```


Example 3:

![](https://raw.githubusercontent.com/Zhenye-Na/img-hosting-picgo/master/img/1028.png)

```
Input: root = [1,1,0,1,1,0,1,0]
Output: [1,1,0,1,1,null,1]
```

Constraints:

```
The number of nodes in the tree is in the range [1, 200].
Node.val is either 0 or 1.
```

## Solution

Use Divide & Conquer

### Python

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        
        res = self.helper(root)
        if res:
            return None
        return root
        
        
    def helper(self, root):
        if not root:
            return True
        
        left = self.helper(root.left)
        right = self.helper(root.right)
    
        if left:
            root.left = None
            
        if right:
            root.right = None
    
        if left and right and root.val == 0:
            return True
    
        return False

```

### Java

```java
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
```


**Complexity Analysis**

- Time Complexity
  - O(n)
- Space Complexity
  - O(1)
