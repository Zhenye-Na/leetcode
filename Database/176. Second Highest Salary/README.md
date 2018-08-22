# 176. Second Highest Salary

### Approach: Using sub-query and `LIMIT` clause [Accepted]

Sort the distinct salary in descend order and then utilize the `LIMIT` clause to get the second highest salary.

```sql
SELECT DISTINCT
    Salary AS SecondHighestSalary
FROM
    Employee
ORDER BY Salary DESC
LIMIT 1 OFFSET 1
```

However, this solution will be judged as 'Wrong Answer' *_if there is no such second highest salary since there might be only one record in this table_*. To overcome this issue, we can take this as a temp table.

```sql
SELECT
    (SELECT DISTINCT
            Salary
        FROM
            Employee
        ORDER BY Salary DESC
        LIMIT 1 OFFSET 1) AS SecondHighestSalary
;
```

> [*Introduction to SQL LIMIT clause*](http://www.sqltutorial.org/sql-limit/)

To retrieve a portion of rows returned by a query, you use the LIMIT and OFFSET keywords. The following illustrates the syntax of the LIMIT clause.

```sql
SELECT 
    column_list
FROM
    table1
ORDER BY column_list
LIMIT row_count OFFSET offset;
```

The `row_count` specifies the _number of rows that will be returned_.

The `OFFSET` means to **skip the offset rows before beginning to return rows**. The `OFFSET` keyword is optional so you can skip it. If you use both `LIMIT` and `OFFSET` keywords, the `OFFSET` skips `offset` rows **first** before the `LIMIT` constrains the number of rows.

When you use the `LIMIT` clause, it is important to use an `ORDER BY` clause to make sure that the result set returned in a specified order.



### Approach: Using `IFNULL` and `LIMIT` clause [Accepted]

Another way to solve the `'NULL'` problem is to use `IFNULL` funtion as below.


```sql
SELECT
    IFNULL(
      (SELECT DISTINCT Salary
       FROM Employee
       ORDER BY Salary DESC
       LIMIT 1 OFFSET 1),
    NULL) AS SecondHighestSalary
;
```