-- 2. Создать и заполнить таблицы лайков и постов.

-- Заполняем communities_users
DROP procedure IF EXISTS `GenerateCommunityUsers`;
DELIMITER //
create procedure GenerateCommunityUsers()
BEGIN
	DECLARE done INT DEFAULT FALSE;
    DECLARE community_id INT;
	DECLARE community_cur CURSOR FOR SELECT id FROM communities;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

    OPEN community_cur;
    read_loop: LOOP
		FETCH community_cur INTO community_id;
        IF done THEN
			LEAVE read_loop;
        END IF;
        INSERT INTO communities_users SELECT community_id, users.id from users WHERE NOT EXISTS (SELECT 1 FROM communities_users  where community_id=community_id and user_id = users.id) ORDER BY RAND() LIMIT 10;
    END LOOP;
END //
DELIMITER ;

CALL GenerateCommunityUsers();
DROP procedure IF EXISTS `GenerateCommunityUsers`;

-- Заполняем таблицу posts
DROP procedure IF EXISTS `GeneratePosts`;
DELIMITER //
create procedure GeneratePosts()
BEGIN
    DECLARE v_user_id INT;
	DECLARE head VARCHAR(255);
    DECLARE body VARCHAR(255);
    DECLARE media_id INT;
    DECLARE is_public INT;
    DECLARE is_archived INT;
	DECLARE views_counter INT;
	DECLARE done INT DEFAULT FALSE;
    DECLARE community_id INT;
	DECLARE community_cur CURSOR FOR SELECT id FROM communities;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

    OPEN community_cur;
    read_loop: LOOP
		FETCH community_cur INTO community_id;
        IF done THEN
			LEAVE read_loop;
        END IF;
        SET v_user_id = (SELECT user_id FROM communities_users WHERE community_id = community_id ORDER BY RAND() LIMIT 1);
        IF v_user_id is NOT NULL THEN
			SET head = UUID();
			SET body = UUID();
			SET media_id = (select id from media ORDER BY RAND() LIMIT 1);
			SET is_public = (SELECT FLOOR(RAND()*(1-0+1))+0);
			SET is_archived = (SELECT FLOOR(RAND()*(1-0+1))+0);
			SET views_counter = (SELECT FLOOR(RAND()*(100-0+1))+0);
			INSERT INTO posts (user_id, community_id, head, body, media_id, is_public, is_archived, views_counter, created_at, updated_at)  SELECT v_user_id, community_id, head, body, media_id, is_public, is_archived, views_counter, NOW(), NOW() from dual;
		END IF;
    END LOOP;
END //
DELIMITER ;

CALL GeneratePosts();
CALL GeneratePosts();
CALL GeneratePosts();
CALL GeneratePosts();
CALL GeneratePosts();
DROP procedure IF EXISTS `GeneratePosts`;


-- Заполняем таблицу likes
DROP procedure IF EXISTS `GenerateLikes`;
DELIMITER //
create procedure GenerateLikes()
BEGIN
    DECLARE v_user_id INT;
    DECLARE done INT DEFAULT FALSE;
    DECLARE users_cur CURSOR FOR SELECT id FROM users;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

    OPEN users_cur;
    read_loop: LOOP
        FETCH users_cur INTO v_user_id;
        IF done THEN
			LEAVE read_loop;
        END IF;
        INSERT INTO likes (user_id, target_id, target_type_id) SELECT v_user_id, (select id from messages ORDER BY RAND() LIMIT 1), 1;
        INSERT INTO likes (user_id, target_id, target_type_id) SELECT v_user_id, (select id from users ORDER BY RAND() LIMIT 1), 2;
        INSERT INTO likes (user_id, target_id, target_type_id) SELECT v_user_id, (select id from media ORDER BY RAND() LIMIT 1), 3;
        INSERT INTO likes (user_id, target_id, target_type_id) SELECT v_user_id, (select id from posts ORDER BY RAND() LIMIT 1), 4;
    END LOOP;
END //
DELIMITER ;

CALL GenerateLikes();
CALL GenerateLikes();
CALL GenerateLikes();
CALL GenerateLikes();
CALL GenerateLikes();
DROP procedure IF EXISTS `GenerateLikes`;