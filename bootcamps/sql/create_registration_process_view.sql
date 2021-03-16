CREATE VIEW IF NOT EXISTS registration_process
AS
select r.timestamp,r.emailid,first_name,last_name,program,bootcamps
from registration r
left join (
select *, login_id || "@uncc.edu" as emailid
from grades_tracker gt) g
on r.emailid = g.emailid and r.bootcamp_id = g.bootcamp_id
where max_score is null
