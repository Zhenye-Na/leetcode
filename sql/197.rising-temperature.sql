--
-- @lc app=leetcode id=197 lang=mysql
--
-- [197] Rising Temperature
--
-- https://leetcode.com/problems/rising-temperature/description/
--
-- database
-- Easy (35.72%)
-- Likes:    318
-- Dislikes: 152
-- Total Accepted:    99.9K
-- Total Submissions: 270.2K
-- Testcase Example:  '{"headers": {"Weather": ["Id", "RecordDate", "Temperature"]}, "rows": {"Weather": [[1, "2015-01-01", 10], [2, "2015-01-02", 25], [3, "2015-01-03", 20], [4, "2015-01-04", 30]]}}'
--
-- Given a Weather table, write a SQL query to find all dates' Ids with higher
-- temperature compared to its previous (yesterday's) dates.
-- 
-- 
-- +---------+------------------+------------------+
-- | Id(INT) | RecordDate(DATE) | Temperature(INT) |
-- +---------+------------------+------------------+
-- |       1 |       2015-01-01 |               10 |
-- |       2 |       2015-01-02 |               25 |
-- |       3 |       2015-01-03 |               20 |
-- |       4 |       2015-01-04 |               30 |
-- +---------+------------------+------------------+
-- 
-- 
-- For example, return the following Ids for the above Weather table:
-- 
-- 
-- +----+
-- | Id |
-- +----+
-- |  2 |
-- |  4 |
-- +----+
-- 
-- 
--

-- @lc code=start
# Write your MySQL query statement below
SELECT w1.Id
FROM Weather AS w1, Weather AS w2
WHERE TO_DAYS(w1.RecordDate) - TO_DAYS(w2.RecordDate) = 1 AND w1.Temperature > w2.Temperature
;

-- @lc code=end

