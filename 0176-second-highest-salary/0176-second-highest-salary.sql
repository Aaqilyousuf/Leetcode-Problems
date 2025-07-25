# Write your MySQL query statement below
-- select max(salary) as 'SecondHighestSalary' from Employee where salary not in (select max(salary) from Employee);
select (
    select distinct salary
    from employee
    order by salary desc
    limit 1 OFFSET 1
) as SecondHighestSalary 
