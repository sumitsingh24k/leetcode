# Write your MySQL query statement below
select t.product_id,
       t.year as first_year,
       t.quantity,
       t.price
from sales as t
join (
    select product_id, min(year) as first_year
    from sales
    group by product_id
) s
on s.product_id = t.product_id
and t.year = s.first_year;