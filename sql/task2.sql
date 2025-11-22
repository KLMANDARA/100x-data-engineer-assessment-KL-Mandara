-- task2.sql
-- Question: <paste question text here>
-- Example: top users by purchase value
SELECT u.user_id, u.name, SUM(e.value) AS total_value
FROM users u
JOIN events e ON u.user_id = e.user_id
WHERE e.event_type = 'purchase'
GROUP BY u.user_id, u.name
ORDER BY total_value DESC;
