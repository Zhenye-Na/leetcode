# Write your MySQL query statement below
SELECT *
FROM cinema
WHERE (cinema.id % 2 <> 0 
       AND cinema.description <> "boring")
ORDER BY cinema.rating DESC;