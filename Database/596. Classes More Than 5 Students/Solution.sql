# Write your MySQL query statement below
SELECT c.class
FROM courses as c
GROUP BY c.class
HAVING COUNT(DISTINCT c.student) >= 5;