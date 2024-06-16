SELECT E1.reports_to AS employee_id,
MAX(E2.name) as name,
COUNT(E1.employee_id) AS reports_count,
ROUND(AVG(E1.age)) AS average_age
from Employees AS E1
JOIN Employees AS E2
ON
E1.reports_to = E2.employee_id
AND E1.reports_to IS NOT NULL
GROUP BY E1.reports_to
ORDER BY E1.reports_to