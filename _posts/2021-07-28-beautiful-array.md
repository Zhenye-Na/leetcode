---
layout: post
title: "932. Beautiful Array"
category: array
---


## Problem Description

An array nums of length `n` is beautiful if:

- nums is a permutation of the integers in the range [1, n].
- For every `0 <= i < j < n`, there is no index `k` with `i < k < j` where `2 * nums[k] == nums[i] + nums[j]`.

Given the integer `n`, return any beautiful array nums of length `n`. There will be at least one valid answer for the given `n`.

Example 1:

```
Input: n = 4
Output: [2,1,4,3]
```

Example 2:

```
Input: n = 5
Output: [3,1,2,5,4]
```

Constraints:

```
1 <= n <= 1000
```


## Solution

Check out Lee's solution video [here](https://www.youtube.com/watch?v=9L6bPGDfyqo). awesome explanation

### Python

```python
class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        res = [1]
        while len(res) < n:
            res = [2 * i - 1 for i in res] + [i * 2 for i in res]

        return [i for i in res if i <= n]


    def beautifulArrayRecursion(self, n: int) -> List[int]:
        if n == 1:
            return [1]

        odd = [2 * i - 1 for i in self.beautifulArrayRecursion(n // 2 + n % 2)]
        even = [2 * i for i in self.beautifulArrayRecursion(n // 2)]

        res = odd + even
        return [i for i in res if i <= n]

    def beautifulArrayBinary(self, n: int) -> List[int]:
        return sorted(range(1, n + 1), key=lambda x: bin(x)[:1:-1])

```

**Complexity Analysis**

- Time Complexity
  - O(logn) recursion and iteration
  - O(nlogn) binary representation
- Space Complexity
  - O(1)
