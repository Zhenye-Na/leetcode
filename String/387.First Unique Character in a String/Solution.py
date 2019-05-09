class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        mapping = {}

        if not s or len(s) <= 0:
            return -1

        for idx, char in enumerate(s):
            mapping[char] = mapping.get(char, 0) + 1

        for idx, key in enumerate(s):
            if mapping[key] == 1:
                return idx

        return -1
