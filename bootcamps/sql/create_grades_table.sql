CREATE TABLE IF NOT EXISTS grades
(
  full_name text,
  canvas_id text,
  user_id text,
  login_id text,
  bootcamp_id id,
  section text,
  assignment text,
  score int,
  PRIMARY KEY (login_id, bootcamp_id , assignment) ON CONFLICT REPLACE
)
