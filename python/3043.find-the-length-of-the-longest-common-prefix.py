from collections import deque
from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.origin = set([])
        self.is_number = False
        self.numbers = []


class PrefixTrie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, num_in_str, origin):
        node = self.root
        for char in num_in_str:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]

            node.origin.add(origin)
            node.numbers.append(num_in_str)
        node.is_number = True

    def search_longest_prefix(self):
        prefix = 0
        queue = deque([self.root])

        depth = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                if len(node.origin) == 2:
                    prefix = max(prefix, depth)
                for child in node.children:
                    queue.append(node.children[child])

            depth += 1

        return prefix


class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        trie = PrefixTrie()

        for num in arr1:
            trie.insert(list(str(num)), "arr1")

        for num in arr2:
            trie.insert(list(str(num)), "arr2")

        return trie.search_longest_prefix()
