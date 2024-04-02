---
layout: post
title: "287. Find the Duplicate Number"
category: array
---

## Problem Description

Given an array of integers `nums` containing `n + 1` integers where each integer is in the range `[1, n]` inclusive.

There is only one repeated number in `nums`, return this repeated number.

> You must solve the problem without modifying the array `nums` and uses only constant extra space.

**Example 1:**

```
Input: nums = [1,3,4,2,2]
Output: 2
```

**Example 2:**

```
Input: nums = [3,1,3,4,2]
Output: 3
```

**Example 3:**

```
Input: nums = [3,3,3,3,3]
Output: 3
```

**Constraints:**

```
1 <= n <= 10^5
nums.length == n + 1
1 <= nums[i] <= n
All the integers in nums appear only once except for precisely one integer which appears two or more times.
```

**Follow up:**

- How can we prove that at least one duplicate number must exist in nums?
- Can you solve the problem in linear runtime complexity?


## Binary Search

### Explanation

In this approach, we'll use binary search to find the duplicate number. We'll set a range from `1` to `n`, and then iteratively narrow down the range by halving it. We'll count the number of elements in the array that fall within the current range. If the count exceeds the range, then the duplicate number lies within that range. We'll update the range accordingly and continue until we find the duplicate number.

### Implementation

```python
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        low, high = 1, len(nums) - 1

        while low < high:
            mid = (low + high) // 2
            count = sum(num <= mid for num in nums)

            if count > mid:
                high = mid
            else:
                low = mid + 1

        return low
```

**Complexity Analysis**

- Time Complexity: `O(n * log(n))`
- Space Complexity: `O(1)`

## Bit Manipulation

### Explanation

In this approach, we'll use bit manipulation to find the duplicate number. We'll iterate over each bit position from the least significant bit to the most significant bit. For each position, we'll count the number of set bits among the elements in the array. If the count of set bits exceeds the count of unset bits, then the duplicate number has a set bit at that position.

### Implementation

```python
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums) - 1
        duplicate = 0

        for bit in range(32):
            mask = 1 << bit
            count_set = sum(num & mask for num in nums)
            count_unset = n + 1 - sum((num >> bit) & 1 for num in nums)

            if count_set > count_unset:
                duplicate |= mask

        return duplicate
```

**Complexity Analysis**

- Time Complexity: `O(n * log(m))`, where `m` is the maximum number of bits required to represent any number in the array
- Space Complexity: `O(1)`

## Two Pointers / Floyd's Tortoise and Hare Algorithm

### Explanation

In this approach, we'll use two pointers to detect a cycle in the array. We'll treat the array as a linked list where each element points to the element at its index. We'll initialize two pointers, slow and fast, and move them through the array. If there is a duplicate number, it will create a cycle in the linked list. We'll use Floyd's Tortoise and Hare Algorithm to detect the cycle and find the duplicate number.

```python
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow
```

**Complexity Analysis**

- Time Complexity: `O(n)`
- Space Complexity: `O(1)`
