# Write your MySQL query statement below
SELECT c.Name as Customers
FROM Customers as c
WHERE c.Id NOT IN (SELECT o.CustomerId
                   FROM  Orders as o
                  );