---
layout: post
title: "108. Convert Sorted Array to Binary Search Tree"
category: divide-and-conquer
---


## Problem Description

Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

Example 1:

![](https://raw.githubusercontent.com/Zhenye-Na/img-hosting-picgo/master/img/btree1.jpg)

```
Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:
```

> ![](https://raw.githubusercontent.com/Zhenye-Na/img-hosting-picgo/master/img/btree2.jpg)

Example 2:

![](https://raw.githubusercontent.com/Zhenye-Na/img-hosting-picgo/master/img/btree.jpg)

```
Input: nums = [1,3]
Output: [3,1]
Explanation: [1,3] and [3,1] are both a height-balanced BSTs.
```

Constraints:

```
1 <= nums.length <= 10^4
-10^4 <= nums[i] <= 10^4
nums is sorted in a strictly increasing order.
```


## Solution

Recursively build binary search tree


### Python

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums or len(nums) == 0:
            return None
        
        if len(nums) == 1:
            return TreeNode(nums[0])
        
        n = len(nums)
        root = TreeNode(nums[n // 2])
        left = self.sortedArrayToBST(nums[: n// 2])
        right = self.sortedArrayToBST(nums[n // 2 + 1:])
        
        root.left = left
        root.right = right
        return root
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
    public TreeNode sortedArrayToBST(int[] nums) {
        if (nums == null || nums.length == 0) {
            return null;
        }

        if (nums.length == 1) {
            return new TreeNode(nums[0]);
        }

        int n = nums.length;
        
        TreeNode root = new TreeNode(nums[n / 2]);
        TreeNode left = sortedArrayToBST(Arrays.copyOfRange(nums, 0, n / 2));
        TreeNode right = sortedArrayToBST(Arrays.copyOfRange(nums, n / 2 + 1, nums.length));

        root.left = left;
        root.right = right;
        return root;

    }
}
```


**Complexity Analysis**

- Time Complexity
  - O(n)
- Space Complexity
  - O(n)
    - this can be optimized by passing the startIndex and endIndex without passing the actual array


