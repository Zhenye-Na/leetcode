# Write your MySQL query statement below
SELECT DISTINCT w1.Id
FROM Weather as w1, Weather as w2
WHERE w1.Temperature > w2.Temperature
  AND w1.RecordDate = DATE_ADD(w2.RecordDate, INTERVAL 1 DAY);