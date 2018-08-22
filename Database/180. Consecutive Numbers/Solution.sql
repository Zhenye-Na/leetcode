# Write your MySQL query statement below
SELECT DISTINCT l1.Num AS ConsecutiveNums
FROM Logs AS l1, Logs AS l2, Logs AS l3
WHERE (l1.Id = l2.Id - 1
  AND l1.Num = l2.Num)
  AND (l3.Id = l2.Id + 1
  AND l3.Num = l2.Num)
;