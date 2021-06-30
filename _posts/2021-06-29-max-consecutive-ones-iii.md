---
layout: post
title: "1004. Max Consecutive Ones III"
category: two-pointers
---


## Problem Description

Given a binary array `nums` and an integer `k`, return the maximum number of consecutive `1`'s in the array if you can flip at most `k` `0`'s.

Example 1:

```
Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation:  [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
```


Example 2:

```
Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation:  [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
```

Constraints:

- `1 <= nums.length <= 10^5`
- `nums[i]` is either `0` or `1`.
- `0 <= k <= nums.length`


## Solution

Since we have a restriction on we can only flip at most `k` 0's, which means we can only include at most k 0's in our subarray and keep record on the longest subarray we can get from iterating the input array.

This leads to a `sliding window` solution to this problem. To implement `sliding window`, I usually implemented it with two pointers.

You can find both python and java solution below. If you have any questions, please feel free to open an issue in the github repo.

### python

```python
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        if not nums or len(nums) == 0:
            return 0

        left, right = 0, 0
        if nums[right] == 0:
            k -= 1

        n = len(nums)
        max_length = 0

        for left in range(n):

            while right + 1 < n and ( (k > 0) or nums[right + 1] == 1 ):
                if nums[right + 1] == 0:
                    k -= 1
                right += 1

            if k >= 0:
                max_length = max(max_length, right - left + 1)

            if nums[left] == 0:
                k += 1

        return max_length
```


### java

```java
class Solution {
    public int longestOnes(int[] nums, int k) {
        if (nums == null || nums.length == 0)
            return 0;

        int n = nums.length;
        int maxLength = 0;

        int left = 0;
        int right = 0;
        if (nums[right] == 0)
            k--;

        for (left = 0; left < n; left++) {
            while ( right + 1 < n && ( k > 0 || nums[right + 1] == 1 ) ) {
                if (nums[right + 1] == 0)
                    k--;
                right++;
            }

            if (k >= 0)
                maxLength = Math.max(maxLength, right - left + 1);

            if (nums[left] == 0)
                k++;
        }

        return maxLength;
    }
}
```

### Complexity Analysis

- Time Complexity
    - O(n) (think twice)
- Space Complexity
    - O(1)
