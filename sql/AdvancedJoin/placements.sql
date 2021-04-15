select a.name
from students as a
left join packages as b
on a.id = b.id
left join friends as c
on a.id = c.id
left join packages as d
on c.friend_id = d.id
where d.salary > b.salary
order by d.salary
