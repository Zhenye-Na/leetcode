--
-- @lc app=leetcode id=180 lang=mysql
--
-- [180] Consecutive Numbers
--
-- https://leetcode.com/problems/consecutive-numbers/description/
--
-- database
-- Medium (34.97%)
-- Likes:    333
-- Dislikes: 88
-- Total Accepted:    74.2K
-- Total Submissions: 200K
-- Testcase Example:  '{"headers": {"Logs": ["Id", "Num"]}, "rows": {"Logs": [[1, 1], [2, 1], [3, 1], [4, 2], [5, 1], [6, 2], [7, 2]]}}'
--
-- Write a SQL query to find all numbers that appear at least three times
-- consecutively.
-- 
-- 
-- +----+-----+
-- | Id | Num |
-- +----+-----+
-- | 1  |  1  |
-- | 2  |  1  |
-- | 3  |  1  |
-- | 4  |  2  |
-- | 5  |  1  |
-- | 6  |  2  |
-- | 7  |  2  |
-- +----+-----+
-- 
-- 
-- For example, given the above Logs table, 1 is the only number that appears
-- consecutively for at least three times.
-- 
-- 
-- +-----------------+
-- | ConsecutiveNums |
-- +-----------------+
-- | 1               |
-- +-----------------+
-- 
-- 
--

-- @lc code=start
# Write your MySQL query statement below
SELECT DISTINCT l1.Num AS ConsecutiveNums
FROM Logs AS l1, Logs AS l2, Logs AS l3
WHERE l1.Num = l2.Num AND l2.Num = l3.Num AND l1.Id - l2.Id = 1 AND l2.Id - l3.Id = 1
ORDER BY l1.Num
;
-- @lc code=end

