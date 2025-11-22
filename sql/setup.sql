-- setup.sql
-- Create tables and insert small sample data for local testing (SQLite/Postgres compatible)
PRAGMA foreign_keys = ON;

CREATE TABLE users (
  user_id INTEGER PRIMARY KEY,
  name TEXT,
  email TEXT
);

CREATE TABLE events (
  event_id INTEGER PRIMARY KEY,
  user_id INTEGER,
  event_type TEXT,
  event_time TEXT,
  value REAL,
  FOREIGN KEY(user_id) REFERENCES users(user_id)
);

-- Sample inserts
INSERT INTO users (user_id, name, email) VALUES (1, 'Alice', 'alice@example.com');
INSERT INTO events (event_id, user_id, event_type, event_time, value) VALUES
 (1, 1, 'click', '2025-11-20 10:00:00', 1.0),
 (2, 1, 'purchase', '2025-11-21 11:30:00', 99.99);
