# Write your MySQL query statement below
SELECT id,
    CASE
        WHEN (id % 2 = 0) THEN (SELECT s2.student as student 
                                FROM seat as s2 
                                WHERE s2.id = s.id - 1)
        WHEN (id % 2 = 1 AND id <> (SELECT MAX(s3.id) as id FROM seat as s3)) THEN (SELECT s2.student as student 
                                                                                    FROM seat as s2 
                                                                                    WHERE s2.id = s.id + 1)
        WHEN (id % 2 = 1 AND id = (SELECT MAX(s3.id) as id FROM seat as s3)) THEN student
    END student

FROM seat as s