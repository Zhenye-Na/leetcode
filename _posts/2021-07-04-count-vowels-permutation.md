---
layout: post
title: "1220. Count Vowels Permutation"
category: dp
---


## Problem Description

Given an integer n, your task is to count how many strings of length n can be formed under the following rules:

- Each character is a lower case vowel ('a', 'e', 'i', 'o', 'u')
- Each vowel 'a' may only be followed by an 'e'.
- Each vowel 'e' may only be followed by an 'a' or an 'i'.
- Each vowel 'i' may not be followed by another 'i'.
- Each vowel 'o' may only be followed by an 'i' or a 'u'.
- Each vowel 'u' may only be followed by an 'a'.

Since the answer may be too large, return it modulo 10^9 + 7.

Example 1:

```
Input: n = 1
Output: 5
Explanation: All possible strings are: "a", "e", "i" , "o" and "u".
```

Example 2:

```
Input: n = 2
Output: 10
Explanation: All possible strings are: "ae", "ea", "ei", "ia", "ie", "io", "iu", "oi", "ou" and "ua".
```

Example 3: 

```
Input: n = 5
Output: 68
```



## Solution

We used Dynamic Programming to solve this problem.

DP array `f[i][j]` represents that the number of different combination of string (length = i), ending with the j-th vowel

then based on the rules of what character can be or cannot be followed by the other characters. We update the rule to update `f[i + 1][j]`


### Java

```java
class Solution {
    public int countVowelPermutation(int n) {
        if (n == 0)
            return 0;

        // dp initialization
        // f[i][j], string length == i, ending with vowel[j]
        long[][] f = new long[n][5];

        for (int j = 0; j < 5; j++)
            f[0][j] = 1;

        int a = 0, e = 1, i = 2, o = 3, u = 4;
        int mod = (int) Math.pow(10, 9) + 7;

        for (int r = 1; r < n; r++) {
            f[r][a] = (f[r - 1][e] + f[r - 1][i] + f[r - 1][u]) % mod;
            f[r][e] = (f[r - 1][a] + f[r - 1][i]) % mod;
            f[r][i] = (f[r - 1][e] + f[r - 1][o]) % mod;
            f[r][o] = (f[r - 1][i]) % mod;
            f[r][u] = (f[r - 1][i] + f[r - 1][o]) % mod;
        }

        long res = 0;
        for (int j = 0; j < 5; j++)
            res = (res + f[n - 1][j]) % mod;

        return (int) res;
    }
}
```

### Python

```python
class Solution:
    def countVowelPermutation(self, n: int) -> int:
        if not n or n == 0:
            return 0

        # dp initializtion
        # f[i][j] represents a i-length string ending with vowel[j]
        f = [[0 for _ in range(5)] for _ in range(n)]

        for j in range(5):
            f[0][j] = 1

        for i in range(1, n):
            for j in range(5):
                f[i][0] = f[i - 1][1] + f[i - 1][2] + f[i - 1][4]
                f[i][1] = f[i - 1][0] + f[i - 1][2]
                f[i][2] = f[i - 1][1] + f[i - 1][3]
                f[i][3] = f[i - 1][2]
                f[i][4] = f[i - 1][2] + f[i - 1][3]

        res = sum(f[-1])
        return res % (10 ** 9 + 7)
```

**Complexity Analysis**

- Time Complexity
  - O(n*5) = O(n) if n is much greater than 5
- Space Complexity
  - O(n*5) = O(n) if n is much greater than 5
