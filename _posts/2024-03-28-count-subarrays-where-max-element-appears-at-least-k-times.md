---
layout: post
title: "2962. Count Subarrays Where Max Element Appears at Least K Times"
category: two-pointers
---

## Problem Description

You are given an integer array `nums` and a positive integer `k`.

Return the number of subarrays where the maximum element of `nums` appears at least `k` times in that subarray.

> A subarray is a contiguous sequence of elements within an array.

**Example 1:**

```
Input: nums = [1,3,2,3,3], k = 2
Output: 6
Explanation: The subarrays that contain the element 3 at least 2 times are:
[1,3,2,3], [1,3,2,3,3], [3,2,3], [3,2,3,3], [2,3,3] and [3,3].
```

**Example 2:**

```
Input: nums = [1,4,2,1], k = 3
Output: 0
Explanation: No subarray contains the element 4 at least 3 times.
```

**Constraints:**

```
1 <= nums.length <= 10^5
1 <= nums[i] <= 10^6
1 <= k <= 10^5
```

## Analysis

This problem involves identifying subarrays within an array where the maximum element occurs at least k times. We can approach this problem using the sliding window technique, which involves maintaining a window of elements and dynamically adjusting its size based on certain conditions.

- **Sliding Window Technique**: We'll utilize the sliding window approach to efficiently identify subarrays where the maximum element appears at least `k` times. The window will expand or shrink as we iterate through the array, ensuring that we capture all valid subarrays.
- **Identifying Maximum Element**: We start by identifying the maximum element in the array, as our goal is to focus on subarrays containing this element.
- **Counting Occurrences**: Within the sliding window, we count the occurrences of the maximum element. If the count meets or exceeds `k`, we count the subarray as valid.
- **Enumeration of Subarrays**: As we slide the window through the array, we enumerate all possible subarrays and check if the maximum element appears at least `k` times. If it does, we increment our count of valid subarrays.

By employing the sliding window technique, we ensure an efficient and systematic exploration of all possible subarrays meeting the specified criteria.

## Solution

Here's the provided Python solution:

```python
from collections import Counter

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_num = max(nums)
        counter = Counter(nums)

        if counter[max_num] < k:
            return 0

        res = 0
        left = 0
        times = 0

        for right in range(len(nums)):
            if nums[right] == max_num:
                times += 1

            while times >= k:
                if nums[left] == max_num:
                    times -= 1
                left += 1

            res += left

        return res
```

Now, let's analyze the complexity of our solution.

## Complexity Analysis

- Time Complexity: `O(n)` - We traverse the input array once.
- Space Complexity: `O(n)` - We utilize a Counter to store the frequency count of elements in the array. The space complexity is proportional to the size of this Counter, which can be at most `n` in the worst case scenario.
