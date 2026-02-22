SELECT 
   round(SUM(IF(a.event_date = DATE_ADD(t.first_date, INTERVAL 1 DAY), 1, 0)) 
    / COUNT(DISTINCT t.player_id),2) AS fraction
FROM 
(
    SELECT 
        player_id,
        MIN(event_date) AS first_date
    FROM Activity
    GROUP BY player_id
) t
JOIN Activity a
ON t.player_id = a.player_id;