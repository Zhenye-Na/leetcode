# For example, given the above Employee table,
# the query should return the second highest
# salary. 

# If there is no second highest salary,
# then the query should return null.

# Write your MySQL query statement below
SELECT MAX(e1.Salary) as SecondHighestSalary
FROM Employee as e1, Employee as e2
WHERE e1.Salary >= e2.Salary
  AND e1.Salary < (SELECT MAX(e3.Salary)
                   FROM Employee as e3);