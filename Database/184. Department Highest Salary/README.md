# 184. Department Highest Salary

## Approach: Using `JOIN` and `IN` clause [Accepted]

**Algorithm**

Since the `Employee` table contains the `Salary` and `DepartmentId` information, we can query the highest salary in a department.

```sql
SELECT
    DepartmentId, MAX(Salary)
FROM
    Employee
GROUP BY DepartmentId;
```

> Note: There might be multiple employees having the same highest salary, so it is safe not to include the employee name information in this query.

```
| DepartmentId | MAX(Salary) |
|--------------|-------------|
| 1            | 90000       |
| 2            | 80000       |
```

Then, we can join table `Employee` and `Department`, and query the `(DepartmentId, Salary)` are in the temp table using `IN` statement as below.

**MySQL**

```sql
SELECT
    Department.name AS 'Department',
    Employee.name AS 'Employee',
    Salary
FROM
    Employee
        JOIN
    Department ON Employee.DepartmentId = Department.Id
WHERE
    (Employee.DepartmentId , Salary) IN
    (   SELECT
            DepartmentId, MAX(Salary)
        FROM
            Employee
        GROUP BY DepartmentId
    )
;
```

```
| Department | Employee | Salary |
|------------|----------|--------|
| Sales      | Henry    | 80000  |
| IT         | Max      | 90000  |
```