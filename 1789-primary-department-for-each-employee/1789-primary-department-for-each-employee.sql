# Write your MySQL query statement below
select employee_id ,department_id 
from Employee 
where primary_flag ='y'
union all 
select employee_id ,department_id 
from Employee
GROUP BY employee_id
HAVING COUNT(*) = 1
