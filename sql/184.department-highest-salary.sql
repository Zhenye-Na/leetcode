--
-- @lc app=leetcode id=184 lang=mysql
--
-- [184] Department Highest Salary
--
-- https://leetcode.com/problems/department-highest-salary/description/
--
-- database
-- Medium (30.61%)
-- Likes:    385
-- Dislikes: 91
-- Total Accepted:    88.7K
-- Total Submissions: 265.7K
-- Testcase Example:  '{"headers": {"Employee": ["Id", "Name", "Salary", "DepartmentId"], "Department": ["Id", "Name"]}, "rows": {"Employee": [[1, "Joe", 70000, 1], [2, "Jim", 90000, 1], [3, "Henry", 80000, 2], [4, "Sam", 60000, 2], [5, "Max", 90000, 1]], "Department": [[1, "IT"], [2, "Sales"]]}}'
--
-- The Employee table holds all employees. Every employee has an Id, a salary,
-- and there is also a column for the department Id.
-- 
-- 
-- +----+-------+--------+--------------+
-- | Id | Name  | Salary | DepartmentId |
-- +----+-------+--------+--------------+
-- | 1  | Joe   | 70000  | 1            |
-- | 2  | Jim   | 90000  | 1            |
-- | 3  | Henry | 80000  | 2            |
-- | 4  | Sam   | 60000  | 2            |
-- | 5  | Max   | 90000  | 1            |
-- +----+-------+--------+--------------+
-- 
-- 
-- The Department table holds all departments of the company.
-- 
-- 
-- +----+----------+
-- | Id | Name     |
-- +----+----------+
-- | 1  | IT       |
-- | 2  | Sales    |
-- +----+----------+
-- 
-- 
-- Write a SQL query to find employees who have the highest salary in each of
-- the departments. For the above tables, your SQL query should return the
-- following rows (order of rows does not matter).
-- 
-- 
-- +------------+----------+--------+
-- | Department | Employee | Salary |
-- +------------+----------+--------+
-- | IT         | Max      | 90000  |
-- | IT         | Jim      | 90000  |
-- | Sales      | Henry    | 80000  |
-- +------------+----------+--------+
-- 
-- 
-- Explanation:
-- 
-- Max and Jim both have the highest salary in the IT department and Henry has
-- the highest salary in the Sales department.
-- 
--

-- @lc code=start
# Write your MySQL query statement below
SELECT d.Name AS Department, e.Name AS Employee, e.Salary AS Salary
FROM Employee AS e, Department AS d
WHERE e.DepartmentId = d.Id
  AND e.Salary = (SELECT MAX(Salary) FROM Employee AS e2 WHERE e2.DepartmentId = d.Id)
;
-- @lc code=end

