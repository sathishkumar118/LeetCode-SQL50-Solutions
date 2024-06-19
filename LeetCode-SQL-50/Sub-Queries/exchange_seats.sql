SELECT
    id,
    CASE
        WHEN MOD(id, 2) = 0 THEN LAG(student,1) over(order by id)
        WHEN LEAD(student,1) over(order by id) IS NULL THEN student
        ELSE LEAD(student,1) over(order by id)
    END as student
from 
Seat