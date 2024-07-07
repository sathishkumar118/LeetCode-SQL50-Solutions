select
d.name as Department,
emp.name as Employee,
emp.salary as salary
from
(
    select
    *,
    dense_rank() over(partition by departmentId order by salary desc) as sal_rank
    from
    Employee
) as emp
left join
Department as d
on emp.departmentId = d.id
where emp.sal_rank <= 3
order by emp.salary desc