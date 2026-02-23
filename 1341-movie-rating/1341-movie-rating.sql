
(
    select u.name as results
    from users u
    join MovieRating r
    on u.user_id=r.user_id
    group by u.user_id,u.name
    order by count(*) desc,u.name ASC
    LIMIT 1
)


UNION ALL

(
    SELECT m.title AS results
    FROM Movies m
    JOIN MovieRating r 
        ON m.movie_id = r.movie_id
    WHERE DATE_FORMAT(r.created_at, '%Y-%m') = '2020-02'
    GROUP BY m.movie_id, m.title
    ORDER BY AVG(r.rating) DESC, m.title ASC
    LIMIT 1
);