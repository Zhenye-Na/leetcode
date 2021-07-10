---
layout: post
title: "300. Longest Increasing Subsequence"
category: dp
---


## Problem Description

Given an integer array nums, return the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

Example 1:

```
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
```

Example 2:

```
Input: nums = [0,1,0,3,2,3]
Output: 4
```


Example 3:

```
Input: nums = [7,7,7,7,7,7,7]
Output: 1
```

Constraints:

```
1 <= nums.length <= 2500
-104 <= nums[i] <= 104
```

Follow up: Can you come up with an algorithm that runs in O(n log(n)) time complexity?


## Solution

Use Dynamic Programming where f[i] represents the length of the longest strictly increasing subsequence ending with nums[i]


### Python

```python
class Solution_DP:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # initialization
        # every single number consist one increasing subseq
        dp = [1 for _ in range(len(nums))]

        for i in range(len(nums)):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    # if current number is greater than prev number
                    # we can create a new subseq with length + 1, or current length
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)
```

### Java

```java
class Solution {
    public int lengthOfLIS(int[] nums) {
        int[] f = new int[nums.length];
        for (int i = 0; i < nums.length; i++) {
            f[i] = 1;
        }

        for (int i = 0; i < nums.length; i++) {
            for (int j = 0; j < i; j++) {
                if (nums[j] < nums[i]) {
                    f[i] = Math.max(f[i], f[j] + 1);
                }
            }
        }

        int maxLen = 1;
        for (int i = 0; i < nums.length; i++) {
            maxLen = Math.max(maxLen, f[i]);
        }

        return maxLen;
    }
}
```

**Complexity Analysis**

- Time Complexity
  - O(n^2)
- Space Complexity
  - O(n)

