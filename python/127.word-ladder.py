#
# @lc app=leetcode id=127 lang=python3
#
# [127] Word Ladder
#
# https://leetcode.com/problems/word-ladder/description/
#
# algorithms
# Hard (31.55%)
# Likes:    4766
# Dislikes: 1402
# Total Accepted:    555.3K
# Total Submissions: 1.7M
# Testcase Example:  '"hit"\n"cog"\n["hot","dot","dog","lot","log","cog"]'
#
# A transformation sequence from word beginWord to word endWord using a
# dictionary wordList is a sequence of words such that:
# 
# 
# The first word in the sequence is beginWord.
# The last word in the sequence is endWord.
# Only one letter is different between each adjacent pair of words in the
# sequence.
# Every word in the sequence is in wordList.
# 
# 
# Given two words, beginWord and endWord, and a dictionary wordList, return the
# number of words in the shortest transformation sequence from beginWord to
# endWord, or 0 if no such sequence exists.
# 
# 
# Example 1:
# 
# 
# Input: beginWord = "hit", endWord = "cog", wordList =
# ["hot","dot","dog","lot","log","cog"]
# Output: 5
# Explanation: One shortest transformation is "hit" -> "hot" -> "dot" -> "dog"
# -> "cog" with 5 words.
# 
# 
# Example 2:
# 
# 
# Input: beginWord = "hit", endWord = "cog", wordList =
# ["hot","dot","dog","lot","log"]
# Output: 0
# Explanation: The endWord "cog" is not in wordList, therefore there is no
# possible transformation.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= beginWord.length <= 10
# endWord.length == beginWord.length
# 1 <= wordList.length <= 5000
# wordList[i].length == beginWord.length
# beginWord, endWord, and wordList[i] consist of lowercase English letters.
# beginWord != endWord
# All the strings in wordList are unique.
# 
# 
#

# @lc code=start
from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not beginWord or len(beginWord) == 0 or \
            not endWord or len(endWord) == 0 or \
            not wordList or len(wordList) == 0 or \
            len(beginWord) != len(endWord) or \
            endWord not in wordList:
            return 0

        wordList = set(wordList)
        word_queue = deque([beginWord])
        seen = set([beginWord])
        steps = 1

        while word_queue:
            size = len(word_queue)
            for _ in range(size):
                curr_word = word_queue.popleft()
                if curr_word == endWord:
                    return steps

                next_words, wordList = self._gen_new_words(curr_word, wordList)
                for next_word in next_words:
                    if next_word not in seen:
                        word_queue.append(next_word)
                        seen.add(next_word)

            steps += 1

        return 0


    def _gen_new_words(self, curr_word, wordList):
        new_words = []
        for i in range(len(curr_word)):
            for code in 'abcdefghijklmnopqrstuvwxyz':
                if curr_word[i] == code:
                    continue
                tmp_word = curr_word[:i] + code + curr_word[i + 1:]
                if tmp_word in wordList:
                    new_words.append(tmp_word)
                    wordList.remove(tmp_word)

        return new_words, wordList
# @lc code=end

