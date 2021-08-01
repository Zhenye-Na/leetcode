---
layout: post
title: "677. Map Sum Pairs"
category: trie
---


## Problem Description

Implement the MapSum class:

- `MapSum()` Initializes the MapSum object.
- `void insert(String key, int val)` Inserts the key-val pair into the map. If the key already existed, the original key-value pair will be overridden to the new one.
- `int sum(string prefix)` Returns the sum of all the pairs' value whose key starts with the prefix.
 

Example 1:

```
Input
["MapSum", "insert", "sum", "insert", "sum"]
[[], ["apple", 3], ["ap"], ["app", 2], ["ap"]]
Output
[null, null, 3, null, 5]

Explanation
MapSum mapSum = new MapSum();
mapSum.insert("apple", 3);  
mapSum.sum("ap");           // return 3 (apple = 3)
mapSum.insert("app", 2);    
mapSum.sum("ap");           // return 5 (apple + app = 3 + 2 = 5)
```

Constraints:

```
1 <= key.length, prefix.length <= 50
key and prefix consist of only lowercase English letters.
1 <= val <= 1000
At most 50 calls will be made to insert and sum.
```


## Solution

- HashMap: storing the value of each string
- Trie: storing prefix information

### Python

```python
class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = Trie()
        self.d = {}

    def insert(self, key: str, val: int) -> None:
        if key in self.d:
            self.trie.add(key, val - self.d[key])
        else:
            self.trie.add(key, val)

        self.d[key] = val

    def sum(self, prefix: str) -> int:
        return self.trie.searchPrefix(prefix)


class TrieNode:

    def __init__(self):
        self.children = {}
        self.val = 0


class Trie:

    def __init__(self):
        self.root = TrieNode()
        self.mapping = {}

    def add(self, word, val):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
            node.val += val

    def searchPrefix(self, prefix):
        node = self.root
        for ch in prefix:
            node = node.children.get(ch)
            if node is None:
                return 0

        return node.val


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
```

### Java


```java
class TrieNode {
    public HashMap<Character, TrieNode> children;
    public int value;

    public TrieNode() {
        this.value = 0;
        this.children = new HashMap<>();
    }
}

class Trie {
    public TrieNode root;

    public Trie() {
        this.root = new TrieNode();
    }

    public void add(String key, int val) {
        TrieNode node = this.root;
        int length = key.length();
        for (int i = 0; i < length; i++) {
            if (!node.children.containsKey(key.charAt(i))) {
                node.children.put(key.charAt(i), new TrieNode());
            }
            node = node.children.get(key.charAt(i));
            node.value += val;
        }

    }


    public int search(String prefix) {
        TrieNode node = this.root;
        int length = prefix.length();
        for (int i = 0; i < length; i++) {
            if (!node.children.containsKey(prefix.charAt(i))) {
                return 0;
            }
            node = node.children.get(prefix.charAt(i));
        }

        return node.value;

    }

}



class MapSum {

    private Trie trie;
    private HashMap<String, Integer> record;

    /** Initialize your data structure here. */
    public MapSum() {
        this.trie = new Trie();
        this.record = new HashMap<>();
    }
    
    public void insert(String key, int val) {
        if (!this.record.containsKey(key)) {
            this.trie.add(key, val);
        } else {
            this.trie.add(key, val - this.record.get(key));
        }

        this.record.put(key, val);
    }
    
    public int sum(String prefix) {
        return this.trie.search(prefix);
    }
}

/**
 * Your MapSum object will be instantiated and called as such:
 * MapSum obj = new MapSum();
 * obj.insert(key,val);
 * int param_2 = obj.sum(prefix);
 */
```



**Complexity Analysis**

- Time Complexity
  - O(NL)
    - N: number of strings / number of `insert()` api calls
    - L: average length of input strings
- Space Complexity
  - O(NL)
