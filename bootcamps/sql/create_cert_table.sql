CREATE TABLE IF NOT EXISTS certificates
(
  login_id text,
  bootcamp_id int,
  cert_sent_date datetime,
  hash text,
  PRIMARY KEY (login_id, bootcamp_id) ON CONFLICT IGNORE
)
