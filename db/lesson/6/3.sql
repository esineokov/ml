-- Подсчитать общее количество лайков десяти самым молодым пользователям (сколько лайков получили 10 самых молодых пользователей).

select user_id, (select likes_count from (select v_user_id, count(v_user_id) as likes_count from (
                  select l.target_id,
                         l.target_type_id,
                         (case
                              WHEN l.target_type_id = 1 THEN (select m.from_user_id from messages as m where m.id = l.target_id)
                              WHEN l.target_type_id = 2 THEN (select u.id from users as u where u.id = l.target_id)
                              WHEN l.target_type_id = 3 THEN (select m.user_id from media as m where m.id = l.target_id)
                              WHEN l.target_type_id = 4 THEN (select p.user_id from posts as p where p.id = l.target_id)
                              ELSE
                                  NULL
                             end) v_user_id
                  from likes as l
              ) as tbl1 where v_user_id is not null group by v_user_id) as tbl2 where v_user_id = user_id) as likes_count
 from profiles order by birthday desc limit 10;
