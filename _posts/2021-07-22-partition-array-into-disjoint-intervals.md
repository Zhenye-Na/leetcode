---
layout: post
title: "915. Partition Array into Disjoint Intervals"
category: array
---


## Problem Description

Given an array nums, partition it into two (contiguous) subarrays left and right so that:

```
Every element in left is less than or equal to every element in right.
left and right are non-empty.
left has the smallest possible size.
```

Return the length of left after such a partitioning.

It is guaranteed that such a partitioning exists.


Example 1:

```
Input: nums = [5,0,3,8,6]
Output: 3
Explanation: left = [5,0,3], right = [8,6]
```

Example 2:

```
Input: nums = [1,1,1,0,6,12]
Output: 4
Explanation: left = [1,1,1,0], right = [6,12]
```

Note:

```
2 <= nums.length <= 30000
0 <= nums[i] <= 106
It is guaranteed there is at least one way to partition nums as described.
```

## Solution

### Python

```python
class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        leftMax = globalMax = nums[0]
        partition = 0

        for i in range(1, len(nums)):
            globalMax = max(globalMax, nums[i])
            if nums[i] < leftMax:  # If nums[i] < leftMax then nums[i] belong to left subarray, re-partition leftSubArr = nums[0..i]
                partition = i
                leftMax = globalMax

        return partition + 1

```


### Java

```java
class Solution {
    public int partitionDisjoint(int[] nums) {
        int prevMax = nums[0]; 
        int currMax = nums[0];
        int ans = 0;
        
        for (int i = 1; i < nums.length; i++) {
            
          currMax = Math.max(nums[i], currMax); 
            
            if (nums[i] < prevMax) {
                ans = i;
                prevMax = currMax;
            }
        }
        return ans + 1; 
    }
}
```



**Complexity Analysis**

- Time Complexity
  - O(n)
- Space Complexity
  - O(1)

