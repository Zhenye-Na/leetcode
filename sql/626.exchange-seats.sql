--
-- @lc app=leetcode id=626 lang=mysql
--
-- [626] Exchange Seats
--
-- https://leetcode.com/problems/exchange-seats/description/
--
-- database
-- Medium (55.75%)
-- Likes:    248
-- Dislikes: 212
-- Total Accepted:    37.4K
-- Total Submissions: 63.9K
-- Testcase Example:  '{"headers": {"seat": ["id","student"]}, "rows": {"seat": [[1,"Abbot"],[2,"Doris"],[3,"Emerson"],[4,"Green"],[5,"Jeames"]]}}'
--
-- Mary is a teacher in a middle school and she has a table seat storing
-- students' names and their corresponding seat ids.
-- The column id is continuous increment.
-- 
-- 
-- Mary wants to change seats for the adjacent students.
-- 
-- 
-- Can you write a SQL query to output the result for Mary?
-- 
-- 
-- 
-- 
-- +---------+---------+
-- |    id   | student |
-- +---------+---------+
-- |    1    | Abbot   |
-- |    2    | Doris   |
-- |    3    | Emerson |
-- |    4    | Green   |
-- |    5    | Jeames  |
-- +---------+---------+
-- 
-- For the sample input, the output is:
-- 
-- 
-- 
-- 
-- +---------+---------+
-- |    id   | student |
-- +---------+---------+
-- |    1    | Doris   |
-- |    2    | Abbot   |
-- |    3    | Green   |
-- |    4    | Emerson |
-- |    5    | Jeames  |
-- +---------+---------+
-- 
-- 
-- Note:
-- If the number of students is odd, there is no need to change the last one's
-- seat.
-- 
--

-- @lc code=start
# Write your MySQL query statement below
SELECT
  CASE
    WHEN seat.id % 2 = 1 AND seat.id = (SELECT COUNT(*) FROM seat) THEN seat.id
    WHEN seat.id % 2 = 0 THEN seat.id - 1
    ELSE seat.id + 1
  END AS id,
  student
FROM seat
ORDER BY id ASC
;
-- @lc code=end

