# 196. Delete Duplicate Emails

Approach: Using `DELETE` and `WHERE` clause *[Accepted]*

By joining this table with itself on the `Email` column, we can get the following code.

```sql
SELECT p1.*
FROM Person p1, Person p2
WHERE p1.Email = p2.Email;
```

Then we need to find the bigger id having same email address with other records. So we can add a new condition to the `WHERE` clause like this.

```sql
SELECT p1.*
FROM Person p1, Person p2
WHERE p1.Email = p2.Email 
  AND p1.Id > p2.Id;
```

As we already get the records to be deleted, we can alter this statement to `DELETE` in the end.


```sql
DELETE p1
FROM Person p1, Person p2
WHERE p1.Email = p2.Email
  AND p1.Id > p2.Id;
```