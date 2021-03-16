CREATE TABLE IF NOT EXISTS registration
(
  timestamp DATETIME,
  emailid text,
  first_name text,
  last_name text,
  banner_id text,
  program text,
  bootcamp_id id,
  bootcamps text,
  statistics_knowledge int,
  python_knowledge int,
  r_knowledge int,
  is_processed int,
  course_completed int,
  cert_sent int,
  PRIMARY KEY (banner_id, bootcamp_id) ON CONFLICT IGNORE
)
