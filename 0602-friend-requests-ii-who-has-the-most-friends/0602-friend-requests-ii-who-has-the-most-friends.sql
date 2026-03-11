SELECT total AS id, COUNT(*) AS num
FROM (
    SELECT requester_id AS total FROM RequestAccepted
    UNION ALL
    SELECT accepter_id FROM RequestAccepted
) t
GROUP BY total
ORDER BY num DESC
LIMIT 1;