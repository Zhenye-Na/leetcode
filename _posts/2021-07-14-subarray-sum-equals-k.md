---
layout: post
title: "560. Subarray Sum Equals K"
category: hashmap
---


## Problem Description

Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.

Example 1:

```
Input: nums = [1,1,1], k = 2
Output: 2
```

Example 2:

```
Input: nums = [1,2,3], k = 3
Output: 2
```

Constraints:

```
1 <= nums.length <= 2 * 104
-1000 <= nums[i] <= 1000
-10^7 <= k <= 10^7
```


## Solution

Use HashMap to store prefixSum occurences

### Python

```python
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = [0]
        for num in nums:
            prefix_sum.append(prefix_sum[-1] + num)

        prefix_sum_count = {}
        res = 0

        for i in range(len(prefix_sum)):
            if prefix_sum[i] - k in prefix_sum_count:
                res += prefix_sum_count[prefix_sum[i] - k]
            prefix_sum_count[prefix_sum[i]] = prefix_sum_count.get(prefix_sum[i], 0) + 1

        return res
```

### Java


```java
class Solution {
    public int subarraySum(int[] nums, int k) {
        int prefixSum = 0;
        int count = 0;

        Map<Integer, Integer> map = new HashMap<>();
        map.put(0, 1);

        for (int num : nums) {
            prefixSum += num;
            if (map.containsKey(prefixSum - k)) {
                count += map.get(prefixSum - k);
            }
            map.put(prefixSum, map.getOrDefault(prefixSum, 0) + 1);
        }

        return count;
    }
}
```

**Complexity Analysis**

- Time Complexity
  - O(n)
- Space Complexity
  - O(n)

