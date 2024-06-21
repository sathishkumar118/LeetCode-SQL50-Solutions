SELECT IFNULL(
    (
        SELECT salary
        FROM
        (
            SELECT
                salary,
                dense_rank() OVER (ORDER BY salary DESC) AS salary_rank
            FROM Employee
        ) AS emp
        where salary_rank = 2
        LIMIT 1
    ), NULL) AS SecondHighestSalary;