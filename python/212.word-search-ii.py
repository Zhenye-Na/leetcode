#
# @lc app=leetcode id=212 lang=python3
#
# [212] Word Search II
#
# https://leetcode.com/problems/word-search-ii/description/
#
# algorithms
# Hard (36.67%)
# Likes:    3542
# Dislikes: 142
# Total Accepted:    287.3K
# Total Submissions: 770K
# Testcase Example:  '[["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]\n' +
#  '["oath","pea","eat","rain"]'
#
# Given an m x n board of characters and a list of strings words, return all
# words on the board.
# 
# Each word must be constructed from letters of sequentially adjacent cells,
# where adjacent cells are horizontally or vertically neighboring. The same
# letter cell may not be used more than once in a word.
# 
# 
# Example 1:
# 
# 
# Input: board =
# [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]],
# words = ["oath","pea","eat","rain"]
# Output: ["eat","oath"]
# 
# 
# Example 2:
# 
# 
# Input: board = [["a","b"],["c","d"]], words = ["abcb"]
# Output: []
# 
# 
# 
# Constraints:
# 
# 
# m == board.length
# n == board[i].length
# 1 <= m, n <= 12
# board[i][j] is a lowercase English letter.
# 1 <= words.length <= 3 * 10^4
# 1 <= words[i].length <= 10
# words[i] consists of lowercase English letters.
# All the strings of words are unique.
# 
# 
#

# @lc code=start
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.word = None


class Trie:
    def __init__(self):
        self.root = TrieNode()


    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children.get(char)

        node.is_word = True
        node.word = word


class Solution:

    def __init__(self):
        self.dx = [1, -1, 0, 0]
        self.dy = [0, 0, 1, -1]

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        self.m, self.n = len(board), len(board[0])

        for word in words:
            if len(word) > self.m * self.n:
                continue
            trie.insert(word)


        res = []
        visited = set([])

        for i in range(self.m):
            for j in range(self.n):
                if trie.root.children.get(board[i][j]):
                    self._dfs(i, j, board, trie.root, res, visited)
        
        return res


    def _dfs(self, x, y, board, node, res, visited):
        if not self._check(x, y, visited):
            return

        curr_node = node.children.get(board[x][y], None)
        if not curr_node:
            return

        if curr_node.is_word:
            res.append(curr_node.word)
            curr_node.is_word = False

        visited.add((x, y))
        for d in range(4):
            self._dfs(x + self.dx[d], y + self.dy[d], board, curr_node, res, visited)
        visited.remove((x, y))


    def _check(self, x, y, visited):
        return 0 <= x < self.m and 0 <= y < self.n and (x, y) not in visited
# @lc code=end

