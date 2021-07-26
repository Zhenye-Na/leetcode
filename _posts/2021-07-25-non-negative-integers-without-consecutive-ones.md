---
layout: post
title: "600. Non-negative Integers without Consecutive Ones"
category: dp
---


## Problem Description

Given a positive integer n, return the number of the integers in the range [0, n] whose binary representations do not contain consecutive ones.

Example 1:

```
Input: n = 5
Output: 5
Explanation:
Here are the non-negative integers <= 5 with their corresponding binary representations:
0 : 0
1 : 1
2 : 10
3 : 11
4 : 100
5 : 101
Among them, only integer 3 disobeys the rule (two consecutive ones) and the other 5 satisfy the rule.
```

Example 2:

```
Input: n = 1
Output: 2
```

Example 3:

```
Input: n = 2
Output: 3
```

Constraints:

```
1 <= n <= 10^9
```


## Solution

Check this [video](https://www.youtube.com/watch?v=a9-NtLIs1Kk) out.


### Python

```python
class Solution:
    def findIntegers(self, n: int) -> int:
        if n < 2:
            return n + 1
        
        bits = bin(n).replace('0b', '')
        bits = bits[::-1]
        k = len(bits)
        
        f = [0] * k
        f[0] = 1
        f[1] = 2
        for i in range(2, k):
            f[i] = f[i - 1] + f[i - 2]
        
        ans = 0
        for i in range(k - 1, -1, -1):
            if bits[i] == '1':
                ans += f[i]
                if i < k - 1 and bits[i + 1] == '1':
                    return ans

        ans += 1
        return ans
```

### Java

```java
class Solution {
    public int findIntegers(int n) {
        StringBuilder sb = new StringBuilder(Integer.toBinaryString(n)).reverse();
        int n = sb.length();
        
        int a[] = new int[n];
        int b[] = new int[n];
        a[0] = b[0] = 1;
        for (int i = 1; i < n; i++) {
            a[i] = a[i - 1] + b[i - 1];
            b[i] = a[i - 1];
        }
        
        int result = a[n - 1] + b[n - 1];
        for (int i = n - 2; i >= 0; i--) {
            if (sb.charAt(i) == '1' && sb.charAt(i + 1) == '1') break;
            if (sb.charAt(i) == '0' && sb.charAt(i + 1) == '0') result -= b[i];
        }
        
        return result;
    }
}
```

**Complexity Analysis**

- Time Complexity
  - O(len(bits))
- Space Complexity
  - O(1)
