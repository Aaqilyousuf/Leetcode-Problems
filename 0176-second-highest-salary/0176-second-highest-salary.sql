# Write your MySQL query statement below

-- select max(salary) as 'SecondHighestSalary' from Employee where salary not in (select max(salary) from Employee);

-- select (
--     select distinct salary
--     from employee
--     order by salary desc
--     limit 1 OFFSET 1
-- ) as SecondHighestSalary 
WITH RankedSalaries AS (
  SELECT 
    salary,
    DENSE_RANK() OVER (ORDER BY salary DESC) AS rnk
  FROM Employee
)
SELECT 
  (
    SELECT salary 
    FROM RankedSalaries 
    WHERE rnk = 2 
    LIMIT 1
  ) AS SecondHighestSalary;
