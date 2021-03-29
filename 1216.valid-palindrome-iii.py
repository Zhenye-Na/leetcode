# 1216. Valid Palindrome III

# Given a string s and an integer k, find out if the given string is a K-Palindrome or not.

# A string is K-Palindrome if it can be transformed into a palindrome by
# removing at most k characters from it.

 
# Example 1:

# Input: s = "abcdeca", k = 2
# Output: true
# Explanation: Remove 'b' and 'e' characters.
 

# Constraints:

# 1 <= s.length <= 1000
# s has only lowercase English letters.
# 1 <= k <= s.length


class Solution:

    def isValidPalindrome(self, s, k):
        if not s or len(s) == 0:
            return True

        t = s[::-1]
        l = len(s)

        s = "#" + s
        t = "#" + t

        # dp initialization
        # f[i][j] represents how many deletes so that s[:i] and t[:j] are same
        # f[i][j] -> longest common subsequence
        f = [[0 for _ in range(l + 1)] for _ in range(l + 1)]

        for i in range(1, l + 1):
            for j in range(1, l + 1):
                if s[i] == t[j]:
                    f[i][j] = f[i - 1][j - 1] + 1
                else:
                    f[i][j] = max(
                        f[i - 1][j - 1],
                        f[i - 1][j],
                        f[i][j - 1]
                    )

        return l - f[l][l] <= k
        


solver = Solution()

print(solver.isValidPalindrome("abcdeca", 2))
print(solver.isValidPalindrome("racecar", 0))
print(solver.isValidPalindrome("aaaaabbbbb", 5))

