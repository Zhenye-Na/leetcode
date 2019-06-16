#
# @lc app=leetcode id=1092 lang=python3
#
# [1092] Shortest Path in Binary Matrix
#

"""
Given two strings str1 and str2, return the shortest string that has both str1 and str2 as subsequences.  If multiple answers exist, you may return any of them.

(A string S is a subsequence of string T if deleting some number of characters from T (possibly 0, and the characters are chosen anywhere from T) results in the string S.)


Example 1:

Input: str1 = "abac", str2 = "cab"
Output: "cabac"
Explanation: 
str1 = "abac" is a substring of "cabac" because we can delete the first "c".
str2 = "cab" is a substring of "cabac" because we can delete the last "ac".
The answer provided is the shortest such string that satisfies these properties.
 

Note:

1 <= str1.length, str2.length <= 1000
str1 and str2 consist of lowercase English letters.
"""

class Solution(object):
    def shortestCommonSupersequence(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        m = len(str1) 
        n = len(str2) 
        dp = [[0] * (n + 2) for i in range(m + 2)] 
        self.lcs(str1, str2, m, n, dp) 

        result = []
        index = dp[m][n]
        i, j = m, n
        while i > 0 and j > 0:
            if str1[i - 1] == str2[j - 1]:
                result.append(str1[i - 1])
  
                i -= 1
                j -= 1
                index -= 1
        
            elif dp[i - 1][j] > dp[i][j - 1]:
                result.append(str2[j - 1])
                
                j -= 1
                index -= 1

            else:
                result.append(str1[i - 1])
                
                i -= 1
                index -= 1

        print("".join(result[::-1]))
        while i > 0:
            result.append(str1[i - 1])
            i -= 1
            index -= 1

        print("".join(result[::-1]))
        while j > 0:
            result.append(str2[j - 1])
            j -= 1
            index -= 1
                
        return "".join(result[::-1])
                
                
    # Returns length of LCS for 
    # X[0..m - 1], Y[0..n - 1]
    def lcs(self, X, Y, m, n, dp): 

        # Following steps build L[m + 1][n + 1] 
        # in bottom up fashion. Note that L[i][j] 
        # contains length of LCS of X[0..i - 1] 
        # and Y[0..j - 1] 
        for i in range(m + 1): 

            for j in range(n + 1): 

                if i == 0:
                    dp[i][j] = j
                elif j == 0: 
                    dp[i][j] = i
                elif X[i - 1] == Y[j - 1]:

                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:

                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1])
