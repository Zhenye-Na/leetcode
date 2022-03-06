---
layout: post
title: "1359. Count All Valid Pickup and Delivery Options"
category: dp
---

## Problem Details

Given n orders, each order consist in pickup and delivery services. 

Count all valid pickup/delivery possible sequences such that delivery(i) is always after of pickup(i). 

Since the answer may be too large, return it modulo 10^9 + 7.

Example 1:

```
Input: n = 1
Output: 1
Explanation: Unique order (P1, D1), Delivery 1 always is after of Pickup 1.
```

Example 2:

```
Input: n = 2
Output: 6
Explanation: All possible orders: 
(P1,P2,D1,D2), (P1,P2,D2,D1), (P1,D1,P2,D2), (P2,P1,D1,D2), (P2,P1,D2,D1) and (P2,D2,P1,D1).
This is an invalid order (P1,D2,P2,D1) because Pickup 2 is after of Delivery 2.
```

Example 3:

```
Input: n = 3
Output: 90
```

Constraints:

```
1 <= n <= 500
```

## Solution

Dynamic Programming + Math

For example, given 2 order

```
when n = 1:

[P1, D1] => 1

when n = 2:

[X, (P1), (D1), X] => ?

question:

how many ways we can insert P2 into the results that n = 1 ? => 3 (2 * 2 - 1)

how many ways we can insert D2 into the results that after inserting P2 ? => 4 (2 * 2)

But we need D2 to be after P2 so we divide the result by 2

which is 4 * 3 / 2 = 6
```

## Solution

```python
class Solution:
    def countOrders(self, n: int) -> int:
        # f[i] represents number combinations of i orders
        f = [0 for _ in range(n + 1)]
        f[0] = 1

        for i in range(1, n + 1):
            f[i] = (f[i - 1] * (2 * i - 1) * i) % (10 ** 9 + 7)

        return f[-1]
```

**Complexity Analysis**

- Time Complexity
  - O(n)
- Space Complexity
  - O(n) - can be optimized to O(1) using [rolling array](https://www.codetd.com/en/article/13004651)
