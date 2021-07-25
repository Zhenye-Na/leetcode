---
layout: post
title: "126. Word Ladder II"
category: dfs
---


## Problem Description

A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words `beginWord -> s1 -> s2 -> ... -> sk` such that:

```
Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return all the shortest transformation sequences from beginWord to endWord, or an empty list if no such sequence exists. Each sequence should be returned as a list of the words [beginWord, s1, s2, ..., sk].
```
 

Example 1:

```
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
Explanation: There are 2 shortest transformation sequences:
"hit" -> "hot" -> "dot" -> "dog" -> "cog"
"hit" -> "hot" -> "lot" -> "log" -> "cog"
```

Example 2:

```
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: []
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
```

Constraints:

```
1 <= beginWord.length <= 5
endWord.length == beginWord.length
1 <= wordList.length <= 1000
wordList[i].length == beginWord.length
beginWord, endWord, and wordList[i] consist of lowercase English letters.
beginWord != endWord
All the words in wordList are unique.
```

## Solution



### Python

```python
from collections import deque, defaultdict

class Solution:

    def __init__(self):
        self.distance = {}
        self.neighbors = {}


    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        path = []
        if not self.find_ladder_length(beginWord, endWord, wordList):
            return path

        self.dfs(path, endWord, [], beginWord)
        return path


    def dfs(self, result, end, curr_path, curr_word):
        if curr_word == end:
            result.append(curr_path[:] + [curr_word])
            return

        for next_word in self.neighbors[curr_word]:
            if next_word in self.distance and self.distance[next_word] < self.distance[curr_word]:
                curr_path.append(curr_word)
                self.dfs(result, end, curr_path, next_word)
                curr_path.pop()


    def find_ladder_length(self, beginWord, endWord, wordList):
        if not beginWord or len(beginWord) == 0 or \
            not endWord or len(endWord) == 0 or \
            not wordList or len(wordList) == 0 or \
            len(beginWord) != len(endWord):
            return False


        wordList = set(wordList)
        wordList.add(beginWord)
        word_queue = deque([endWord])
        seen = set([endWord])
        steps = 1

        while word_queue:
            size = len(word_queue)
            for _ in range(size):
                curr_word = word_queue.popleft()
                self.distance[curr_word] = steps
                next_words = self._gen_new_words(curr_word, wordList)
                self.neighbors[curr_word] = next_words
                if curr_word == beginWord:
                    return True

                for next_word in next_words:
                    if next_word not in seen:
                        word_queue.append(next_word)
                        seen.add(next_word)

            steps += 1

        return False


    def _gen_new_words(self, curr_word, wordList):
        new_words = []
        for i in range(len(curr_word)):
            for code in 'abcdefghijklmnopqrstuvwxyz':
                if curr_word[i] == code:
                    continue
                tmp_word = curr_word[:i] + code + curr_word[i + 1:]
                if tmp_word in wordList:
                    new_words.append(tmp_word)
                    # wordList.remove(tmp_word)

        return new_words
```

### Java

```java
class Solution {
    private Map<String, Set<String>> graph;
    private List<List<String>> result;
    private Map<String, Integer> distance;
    
    public List<List<String>> findLadders(String beginWord, String endWord, List<String> wordList) {
        distance = new HashMap<>();
        graph = buildGraph(beginWord, wordList);
        result = new ArrayList<>();
        dfs(beginWord, endWord,  new ArrayList<>());
        return result;
    }
    
    private void dfs(String word, String target, List<String> solution) {
        solution.add(word);
        if (target.equals(word)) {
            result.add(solution);
        } else {
            for (String child : graph.get(word)) {
                if (distance.get(word) + 1 == distance.getOrDefault(child, Integer.MAX_VALUE)) { 
                    dfs(child, target, new ArrayList<>(solution));
                }
            }
        }
    }
    
    private Map<String, Set<String>> buildGraph(String beginWord, List<String> wordList) {
        Map<String, Set<String>> map = new HashMap<>();
        Queue<String> queue = new LinkedList<>();
        queue.add(beginWord);
        distance.put(beginWord, 0);
        while (!queue.isEmpty()) {
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                String word = queue.poll();
                Set<String> set = map.getOrDefault(word, new HashSet<>());
                map.put(word, set);
                for (String s : wordList) {
                    int cnt = 0;
                    for (int j = 0; j < word.length(); j++) {
                        if (s.charAt(j) != word.charAt(j)) {
                            cnt++;
                        }
                    }
                    if (cnt == 1) {
                        if (!distance.containsKey(s)) {
                            queue.add(s);
                            distance.put(s, distance.get(word) + 1);
                        }
                        set.add(s);
                    }
                }
            }
        }
        return map;
    }
    
}
```


**Complexity Analysis**

[here](https://leetcode.com/problems/word-ladder-ii/solution/)

