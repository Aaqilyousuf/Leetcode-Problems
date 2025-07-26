# Write your MySQL query statement below
-- with deptSal as (
-- select d.name as Department, e.name as Employee,e.salary as Salary Rank() over (partition by d.name order by e.salary desc) as Rnk
-- from employee e
-- join department d on d.id = e.departmentId
-- ) 
-- select * from deptSal
-- where Rnk = 1
select d.name as Department, e.name as Employee,e.salary as Salary
from employee e
join department d on e.departmentId = d.id
where e.salary = (
    select MAX(salary)
    from employee
    where departmentId = e.departmentId
)