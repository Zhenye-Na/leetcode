## Seven Types of SQL JOINs



### Inner Join

The inner join is probably the most commonly-used type of join in SQL. Inner joins return all rows from two or more tables that meet the join condition.



![](./assets/0_MHrYXyHi3YLvkH7i_-20190702152649805.png)



#### Sample SQL

```sql
SELECT columns
FROM TableA
INNER JOIN TableB
ON A.columnName = B.columnName;
```



### Left [Outer] Join

The left outer join (sometimes abbreviated to left join) returns <u>all rows from the left-hand table specified in the ON condition</u>. And, *only* the <u>rows from the right-hand table that meet the join condition</u>.





#### Sample SQL

```sql
SELECT columns
FROM TableA
LEFT OUTER JOIN TableB
ON A.columnName = B.columnName
```





### Left [Outer] Join without Intersection

This join type is a variant on the basic left outer join. But instead, it returns all rows from the left-hand table specified in the ON condition that also meets the join condition. *None* of the rows from the right-hand table that matches the join condition.



#### Sample SQL

```sql
SELECT columns
FROM TableA
LEFT OUTER JOIN TableB
ON A.columnName = B.columnName
WHERE B.columnName IS NULL
```



### Right [Outer] Join

The right outer join (sometimes abbreviated to right join) returns all rows from the right-hand table specified in the ON condition and *only* the rows from the left-hand table that meet the join condition.



[![img](/Users/macbookpro/Desktop/leetcode/Database/assets/0_jM3CoEQ9DAnT1PbD_.png)](https://s3.amazonaws.com/prod.io.teamsql.wordpress/wp-content/uploads/2017/04/16133807/0_jM3CoEQ9DAnT1PbD_.png)



#### Sample SQL

```sql
SELECT columns
FROM TableA
RIGHT OUTER JOIN TableB
ON A.columnName = B.columnName
```

 

### Right [Outer] Join without Intersection

This join is a variant on the right outer join, but instead, it returns all rows from the right-hand table specified in the ON condition that also meets the join condition and *none* of the rows from the left-hand table that match the join condition.





[![img](/Users/macbookpro/Desktop/leetcode/Database/assets/0_VJOHPBkd0e0Y4jcs_.png)](https://s3.amazonaws.com/prod.io.teamsql.wordpress/wp-content/uploads/2017/04/16133850/0_VJOHPBkd0e0Y4jcs_.png)

## 

#### Sample SQL

```sql
SELECT columns
FROM TableA
RIGHT OUTER JOIN TableB
ON A.columnName = B.columnName
WHERE A.columnName IS NULL
```

 

### Full [Outer] Join

The entire outer join (sometimes abbreviated to full join) returns all rows from both tables named in the ON condition where the join condition is *not* met (including NULL values).

###  [![img](/Users/macbookpro/Desktop/leetcode/Database/assets/0_JjEjDtvyjjCWps2w_-1111.png)](https://s3.amazonaws.com/prod.io.teamsql.wordpress/wp-content/uploads/2017/04/16133954/0_JjEjDtvyjjCWps2w_-1111.png)

#### Sample SQL

```
SELECT columns
FROM TableA
FULL JOIN TableB
ON A.columnName = B.columnName
```

 

### Full [Outer] Join without Intersection

This variant of the full outer join (sometimes abbreviated to full join) returns all rows from both tables named in the ON condition where the join condition is *not* met (excluding NULL values).



## [![img](/Users/macbookpro/Desktop/leetcode/Database/assets/0_6osFFhtC_1MRyk12222222222Y_.png)](https://s3.amazonaws.com/prod.io.teamsql.wordpress/wp-content/uploads/2017/04/16134027/0_6osFFhtC_1MRyk12222222222Y_.png)

#### Sample SQL

```
SELECT columns
FROM TableA
FULL JOIN TableB
ON A.columnName = B.columnName
WHERE A.columnName IS NULL
OR B.columnName IS NULL
```



## References

- TeamSQL, [The Seven Types of SQL Joins](https://teamsql.io/blog/?p=923)

  