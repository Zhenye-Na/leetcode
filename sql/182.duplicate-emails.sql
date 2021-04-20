--
-- @lc app=leetcode id=182 lang=mysql
--
-- [182] Duplicate Emails
--
-- https://leetcode.com/problems/duplicate-emails/description/
--
-- database
-- Easy (56.54%)
-- Likes:    361
-- Dislikes: 24
-- Total Accepted:    151.8K
-- Total Submissions: 256.8K
-- Testcase Example:  '{"headers": {"Person": ["Id", "Email"]}, "rows": {"Person": [[1, "a@b.com"], [2, "c@d.com"], [3, "a@b.com"]]}}'
--
-- Write a SQL query to find all duplicate emails in a table named Person.
-- 
-- 
-- +----+---------+
-- | Id | Email   |
-- +----+---------+
-- | 1  | a@b.com |
-- | 2  | c@d.com |
-- | 3  | a@b.com |
-- +----+---------+
-- 
-- 
-- For example, your query should return the following for the above table:
-- 
-- 
-- +---------+
-- | Email   |
-- +---------+
-- | a@b.com |
-- +---------+
-- 
-- 
-- Note: All emails are in lowercase.
-- 
--

-- @lc code=start
# Write your MySQL query statement below
SELECT DISTINCT Email
FROM Person
GROUP BY Email
HAVING COUNT(Email) > 1
;
-- @lc code=end

