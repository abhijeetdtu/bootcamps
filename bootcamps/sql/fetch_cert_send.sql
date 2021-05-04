select SUBSTR(full_name, instr(full_name , ',')+1, length(full_name) - instr(full_name , ','))|| " " || SUBSTR(full_name, 0, instr(full_name , ',')) as full_name
,gt.login_id
,bootcamp
,gt.bootcamp_id
,(total_assignments - assignments_completed) as remaining
, (total_score*1.0/max_score)*100 as score
, hash
from grades_tracker gt
left join certificates c on c.login_id = gt.login_id and c.bootcamp_id = gt.bootcamp_id
--where (gt.bootcamp_id in (3,2))
where ((score > 89 and gt.bootcamp_id in (3,2))
      or (total_score > 230*.88 and gt.bootcamp_id = 1 )
      or (gt.bootcamp_id = 1 and total_score= 77 and assignments_completed = 1)
      or (gt.bootcamp_id = 2 and total_score > 117*.89) -- Hello world  (5 Points) is not graded 122-5
      )
      and hash is null
order by score desc, (total_assignments - assignments_completed)
