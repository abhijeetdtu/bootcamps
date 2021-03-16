CREATE VIEW IF NOT EXISTS grades_tracker
AS
with scores as (select *
from grades g
join bootcamps bc on g.bootcamp_id = bc.bootcamp_id
join
(select distinct section ,  assignment , score as max_score
from grades
where assignment GLOB '*[1-9]*'
and full_name like '%Points Possible%' ) as ps
on g.assignment = ps.assignment)
select full_name,login_id ,bootcamp_id, name as bootcamp, sum(score) as total_score , sum(max_score) as max_score , count(score) as assignments_completed , count(max_score) as total_assignments
from scores
group by login_id,section
order by total_score desc
