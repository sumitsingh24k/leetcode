# Write your MySQL query statement below
SELECT
ROUND(
    COUNT(customer_id) * 100.0 /
    (SELECT COUNT(DISTINCT customer_id) FROM Delivery),
    2
) as immediate_percentage 
FROM (
    SELECT *,
           ROW_NUMBER() OVER (
               PARTITION BY customer_id
               ORDER BY order_date
           ) AS rn
    FROM Delivery
) t
WHERE rn = 1
  AND order_date = customer_pref_delivery_date;