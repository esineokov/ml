-- 4. Определить кто больше поставил лайков (всего) - мужчины или женщины?

-- 1) Вариант
select p.gender, count(p.gender) as likes_count from likes as l, profiles as p where p.user_id = l.user_id group by p.gender;

-- 2) Вариант
SELECT IF(
    (select count(p.gender) as likes_count from likes as l, profiles as p where p.user_id = l.user_id and p.gender = 'm' group by p.gender) >
    (select count(p.gender) as likes_count from likes as l, profiles as p where p.user_id = l.user_id and p.gender = 'w' group by p.gender),
    'Мужчины', 'Женщины') 'Больше всего лайков поставили'