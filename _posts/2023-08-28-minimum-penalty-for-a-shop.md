---
layout: post
title: "2483. Minimum Penalty for a Shop"
category: prefix-sum
---

## Problem Description

You are given the customer visit log of a shop represented by a `0-indexed` string customers consisting only of characters `'N'` and `'Y'`:

if the ith character is `'Y'`, it means that customers come at the ith hour
whereas `'N'` indicates that no customers come at the ith hour.
If the shop closes at the jth hour `(0 <= j <= n)`, the penalty is calculated as follows:

- For every hour when the shop is open and no customers come, the penalty increases by `1`.
- For every hour when the shop is closed and customers come, the penalty increases by `1`.
- 
Return the **earliest hour** at which the shop must be closed to incur a minimum penalty.

Note that if a shop closes at the `jth` hour, it means the shop is closed at the hour `j`.

Example 1:

```
Input: customers = "YYNY"
Output: 2
Explanation: 
- Closing the shop at the 0th hour incurs in 1+1+0+1 = 3 penalty.
- Closing the shop at the 1st hour incurs in 0+1+0+1 = 2 penalty.
- Closing the shop at the 2nd hour incurs in 0+0+0+1 = 1 penalty.
- Closing the shop at the 3rd hour incurs in 0+0+1+1 = 2 penalty.
- Closing the shop at the 4th hour incurs in 0+0+1+0 = 1 penalty.
Closing the shop at 2nd or 4th hour gives a minimum penalty. Since 2 is earlier, the optimal closing time is 2.
```

Example 2:

```
Input: customers = "NNNNN"
Output: 0
Explanation: It is best to close the shop at the 0th hour as no customers arrive.
```


Example 3:

```
Input: customers = "YYYY"
Output: 4
Explanation: It is best to close the shop at the 4th hour as customers arrive at each hour.
```

## Solution

There are two available algorithms to solve this problem, but lets understand the problem first

```
#     Y   Y    N   Y
#   | 
#       |
#           | <- suppose the store closes at this moment
#                |
#                     |
```

Given the above example and vertical pipe above means that the store closes at that timestamp. Based on the penalty score calculation rules above, how are we going to get the value ?

- Before the store closed, we care about: there **are no customers** in this store
- After the store closed, we care about: there **are customers** in this store

Effectively, we could come up with a straightforward solution to iterate thru the timestamps to see which outputs the minimum penalty score

#### Solution 1: Two Pointers

```python
class Solution_TwoPointers:
    def bestClosingTime(self, customers: str) -> int:

        if not customers or len(customers) == 0:
            return 0

        min_penalty, earliest_time = len(customers), len(customers)
        for i in range(len(customers) + 1):
            left, right = i - 1, i + 1
            curr_penalty = 0
            
            if 0 <= i < len(customers) and customers[i] == 'Y':
                curr_penalty += 1
            while left >= 0:
                if customers[left] == 'N':
                    curr_penalty += 1
                left -= 1
            while right < len(customers):
                if customers[right] == 'Y':
                    curr_penalty += 1
                right += 1
            
            if curr_penalty < min_penalty:
                min_penalty = curr_penalty
                earliest_time = i

        return earliest_time
```

In this implementation:

- Time Complexity: `O(n^2)`
- Space Complexity: `O(1)`

We can see the time complexity is pretty bad and is there a way to optimize this ?

The answer is yes. How are going to do it ? Let's see:

In the above implementation, for example, when `i` increases from `6` to `7`, both `left` and `right` pointer iterated thru the list once, which is the most time-consuming part. Is there a way we could optimize this part ?

Perhaps you have already figure it out that we could use `Prefix Sum` to help memorize the duplicated operation and increase the performance.

How does `Prefix Sum` work in this case? Let's reuse the same example as above:

```
#     Y   Y    N   Y
#   | 
#       |
#           | <- suppose the store closes at this moment
#                |
#                     |
```

Let's divide the whole penalty score calculation into three different steps:

1. Calculate penalty score with no customers in the store, before the store closed
2. Calculate penalty score at the time store closed (Optional, based on the fashion Prefix Sum is constructed)
3. Calculate penalty score with customers in the store, after the store closed

So the Prefix Sum is effectly constructed based on the calculation method of penalty score, and in this case:

For Step `#1`, it is just to retrieve the penalty score created using data with **there are no customers**. Similarly, for Step `#3` retrieve the penalty score created using data with **there are customers**

#### Solution 2: Prefix Sum

```python
class Solution_PrefixSum:
    def bestClosingTime(self, customers: str) -> int:

        prefix_sum = self.getPrefixedSum(customers)
        suffix_sum = self.getSuffixedSum(customers)

        min_p, min_t = len(customers), len(customers)
        for i in range(len(customers) + 1):

            curr_p = prefix_sum[i] + (1 if 0 <= i < len(customers) and customers[i] == 'Y' else 0) + suffix_sum[len(customers)] - suffix_sum[i]

            if curr_p < min_p:
                min_p = curr_p
                min_t = i

        return min_t

    def getPrefixedSum(self, customers):
        prefix_sum = [0]
        for i in range(len(customers) + 1):
            if i >= len(customers):
                prefix_sum.append(prefix_sum[-1])
                continue

            if customers[i] == 'N':
                prefix_sum.append(prefix_sum[-1] + 1)
            else:
                prefix_sum.append(prefix_sum[-1])

        return prefix_sum

    def getSuffixedSum(self, customers):
        suffix_sum = [0]
        for i in range(len(customers)):
            if i >= len(customers):
                suffix_sum.append(suffix_sum[-1])
                continue

            if customers[i] == 'Y':
                suffix_sum.append(suffix_sum[-1] + 1)
            else:
                suffix_sum.append(suffix_sum[-1])

        return suffix_sum
```

The reason there is a suffix sum above is just to distinguish the different calculation method.

The Complexity analysis for this implementation is:

- Time Complexity: `O(n)`
- Space Complexity: `O(n)`
