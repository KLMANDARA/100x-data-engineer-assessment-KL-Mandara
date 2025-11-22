-- task1.sql
-- Question: <paste question text here>
-- Approach: <brief approach notes>

-- Example query: count events by type
SELECT event_type, COUNT(*) AS cnt
FROM events
GROUP BY event_type
ORDER BY cnt DESC;
