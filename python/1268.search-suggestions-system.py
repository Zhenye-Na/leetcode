#
# @lc app=leetcode id=1268 lang=python3
#
# [1268] Search Suggestions System
#
# https://leetcode.com/problems/search-suggestions-system/description/
#
# algorithms
# Medium (64.53%)
# Likes:    1215
# Dislikes: 98
# Total Accepted:    88.9K
# Total Submissions: 135.7K
# Testcase Example:  '["mobile","mouse","moneypot","monitor","mousepad"]\r\n"mouse"\r'
#
# Given an array of strings products and a string searchWord. We want to design
# a system that suggests at most three product names from products after each
# character of searchWord is typed. Suggested products should have common
# prefix with the searchWord. If there are more than three products with a
# common prefix return the three lexicographically minimums products.
# 
# Return list of lists of the suggested products after each character of
# searchWord is typed. 
# 
# 
# Example 1:
# 
# 
# Input: products = ["mobile","mouse","moneypot","monitor","mousepad"],
# searchWord = "mouse"
# Output: [
# ["mobile","moneypot","monitor"],
# ["mobile","moneypot","monitor"],
# ["mouse","mousepad"],
# ["mouse","mousepad"],
# ["mouse","mousepad"]
# ]
# Explanation: products sorted lexicographically =
# ["mobile","moneypot","monitor","mouse","mousepad"]
# After typing m and mo all products match and we show user
# ["mobile","moneypot","monitor"]
# After typing mou, mous and mouse the system suggests ["mouse","mousepad"]
# 
# 
# Example 2:
# 
# 
# Input: products = ["havana"], searchWord = "havana"
# Output: [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]
# 
# 
# Example 3:
# 
# 
# Input: products = ["bags","baggage","banner","box","cloths"], searchWord =
# "bags"
# Output:
# [["baggage","bags","banner"],["baggage","bags","banner"],["baggage","bags"],["bags"]]
# 
# 
# Example 4:
# 
# 
# Input: products = ["havana"], searchWord = "tatiana"
# Output: [[],[],[],[],[],[],[]]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= products.length <= 1000
# There are no repeated elements in products.
# 1 <= Σ products[i].length <= 2 * 10^4
# All characters of products[i] are lower-case English letters.
# 1 <= searchWord.length <= 1000
# All characters of searchWord are lower-case English letters.
# 
# 
#

# @lc code=start

# Runtime 401 ms
# Memory 21.3 MB

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = []
        self.is_word = False


class Trie:
    def __init__(self, output_limit):
        self.root = TrieNode()
        self.output_limit = output_limit

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.word.append(word)

    def find_by_prefix(self, prefix):
        node = self.root
        result = []

        for char in prefix:
            node = node.children.get(char)
            if node is None:
                return []
            result = node.word[:]
        result.sort()
        return result[: self.output_limit]


class Solution:
    def suggestedProducts(
        self, products: List[str], searchWord: str
    ) -> List[List[str]]:

        trie = Trie(3)
        for product in products:
            trie.insert(product)

        outputs = []
        for i in range(1, len(searchWord) + 1):
            outputs.append(trie.find_by_prefix(searchWord[0:i]))

        return outputs



# Runtime 200 ms
# Memory 21.3 MB

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = []
        self.is_word = False


class Trie:
    def __init__(self, output_limit):
        self.root = TrieNode()
        self.output_limit = output_limit

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            if len(node.word) < 3:
                node.word.append(word)

    def find_by_prefix(self, node, char):

        if node is None:
            return [], None
        node = node.children.get(char)
        if node is None:
            return [], None
        return node.word[:], node


class Solution:
    def suggestedProducts(
        self, products: List[str], searchWord: str
    ) -> List[List[str]]:

        products.sort()

        trie = Trie(3)
        for product in products:
            trie.insert(product)

        outputs = []
        node = trie.root
        for i in range(len(searchWord)):
            results, node = trie.find_by_prefix(node, searchWord[i])
            outputs.append(results)

        return outputs
# @lc code=end

