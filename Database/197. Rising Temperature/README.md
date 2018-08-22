# 197. Rising Temperature

MySQL `DATE_ADD()` Function

Example: Add 10 days to a date and return the date:

```
SELECT DATE_ADD("2017-06-15", INTERVAL 10 DAY);
```


Syntax

```
DATE_ADD(date, INTERVAL value unit)
```

- `date`: Required. The date to be modified
- `value`: Required. The value of the time/date interval to add. You can specify positive and negative values for this parameter
- `unit`: Required. The unit type of the interval.