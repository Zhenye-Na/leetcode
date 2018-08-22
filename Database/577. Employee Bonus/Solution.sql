SELECT E.name, B.bonus
  FROM Employee AS E
  INNER JOIN Bonus AS B
    ON E.empId = B.empId
  WHERE B.bonus < 1000
;