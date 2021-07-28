---
layout: post
title: "16. 3Sum Closest"
category: array
---


## Problem Description

Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example 1:

```
Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
```

Constraints:

```
3 <= nums.length <= 10^3
-10^3 <= nums[i] <= 10^3
-10^4 <= target <= 10^4
```

## Solution

Two Sum

### Python

```python
import sys

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = None

        for i in range(len(nums)):
            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[left] + nums[right] + nums[i]
                if ans is None or abs(total - target) < abs(ans - target):
                    ans = total

                if total <= target:
                    left += 1
                else:
                    right -= 1

        return ans
```

### Java

```java
class Solution {
    public int threeSumClosest(int[] nums, int target) {
        if (nums == null || nums.length < 3) {
            return -1;
        }
        
        Arrays.sort(nums);
        int bestSum = nums[0] + nums[1] + nums[2];

        for (int i = 0; i < nums.length; i++) {
            int start = i + 1, end = nums.length - 1;
            while (start < end) {
                int sum = nums[i] + nums[start] + nums[end];

                if (Math.abs(target - sum) < Math.abs(target - bestSum)) {
                    bestSum = sum;
                }

                if (sum < target) {
                    start++;
                } else {
                    end--;
                }
            }
        }

        return bestSum;
    }
}
```

**Complexity Analysis**

- Time Complexity
  - O(n^2)
- Space Complexity
  - O(1)
