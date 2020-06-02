# Практическое задание по теме “Транзакции, переменные, представления”

# 1) В базе данных shop и sample присутствуют одни и те же таблицы, учебной базы данных. Переместите запись id = 1 из таблицы shop.users в таблицу sample.users. Используйте транзакции.
START TRANSACTION;
INSERT INTO sample.users (id, name, birthday_at, created_at, updated_at)
SELECT * FROM shop.users su where su.id = 1
ON DUPLICATE KEY UPDATE sample.users.name = su.name,
                        sample.users.birthday_at = su.birthday_at,
                        sample.users.created_at = su.created_at,
                        sample.users.updated_at = su.updated_at;
DELETE FROM shop.users where id = 1;
COMMIT;

# 2) Создайте представление, которое выводит название name товарной позиции из таблицы products и соответствующее название каталога name из таблицы catalogs.
CREATE VIEW `product_catalog` AS SELECT p.name as pname, c.name as cname FROM products p left join catalogs c on p.catalog_id = c.id


# Практическое задание по теме “Хранимые процедуры и функции, триггеры"
# 1) Создайте хранимую функцию hello(), которая будет возвращать приветствие, в зависимости от текущего времени суток. С 6:00 до 12:00 функция должна возвращать фразу "Доброе утро", с 12:00 до 18:00 функция должна возвращать фразу "Добрый день", с 18:00 до 00:00 — "Добрый вечер", с 00:00 до 6:00 — "Доброй ночи".
DELIMITER $$
CREATE FUNCTION hello()
RETURNS VARCHAR(50)
DETERMINISTIC
BEGIN
    DECLARE dt time;
    SET dt = CURRENT_TIME();

    IF dt BETWEEN TIME('05:59:59') and TIME('11:59:59') THEN
		RETURN 'Доброе утро';
	END IF;
	IF dt BETWEEN TIME('12:00:00') and TIME('17:59:59') THEN
		RETURN 'Добрый день';
	END IF;
	IF dt BETWEEN TIME('18:00:00') and TIME('23:59:59') THEN
		RETURN 'Добрый вечер';
	END IF;
	IF dt BETWEEN TIME('00:00:00') and TIME('06:00:00') THEN
		RETURN 'Доброй ночи';
	END IF;
END$$
DELIMITER ;

# 2) .В таблице products есть два текстовых поля: name с названием товара и
#  description с его описанием. Допустимо присутствие обоих полей или одного из них.
#  Ситуация, когда оба поля принимают неопределенное значение NULL неприемлема.
#  Используя триггеры, добейтесь того, чтобы одно из этих полей или оба поля были заполнены.
#  При попытке присвоить полям NULL-значение необходимо отменить операцию.

DELIMITER //

CREATE TRIGGER products_insert BEFORE INSERT ON products
FOR EACH ROW BEGIN
  IF NEW.name IS NULL AND NEW.description IS NULL THEN
    SIGNAL SQLSTATE '42000'
    SET MESSAGE_TEXT = 'Both name and description are NULL';
  END IF;
END//

CREATE TRIGGER products_update BEFORE UPDATE ON products
FOR EACH ROW BEGIN
  IF NEW.name IS NULL AND NEW.description IS NULL THEN
    SIGNAL SQLSTATE '42000'
    SET MESSAGE_TEXT = 'Both name and description are NULL';
  END IF;
END//