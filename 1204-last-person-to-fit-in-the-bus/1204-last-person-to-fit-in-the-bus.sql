# Write your MySQL query statement below
select person_name from 
(
    select person_name,
    sum(weight)  over ( order by turn) as toaal_weight
    ,row_number() over ( order by turn) as rowno from Queue 
) t
where toaal_weight<=1000 
order by rowno desc 
limit 1