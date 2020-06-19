# Практическое задание по теме “Оптимизация запросов”

# Создайте таблицу logs типа Archive. Пусть при каждом создании записи в таблицах users,
# catalogs и products в таблицу logs помещается время и дата создания записи, название таблицы,
# идентификатор первичного ключа и содержимое поля name.

CREATE TRIGGER after_users_insert
    AFTER INSERT ON users
    FOR EACH ROW
 INSERT INTO logs VALUES(NOW(), 'users', NEW.id, NEW.name);


CREATE TRIGGER after_catalogs_insert
    AFTER INSERT ON catalogs
    FOR EACH ROW
 INSERT INTO logs VALUES(NOW(), 'catalogs', NEW.id, NEW.name);


CREATE TRIGGER after_products_insert
    AFTER INSERT ON products
    FOR EACH ROW
 INSERT INTO logs VALUES(NOW(), 'products', NEW.id, NEW.name);

# ------------
# (по желанию) Создайте SQL-запрос, который помещает в таблицу users миллион записей.

DROP procedure IF EXISTS `GenerateUsers`;
DELIMITER //
create procedure GenerateUsers()
BEGIN
    DECLARE counter INT DEFAULT 0;
    WHILE counter < 1000000 DO
        SET counter = counter + 1;
        INSERT INTO users (id, name, birthday_at, created_at, updated_at) VALUES (NULL, (SELECT LEFT(UUID(), 8)), (SELECT CURRENT_DATE - INTERVAL (SELECT FLOOR(RAND()*(10000-100+1))+100) DAY), NOW(), NOW());
    END WHILE;
END //
DELIMITER ;

CALL GenerateUsers();
DROP procedure IF EXISTS `GenerateUsers`;


select count(*) from users;