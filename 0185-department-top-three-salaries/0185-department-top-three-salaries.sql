# Write your MySQL query statement below
SELECT d.name as Department ,
t.name  as Employee,
t.salary as Salary  
FROM (
    SELECT *,
           DENSE_RANK() OVER (PARTITION BY departmentId ORDER BY salary DESC) AS ranking
    FROM Employee
) t
join department d
on
t.departmentId =d.id
WHERE ranking < 4