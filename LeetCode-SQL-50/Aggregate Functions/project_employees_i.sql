SELECT project_id, ROUND(AVG(E.experience_years),2) as average_years  FROM Project as P LEFT JOIN Employee as E
ON
P.employee_id  = E.employee_id
GROUP BY project_id 