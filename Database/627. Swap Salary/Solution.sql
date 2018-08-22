# Write your MySQL query statement below
UPDATE salary
SET salary.sex = CASE salary.sex WHEN "m" THEN "f"
                                 WHEN "f" THEN "m"
                 END
WHERE salary.sex IN ("m", "f");