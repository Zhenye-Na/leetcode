# 596. Classes More Than 5 Students


Approach: Using `GROUP BY` and `HAVING` condition [Accepted]

Using sub-query is one way to add some condition to a `GROUP BY` clause, however, using `HAVING` is another simpler and natural approach. So we can rewrite the above solution as below.

```sql
SELECT
    class
FROM
    courses
GROUP BY class
HAVING COUNT(DISTINCT student) >= 5;
```