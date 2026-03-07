# Write your MySQL query statement below
delete from Person
where id in (
select id from (
    select id,
    row_number() over (partition by  email order by id) as rnk from Person
)t
where rnk>1
)