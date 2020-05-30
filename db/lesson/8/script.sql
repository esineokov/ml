-- Подсчитать общее количество лайков десяти самым молодым пользователям (сколько лайков получили 10 самых молодых пользователей).
select tbl.user_id, p.birthday, count(*) from (
	select 1 as ttp, m.id, m.from_user_id as user_id from messages m union
	select 2 as ttp, u.id, u.id as user_id from users u union
	select 3 as ttp, me.id, me.user_id as user_id from media me union
	select 4 as ttp, p.id, p.user_id as user_id from posts p
) as tbl
left join likes l ON l.target_type_id = tbl.ttp and l.target_id = tbl.id and l.id is not null
left join profiles p ON p.user_id = tbl.user_id
group by tbl.user_id, p.birthday
order by p.birthday desc
limit 10;


-- 4. Определить кто больше поставил лайков (всего) - мужчины или женщины?
select gender from likes l left join profiles p ON p.user_id = l.user_id group by gender limit 1;

-- 5. Найти 10 пользователей, которые проявляют наименьшую активность в использовании социальной сети
-- (критерии активности необходимо определить самостоятельно).

select u.id, ifnull(tbl1.c, 0) + ifnull(tbl2.c, 0) + ifnull(tbl3.c, 0) + ifnull(tbl4.c, 0) + ifnull(tbl5.c, 0) + ifnull(tbl6.c, 0) as activity from users u
left join (select cu.user_id, count(*) as c from communities_users cu group by cu.user_id) tbl1 ON tbl1.user_id = u.id
left join (select f.user_id, count(*) as c from friendship f group by f.user_id) tbl2 ON tbl2.user_id = u.id
left join (select l.user_id, count(*) as c from likes l group by l.user_id) tbl3 ON tbl3.user_id = u.id
left join (select m.user_id, count(*) as c from media m group by m.user_id) tbl4 ON tbl4.user_id = u.id
left join (select m2.from_user_id as user_id, count(*) as c from messages m2 group by m2.from_user_id) tbl5 ON tbl5.user_id = u.id
left join (select p.user_id, count(*) as c from posts p group by p.user_id) tbl6 ON tbl6.user_id = u.id order by activity LIMIT 10