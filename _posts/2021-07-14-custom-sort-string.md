---
layout: post
title: "791. Custom Sort String"
category: hashmap
---


## Problem Description

order and str are strings composed of lowercase letters. In order, no letter occurs more than once.

order was sorted in some custom order previously. We want to permute the characters of str so that they match the order that order was sorted. More specifically, if x occurs before y in order, then x should occur before y in the returned string.

Return any permutation of str (as a string) that satisfies this property.

Example:

```
Input: 
order = "cba"
str = "abcd"
Output: "cbad"
Explanation: 
"a", "b", "c" appear in order, so the order of "a", "b", "c" should be "c", "b", and "a". 
Since "d" does not appear in order, it can be at any position in the returned string. "dcba", "cdba", "cbda" are also valid outputs.
```

Note:

```
order has length at most 26, and no character is repeated in order.
str has length at most 200.
order and str consist of lowercase letters only.
```

## Solution

### Python

```python
from collections import Counter

class Solution:
    def customSortString(self, order: str, str: str) -> str:
        if not order or not str or len(str) == 0:
            return str

        counter = Counter(str)
        
        res = ""
        for char in order:
            if char in counter:
                res += counter[char] * char
                del counter[char]

        for char in counter:
            res += char * counter[char]
                
        return res
```

### Java

```java
class Solution {
    public String customSortString(String order, String str) {
       HashMap<Character, Integer> map = new HashMap<Character, Integer>();
        String ans = "";
        for (int i = 0 ; i< str.length(); i++) {
            map.put(str.charAt(i), map.getOrDefault( str.charAt(i), 0 ) + 1);
        }

        for (int i = 0; i < order.length(); i++) {
            char oo = order.charAt(i);
            if ( !map.containsKey(oo) )       
                continue;
            
            for (int j = 0; j < map.get(oo); j++)
                ans += oo;    
            map.remove(oo);         
        }

        for (Character key : map.keySet()) {
            int freq = map.get(key);
            for (int j = 0; j < freq; j++)
                ans += key;
        }

        return ans;
    }
}
```

**Complexity Analysis**

- Time Complexity
  - O(n)
- Space Complexity
  - O(n)

