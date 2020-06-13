-- 5. Найти 10 пользователей, которые проявляют наименьшую активность в использовании социальной сети
-- (критерии активности необходимо определить самостоятельно).

select u.id, (
    select sum(tbl.c) from (
        select 'communities_users' as name, count(*) as c from communities_users cu where cu.user_id = u.id union
        select 'friendship' as name, count(*) as c from friendship f where f.user_id = u.id union
        select 'likes' as name, count(*) as c from likes l where l.user_id = u.id union
        select 'media' as name, count(*) as c from media m where m.user_id = u.id union
        select 'messages' as name, count(*) as c from messages m2 where m2.from_user_id = u.id union
        select 'posts' as name, count(*) as c from posts p where p.user_id = u.id
        ) as tbl
) activity from users u order by activity limit 10;