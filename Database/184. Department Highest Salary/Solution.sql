# Write your MySQL query statement below
SELECT DISTINCT d.Name AS Department, e1.Name AS Employee, e1.Salary AS Salary
FROM Employee AS e1, Employee AS e2, Department AS d
WHERE e1.DepartmentId = d.Id
  AND e1.DepartmentId = e2.DepartmentId
  AND e1.Salary <= e2.Salary
GROUP BY d.Name, e1.Name
HAVING COUNT(DISTINCT e2.Salary) = 1
;