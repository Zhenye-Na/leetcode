--
-- @lc app=leetcode id=175 lang=mysql
--
-- [175] Combine Two Tables
--
-- https://leetcode.com/problems/combine-two-tables/description/
--
-- database
-- Easy (53.98%)
-- Likes:    699
-- Dislikes: 98
-- Total Accepted:    187.6K
-- Total Submissions: 347.5K
-- Testcase Example:  '{"headers": {"Person": ["PersonId", "LastName", "FirstName"], "Address": ["AddressId", "PersonId", "City", "State"]}, "rows": {"Person": [[1, "Wang", "Allen"]], "Address": [[1, 2, "New York City", "New York"]]}}'
--
-- Table: Person
-- 
-- 
-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | PersonId    | int     |
-- | FirstName   | varchar |
-- | LastName    | varchar |
-- +-------------+---------+
-- PersonId is the primary key column for this table.
-- 
-- 
-- Table: Address
-- 
-- 
-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | AddressId   | int     |
-- | PersonId    | int     |
-- | City        | varchar |
-- | State       | varchar |
-- +-------------+---------+
-- AddressId is the primary key column for this table.
-- 
-- 
-- 
-- 
-- Write a SQL query for a report that provides the following information for
-- each person in the Person table, regardless if there is an address for each
-- of those people:
-- 
-- 
-- FirstName, LastName, City, State
-- 
-- 
--

-- @lc code=start
# Write your MySQL query statement below
SELECT p.FirstName AS FirstName, p.LastName AS LastName, a.City AS City, a.State As State
FROM Person AS p
LEFT JOIN Address AS a
ON p.PersonId = a.PersonId;

-- @lc code=end

