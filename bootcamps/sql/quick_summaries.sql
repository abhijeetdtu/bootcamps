select count(*) as num_registrations, b.name
from registration r
join bootcamps b on r.bootcamp_id = b.bootcamp_id
group by r.bootcamp_id
