<h3 align="center"><strong>LeetCode Problems</strong></h3>



### DFS
#### Catlan Number

Unique Binary Search Trees


LC 241 Different Ways to Add Parentheses
LC 95 Unique Binary Search Trees II



### Dynamic Programming


范围内取出中间的, 计算两边的, 求最大/最小值

[375] Guess Number Higher or Lower II
[312] Burst Balloons

时间序列类：
    套路I: 状态与前一个时间序列的状态有关，可以是一维或者二维DP，第一维表示序列，第二维表示状态数量。
LC 198. House Robber
LC 213. House Robber II
LC 123. Best Time to Buy and Sell Stock III
LC 309. Best Time to Buy and Sell Stock with Cooldown
LC 376. Wiggle Subsequence
LC 276. Paint Fence
LC 487. Max Consecutive Ones II
LC 1186. Maximum Subarray Sum with One Deletion
903.Valid Permutations for DI Sequence


    套路II: 状态与前几个序列的状态有关，至少是二维DP，第二个维度表示当前最优与前面哪个状态有关。
LC 300. Longest Increasing Subsequence
LC 368. Largest Divisible Subset
LC 1105. Filling Bookcase Shelves
983.Minimum Cost For Tickets


    套路III：状态与两个序列的状态有关，至少是二维DP，两个维度表示两个序列
LC1143: Longest Common Subsequences
LC1092:   Common Supersequences
LC72: Edit Distance
LC97: Interleaving String
LC115. Distinct Subsequences
LC 727.Minimum Window Subsequence


    LCS/SCS 变种
583 Delete Operation for Two Strings
712 Minimum ASCII Delete Sum for Two Strings
1035 Uncrossed Lines
1216 valid-palindrome-iii
1312 Minimum Insertion Steps to Make a String Palindrome


区间类：
    套路IV: 状态与之前分割的区间有关，至少二维DP，第二个维度表示前面分割的数量。
LC 1278. Palindrome Partitioning III
LC 813. Largest Sum of Averages
LC 410. Split Array Largest Sum
LC 1335. Minimum Difficulty of a Job Schedule

    套路V: 大区间的最优值依赖与小区间状态，至少二维DP，两个维度表示区间[i,j]的最优解
LC 516. Longest Palindromic Subsequence
LC 312. Burst Balloons
LC 375. Guess Number Higher or Lower II
LC 375. Guess Number Higher or Lower II
LC 1246. Palindrome Removal

    融合两类的boss题目
 LC 1000. Minimum Cost to Merge Stones -> dp[i][j][k]表示将区间[i:j]归并成k堆的最小代价。

    套路VI: 背包类, 最少二维dp，前i个物品，代价为j的时候的最优值
LC 494. Target
LC 1049. Last Stone Weight II
LC 474.Ones and Zeroes
LC 879. Profitable Schemes
LC 956. Tallest Billboard
518.Coin Change 2

Others
    状态压缩: 状态进行编码作为dp的一个维度来记录状态
LC 691. Stickers to Spell Word
LC 1349. Maximum Students Taking Exam
943.Find the Shortest Superstring

    弃坑型: 一眼看不出是DP，状态不好涉及
887.Super Egg Drop
920.Number of Music Playlists




## Resources

- [Leetcode 分类顺序表第二版(增加重点250题)](https://cspiration.com/leetcodeClassification)
- [](https://lc.jiuzhang.com/problem)
- [](https://leetcode.jp/problems.php)
