--
-- @lc app=leetcode id=601 lang=mysql
--
-- [601] Human Traffic of Stadium
--
-- https://leetcode.com/problems/human-traffic-of-stadium/description/
--
-- database
-- Hard (37.37%)
-- Likes:    131
-- Dislikes: 284
-- Total Accepted:    21.9K
-- Total Submissions: 55.4K
-- Testcase Example:  '{"headers": {"stadium": ["id", "visit_date", "people"]}, "rows": {"stadium": [[1, "2017-01-01", 10], [2, "2017-01-02", 109], [3, "2017-01-03", 150], [4, "2017-01-04", 99], [5, "2017-01-05", 145], [6, "2017-01-06", 1455], [7, "2017-01-07", 199], [8, "2017-01-08", 188]]}}'
--
-- X city built a new stadium, each day many people visit it and the stats are
-- saved as these columns: id, visit_date, people
-- 
-- Please write a query to display the records which have 3 or more consecutive
-- rows and the amount of people more than 100(inclusive).
-- For example, the table stadium:
-- 
-- 
-- +------+------------+-----------+
-- | id   | visit_date | people    |
-- +------+------------+-----------+
-- | 1    | 2017-01-01 | 10        |
-- | 2    | 2017-01-02 | 109       |
-- | 3    | 2017-01-03 | 150       |
-- | 4    | 2017-01-04 | 99        |
-- | 5    | 2017-01-05 | 145       |
-- | 6    | 2017-01-06 | 1455      |
-- | 7    | 2017-01-07 | 199       |
-- | 8    | 2017-01-08 | 188       |
-- +------+------------+-----------+
-- 
-- 
-- For the sample data above, the output is:
-- 
-- 
-- +------+------------+-----------+
-- | id   | visit_date | people    |
-- +------+------------+-----------+
-- | 5    | 2017-01-05 | 145       |
-- | 6    | 2017-01-06 | 1455      |
-- | 7    | 2017-01-07 | 199       |
-- | 8    | 2017-01-08 | 188       |
-- +------+------------+-----------+
-- 
-- 
-- Note:
-- Each day only have one row record, and the dates are increasing with id
-- increasing.
-- 
--

-- @lc code=start
# Write your MySQL query statement below
SELECT DISTINCT S1.*
FROM stadium S1
JOIN stadium S2
JOIN stadium S3
ON (
  (S1.id = S2.id - 1 AND S1.id = S3.id - 2)
  OR (S3.id = S1.id - 1 AND S3.id = S2.id - 2)
  OR (S3.id = S2.id - 1 AND S3.id = S1.id - 2)
  )
WHERE S1.people >= 100
AND S2.people >= 100
AND S3.people >= 100
ORDER BY S1.id
;
-- @lc code=end

