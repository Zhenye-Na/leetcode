# Write your MySQL query statement below
SELECT Person.email
FROM Person
GROUP BY Person.email
HAVING COUNT(*) > 1;