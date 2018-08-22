# 627. Swap Salary

@source: [Stack Overflow](https://stackoverflow.com/questions/37058381/swap-values-in-a-column-in-sql-server-table) question answered by [Martin Smith](https://stackoverflow.com/users/73226/martin-smith)


You can just use case. Conceptually the operation happens "all at once" so there's no need to use a fourth dummy value as in your sequential approach.

```
UPDATE YourTable
SET ID = CASE ID WHEN 1 THEN 3
                 WHEN 2 THEN 1
                 WHEN 3 THEN 2
         END
WHERE ID IN (1,2,3)
```

Though changing ids is unusual as they should generally be immutable.