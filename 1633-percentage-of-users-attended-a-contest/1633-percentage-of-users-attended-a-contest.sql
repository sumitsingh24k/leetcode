# Write your MySQL query statement below
select r.contest_id ,round(
    count(*)*100/
    (SELECT COUNT(*) FROM Users),2
)as percentage 
from Register as r
group by r.contest_id 
order by percentage desc, r.contest_id ASC