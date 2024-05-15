# Write your MySQL query statement below
SELECT t1.id as Id from
    (SELECT id,(temperature - (LAG(temperature, 1) OVER (ORDER BY recordDate))) AS tmp_diff,
    DATEDIFF(recordDate, LAG(recordDate, 1) OVER(ORDER BY recordDate)) as dt_diff FROM Weather) as t1
    where t1.tmp_diff > 0 and t1.dt_diff = 1