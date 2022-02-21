---
layout: post
title: "169. Majority Element"
category: array
---


## Problem Description

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than `⌊n / 2⌋` times. You may assume that the majority element always exists in the array.

Example 1:

```
Input: nums = [3,2,3]
Output: 3
```

Example 2:

```
Input: nums = [2,2,1,1,1,2,2]
Output: 2
```

Constraints:

```
n == nums.length
1 <= n <= 5 * 104
-2^31 <= nums[i] <= 2^31 - 1
```

Follow-up: Could you solve the problem in linear time and in O(1) space?


## Solution

### Solution 1: HashMap

This is the intuitive way to solve this problem, we can use Python's built-in `Collections.Counter()` class to easily solve it


```python
class Solution:
    def majorityElement_HashMap(self, nums: List[int]) -> int:
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)
```

Note: we dont even need to check if number of occurrences is greater than `floor(n // 2)` since we can always return the element that has the greatest occurrences


### Solution 2: Misra-Gries Family of Algorithms - MAJORITY problem

We have two variables that we store. The first-variable is the key (which is either a member of `1, 2, ..., m` or a `null-entity`). The second-variable is an integer (which is a `count`). We start with an `empty` key, and a count of `zero`.

Every time an element `a_i = j` of the data-stream is observed,

- If the key is `empty` we set the value of the key to `j`, and we initialize the count to `1`.
- If the key is not empty, and equal to `j`, we increment the count by `1`.
- If the key is not empty, and not equal to `j`, we decrement the count by `1`
- If the count becomes `zero` as a result of this decrementing, we set the key to `null-entity`.

```python
class Solution:
    def majorityElement_Misra_Gries_Algorithm(self, nums: List[int]) -> int:
        key, count = None, 0
        for num in nums:
            if not key:
                key, count = num, 1
            else:
                if key == num:
                    count += 1
                else:
                    count -= 1

            if count == 0:
                key = None

        return key
```

This about it to see if it makes sense, if you are still confused about this algorithm, think about it this way:

There is guarantee that the majority element exists in this array, and the occurrence of it is greater than `floor(n // 2)`, which means, all the other numbers in this array, the total/sumed-up occurences of them is still lower than the occurrences of majority element

```
Count(majority_element) > Count(remaining_elements)
```
