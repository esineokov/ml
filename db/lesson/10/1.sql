-- 1. Проанализировать какие запросы могут выполняться наиболее часто в процессе работы приложения и добавить необходимые индексы.

# USERS: Индексы first_name, last_name для поиска пользователй
create index users_first_name_index
	on users (first_name);

create index users_last_name_index
	on users (last_name);
# ------------------------------------------
# PROFILES: Индексы для быстрого поиска по параметрам пользователя
# Дни рождения часто надо селектить для вызова напоминания друзьям пользователя о его дне рождения.
create index profiles_birthday_index
    on vk.profiles (birthday);

# Для поиска по городу
create index profiles_city_index
    on vk.profiles (city);

# Поиск по стране
create index profiles_country_index
    on vk.profiles (country);

# Поиск по половому признаку
create index profiles_gender_index
    on vk.profiles (gender);
# ------------------------------------------
# POSTS:
# Индекс для быстрой выборки всех постов сообщества
create index posts_community_id_index
	on posts (community_id);

# Индекс для поиска по тексту заголовка
create index posts_head_index
	on posts (head);

# ------------------------------------------
# MESSAGES:
# Для быстрой выборки всех сообщений одного пользователя
create index messages_from_user_id_index
	on messages (from_user_id);

# Для быстрой ваборки всех сообщений к одному пользователю
create index messages_to_user_id_index
	on messages (to_user_id);

# ------------------------------------------
# LIKES:
# Быстрый поиск количества лайков для конкретной позиции
create index likes_target_id_target_type_id_index
	on likes (target_id, target_type_id);
