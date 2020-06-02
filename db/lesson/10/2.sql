# Построить запрос, который будет выводить следующие столбцы:
# имя группы
# среднее количество пользователей в группах
# самый молодой пользователь в группе
# самый старший пользователь в группе
# общее количество пользователей в группе
# всего пользователей в системе
# отношение в процентах (общее количество пользователей в группе / всего пользователей в системе) * 100

select
    c.name as 'имя группы',
    FIRST_VALUE(p.birthday) over (PARTITION BY cu.community_id ORDER BY p.birthday DESC ) 'самый молодой пользователь в группе',
    FIRST_VALUE(p.birthday) over (PARTITION BY cu.community_id ORDER BY p.birthday ASC ) 'самый старший пользователь в группе',
    count(cu.user_id) OVER (PARTITION BY cu.community_id) as 'общее количество пользователей в группе',
    (SELECT count(*) from users) as 'всего пользователей в системе',
    (count(cu.user_id) OVER (PARTITION BY cu.community_id)/(SELECT count(*) from users))*100 as 'отношение в процентах'
from users u
    left join profiles p on u.id = p.user_id
    left join communities_users cu on u.id = cu.user_id
    left join communities c on cu.community_id = c.id
GROUP BY c.name, p.birthday, cu.user_id, cu.community_id;