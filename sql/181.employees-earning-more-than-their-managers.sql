--
-- @lc app=leetcode id=181 lang=mysql
--
-- [181] Employees Earning More Than Their Managers
--
-- https://leetcode.com/problems/employees-earning-more-than-their-managers/description/
--
-- database
-- Easy (50.22%)
-- Likes:    479
-- Dislikes: 57
-- Total Accepted:    148.6K
-- Total Submissions: 279.2K
-- Testcase Example:  '{"headers": {"Employee": ["Id", "Name", "Salary", "ManagerId"]}, "rows": {"Employee": [[1, "Joe", 70000, 3], [2, "Henry", 80000, 4], [3, "Sam", 60000, null], [4, "Max", 90000, null]]}}'
--
-- The Employee table holds all employees including their managers. Every
-- employee has an Id, and there is also a column for the manager Id.
-- 
-- 
-- +----+-------+--------+-----------+
-- | Id | Name  | Salary | ManagerId |
-- +----+-------+--------+-----------+
-- | 1  | Joe   | 70000  | 3         |
-- | 2  | Henry | 80000  | 4         |
-- | 3  | Sam   | 60000  | NULL      |
-- | 4  | Max   | 90000  | NULL      |
-- +----+-------+--------+-----------+
-- 
-- 
-- Given the Employee table, write a SQL query that finds out employees who
-- earn more than their managers. For the above table, Joe is the only employee
-- who earns more than his manager.
-- 
-- 
-- +----------+
-- | Employee |
-- +----------+
-- | Joe      |
-- +----------+
-- 
-- 
--

-- @lc code=start
# Write your MySQL query statement below
SELECT e1.Name AS Employee
FROM Employee AS e1, Employee AS e2
WHERE e1.ManagerId = e2.Id AND e1.Salary > e2.Salary
;
-- @lc code=end

