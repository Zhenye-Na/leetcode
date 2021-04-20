--
-- @lc app=leetcode id=262 lang=mysql
--
-- [262] Trips and Users
--
-- https://leetcode.com/problems/trips-and-users/description/
--
-- database
-- Hard (26.51%)
-- Likes:    294
-- Dislikes: 205
-- Total Accepted:    46.7K
-- Total Submissions: 160.4K
-- Testcase Example:  '{"headers": {"Trips": ["Id", "Client_Id", "Driver_Id", "City_Id", "Status", "Request_at"], "Users": ["Users_Id", "Banned", "Role"]}, "rows": {"Trips": [["1", "1", "10", "1", "completed", "2013-10-01"], ["2", "2", "11", "1", "cancelled_by_driver", "2013-10-01"], ["3", "3", "12", "6", "completed", "2013-10-01"], ["4", "4", "13", "6", "cancelled_by_client", "2013-10-01"], ["5", "1", "10", "1", "completed", "2013-10-02"], ["6", "2", "11", "6", "completed", "2013-10-02"], ["7", "3", "12", "6", "completed", "2013-10-02"], ["8", "2", "12", "12", "completed", "2013-10-03"], ["9", "3", "10", "12", "completed", "2013-10-03"], ["10", "4", "13", "12", "cancelled_by_driver", "2013-10-03"]], "Users": [["1", "No", "client"], ["2", "Yes", "client"], ["3", "No", "client"], ["4", "No", "client"], ["10", "No", "driver"], ["11", "No", "driver"], ["12", "No", "driver"], ["13", "No", "driver"]]}}'
--
-- The Trips table holds all taxi trips. Each trip has a unique Id, while
-- Client_Id and Driver_Id are both foreign keys to the Users_Id at the Users
-- table. Status is an ENUM type of (‘completed’, ‘cancelled_by_driver’,
-- ‘cancelled_by_client’).
-- 
-- 
-- +----+-----------+-----------+---------+--------------------+----------+
-- | Id | Client_Id | Driver_Id | City_Id |        Status      |Request_at|
-- +----+-----------+-----------+---------+--------------------+----------+
-- | 1  |     1     |    10     |    1    |     completed      |2013-10-01|
-- | 2  |     2     |    11     |    1    | cancelled_by_driver|2013-10-01|
-- | 3  |     3     |    12     |    6    |     completed      |2013-10-01|
-- | 4  |     4     |    13     |    6    | cancelled_by_client|2013-10-01|
-- | 5  |     1     |    10     |    1    |     completed      |2013-10-02|
-- | 6  |     2     |    11     |    6    |     completed      |2013-10-02|
-- | 7  |     3     |    12     |    6    |     completed      |2013-10-02|
-- | 8  |     2     |    12     |    12   |     completed      |2013-10-03|
-- | 9  |     3     |    10     |    12   |     completed      |2013-10-03| 
-- | 10 |     4     |    13     |    12   | cancelled_by_driver|2013-10-03|
-- +----+-----------+-----------+---------+--------------------+----------+
-- 
-- 
-- The Users table holds all users. Each user has an unique Users_Id, and Role
-- is an ENUM type of (‘client’, ‘driver’, ‘partner’).
-- 
-- 
-- +----------+--------+--------+
-- | Users_Id | Banned |  Role  |
-- +----------+--------+--------+
-- |    1     |   No   | client |
-- |    2     |   Yes  | client |
-- |    3     |   No   | client |
-- |    4     |   No   | client |
-- |    10    |   No   | driver |
-- |    11    |   No   | driver |
-- |    12    |   No   | driver |
-- |    13    |   No   | driver |
-- +----------+--------+--------+
-- 
-- 
-- Write a SQL query to find the cancellation rate of requests made by unbanned
-- users (both client and driver must be unbanned) between Oct 1, 2013 and Oct
-- 3, 2013. The cancellation rate is computed by dividing the number of
-- canceled (by client or driver) requests made by unbanned users by the total
-- number of requests made by unbanned users.
-- 
-- For the above tables, your SQL query should return the following rows with
-- the cancellation rate being rounded to two decimal places.
-- 
-- 
-- +------------+-------------------+
-- |     Day    | Cancellation Rate |
-- +------------+-------------------+
-- | 2013-10-01 |       0.33        |
-- | 2013-10-02 |       0.00        |
-- | 2013-10-03 |       0.50        |
-- +------------+-------------------+
-- 
-- 
-- Credits:
-- Special thanks to @cak1erlizhou for contributing this question, writing the
-- problem description and adding part of the test cases.
-- 
--

-- @lc code=start
# Write your MySQL query statement below

((SELECT COUNT(*)
FROM Trips
WHERE status <> 'Completed' AND Client_Id IN (SELECT Users_Id FROM Users WHERE Banned = 'No') AND Driver_Id IN (SELECT Users_Id FROM Users WHERE Banned = 'No'
GROUP BY Request_at)) / (SELECT COUNT(*)
FROM Trips
WHERE Client_Id IN (SELECT Users_Id FROM Users WHERE Banned = 'No') AND Driver_Id IN (SELECT Users_Id FROM Users WHERE Banned = 'No')))


SELECT Users_Id FROM Users WHERE Banned = 'No'
-- @lc code=end

