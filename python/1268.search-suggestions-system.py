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
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.words = []


class Trie:
    def __init__(self):
        self.root = TrieNode()


    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.words.append(word)

        node.is_word = True


    def search_word(self, word):
        """
        Given a word of a word, output the words with same prefix
        """
        if not word or len(word) == 0:
            return []

        ret = []

        length = len(word)
        node = self.root
        word_lst = []

        curr_position = -1
        for i in range(length):
            char = word[i]
            if char in node.children:
                word_lst = node.children.get(char).words
                word_lst.sort()
                ret.append(word_lst[:3] if len(word_lst) > 3 else word_lst)
                node.children[char].words = word_lst
                
                node = node.children[char]
            else:
                curr_position = i
                break
  
        if curr_position != -1:
            for j in range(curr_position, length):
                ret.append([])

        return ret


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie()
        for product in products:
            trie.insert(product)

        return trie.search_word(searchWord)
# @lc code=end

