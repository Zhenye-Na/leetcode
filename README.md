<h3 align="center"><strong>LeetCode Problems</strong></h3>

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

### DFS
#### Catlan Number

Unique Binary Search Trees


LC 241 Different Ways to Add Parentheses
LC 95 Unique Binary Search Trees II



### Dynamic Programming

> 以下题目来自大佬 [wisdompeak](https://github.com/wisdompeak) 总结
>
> Youtube: [残酷刷题群算法小讲座：动态规划的套路 by wisdompeak](https://www.youtube.com/watch?v=FLbqgyJ-70I&ab_channel=HuifengGuan). 讲的真的特别的好, 有刷题基础的 DP 一天十道没问题


#### 时间序列类

##### 套路I: 状态与前一个时间序列的状态有关, 可以是一维或者二维DP, 第一维表示序列，第二维表示状态数量

* LC 198. House Robber
* LC 213. House Robber II
* LC 123. Best Time to Buy and Sell Stock III
* LC 309. Best Time to Buy and Sell Stock with Cooldown
* LC 376. Wiggle Subsequence
* LC 276. Paint Fence
* LC 487. Max Consecutive Ones II
* LC 1186. Maximum Subarray Sum with One Deletion
* 903.Valid Permutations for DI Sequence


##### 套路II: 状态与前几个序列的状态有关, 至少是二维DP, 第二个维度表示当前最优与前面哪个状态有关

* LC 300. Longest Increasing Subsequence
* LC 368. Largest Divisible Subset
* LC 1105. Filling Bookcase Shelves
* 983.Minimum Cost For Tickets


##### 套路III: 状态与两个序列的状态有关, 至少是二维DP, 两个维度表示两个序列

* LC1143: Longest Common Subsequences
* LC1092: Common Supersequences
* LC72: Edit Distance
* LC97: Interleaving String
* LC115. Distinct Subsequences
* LC 727.Minimum Window Subsequence


##### LCS/SCS 变种

* 583 Delete Operation for Two Strings
* 712 Minimum ASCII Delete Sum for Two Strings
* 1035 Uncrossed Lines
* 1216 valid-palindrome-iii
* 1312 Minimum Insertion Steps to Make a String Palindrome


#### 区间类

第 I 类区间型 DP

给出一个序列, 明确要求分割成 K 个连续区间, 然后计算这些区间的最优性质

套路

- 状态定义: `dp[i][k]` 表示针对` s[1:i]` 分成 `k` 个区间, 此时能够得到的最优解
- 搜寻最后一个区间的起始位置 `j`, 将 `dp[i][k]` 分割成 `dp[j - 1][k - 1]` 和 `s[j][i]` 两部分
- 最终结果是 `dp[N][K]`

##### 套路IV: 状态与之前分割的区间有关, 至少二维DP, 第二个维度表示前面分割的数量

* LC 1278. Palindrome Partitioning III
* LC 813. Largest Sum of Averages
* LC 410. Split Array Largest Sum
* LC 1335. Minimum Difficulty of a Job Schedule

##### 套路V: 大区间的最优值依赖与小区间状态, 至少二维DP, 两个维度表示区间[i,j]的最优解

* LC 516. Longest Palindromic Subsequence
* LC 312. Burst Balloons
* LC 375. Guess Number Higher or Lower II
* LC 375. Guess Number Higher or Lower II
* LC 1246. Palindrome Removal

##### 融合两类的 boss 题目

LC 1000. Minimum Cost to Merge Stones -> `dp[i][j][k]`表示将区间`[i:j]`归并成`k`堆的最小代价

##### 套路VI: 背包类, 最少二维dp, 前i个物品, 代价为j的时候的最优值

* LC 494. Target
* LC 1049. Last Stone Weight II
* LC 474.Ones and Zeroes
* LC 879. Profitable Schemes
* LC 956. Tallest Billboard
* 518.Coin Change 2

#### Others
##### 状态压缩: 状态进行编码作为dp的一个维度来记录状态

* LC 691. Stickers to Spell Word
* LC 1349. Maximum Students Taking Exam
* 943.Find the Shortest Superstring

#### 弃坑型: 一眼看不出是DP，状态不好涉及

* 887.Super Egg Drop
* 920.Number of Music Playlists


范围内取出中间的数, 分别计算左右两边的, 再总体求最大/最小值

* [375] Guess Number Higher or Lower II
* [312] Burst Balloons

## Resources

- [Leetcode 分类顺序表第二版 (增加重点 250 题)](https://cspiration.com/leetcodeClassification)
- [LeetCode 加锁题目](https://leetcode.jp/problems.php)
- [某章算法配套题目联系 ladder](https://lc.jiuzhang.com/problem)


<!-- webstyle : https://github.com/riggraz/no-style-please -->

## LeetCode Contest

Weekly Contest 141

* 1089.Duplicate Zeros
* 1090.Largest Values From Labels
* 1091.Shortest Path in Binary Matrix
* 1092.Shortest Common Supersequence

Weekly Contest 248

* 1920.Build Array from Permutation
* 1921.Eliminate Maximum Number of Monsters
* 1922.Count Good Numbers
