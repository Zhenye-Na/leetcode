#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs or len(strs) == 0:
            return []

        strs.sort()
        mapping = {}
        for word in strs:
            sorted_word = ''.join(list(sorted(word)))
            mapping[sorted_word] = mapping.get(sorted_word, []) + [word]

        result = []
        for key_word in mapping:
            result.append(mapping[key_word])

        return result

