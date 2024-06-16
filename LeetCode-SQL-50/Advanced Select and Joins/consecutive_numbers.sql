SELECT distinct num as ConsecutiveNums from(
    SELECT
    num,
    id + 1 - ROW_NUMBER() OVER (PARTITION BY num ORDER BY id) AS grp
    FROM 
    Logs
    ) as l
group by num,grp
having count(num) >= 3