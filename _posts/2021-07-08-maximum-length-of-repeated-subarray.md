---
layout: post
title: "718. Maximum Length of Repeated Subarray"
category: dp
---


## Problem Description

Given two integer arrays nums1 and nums2, return the maximum length of a subarray that appears in both arrays.

Example 1:

```
Input: nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]
Output: 3
Explanation: The repeated subarray with maximum length is [3,2,1].
```

Example 2:

```
Input: nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]
Output: 5
```

Constraints:

```
1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 100
```

## Solution

Use dynamic programming. `dp[i][j]` will be the answer for inputs `A[i:]`, `B[j:]`.

### Python

```python
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:        
        nums1 = ["#"] + nums1
        nums2 = ["#"] + nums2
        max_len = 0

        # dp initialization
        # f[i][j] represents the length of the maximum length of
        # a subarray that appears in nums1[i:], nums2[j:]
        l1, l2 = len(nums1), len(nums2)
        f = [[0 for _ in range(l2)] for _ in range(l1)]

        for i in range(1, l1):
            for j in range(1, l2):
                if nums1[i] == nums2[j]:
                    f[i][j] = f[i - 1][j - 1] + 1

                    max_len = max(max_len, f[i][j])

        return max_len
```


### Java

```java
class Solution {
    public int findLength(int[] nums1, int[] nums2) {
        int res = 0;
        int l1 = nums1.length, l2 = nums2.length;
        int[][] f = new int[l1 + 1][l2 + 1];

        for (int i = 0; i < l1; i++) {
            for (int j = 0; j < l2; j++) {
                f[i + 1][j + 1] = 0;
                if (nums1[i] == nums2[j])
                    f[i + 1][j + 1] = f[i][j] + 1;
                res = Math.max(res, f[i + 1][j + 1]);
            }
        }

        return res;
    }
}
```

**Complexity Analysis**

- Time Complexity
  - O(mn)
- Space Complexity
  - O(mn)
  - can be oprtimzed to O(min(m,n)) if you use rolling array

