-- Практическое задание по теме “Операторы, фильтрация, сортировка и ограничение”

-- 1. Пусть в таблице users поля created_at и updated_at оказались незаполненными. Заполните их текущими датой и временем.
UPDATE users set created_at = NOW();
-- updated_at подставит NOW() автоматически поскольку оно 'ON UPDATE CURRENT_TIMESTAMP'


-- 2. Таблица users была неудачно спроектирована.
-- Записи created_at и updated_at были заданы типом VARCHAR и в них долгое время помещались значения
-- в формате "20.10.2017 8:10". Необходимо преобразовать поля к типу DATETIME, сохранив введеные ранее значения.

UPDATE users set created_at = STR_TO_DATE(created_at, "%d.%m.%Y %k:%i"), updated_at = STR_TO_DATE(updated_at, "%d.%m.%Y %k:%i")
ALTER TABLE users
CHANGE created_at created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
CHANGE updated_at updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP;


-- 3. В таблице складских запасов storehouses_products в поле value могут встречаться самые разные цифры: 0,
-- если товар закончился и выше нуля, если на складе имеются запасы.
-- Необходимо отсортировать записи таким образом, чтобы они выводились в порядке увеличения значения value.
-- Однако, нулевые запасы должны выводиться в конце, после всех записей.
SELECT * FROM storehouses_products ORDER BY IF(value > 0, 0, 1), value;


-- 4. (по желанию) Из таблицы users необходимо извлечь пользователей, родившихся в августе и мае.
-- Месяцы заданы в виде списка английских названий ('may', 'august')
SELECT name FROM users where DATE_FORMAT(birthday_at, '%M') in ('may', 'august');


-- 5. (по желанию) Из таблицы catalogs извлекаются записи при помощи запроса.
-- SELECT * FROM catalogs WHERE id IN (5, 1, 2); Отсортируйте записи в порядке, заданном в списке IN.
select * from catalogs c where id in (5,1,2) ORDER  BY FIELD(id, 5,1,2)


-- Практическое задание теме “Агрегация данных”
-- 1. Подсчитайте средний возраст пользователей в таблице users
SELECT AVG(TIMESTAMPDIFF(YEAR, birthday_at, NOW())) as age FROM users u ;

-- 2. Подсчитайте количество дней рождения, которые приходятся на каждый из дней недели.
-- Следует учесть, что необходимы дни недели текущего года, а не года рождения.
SELECT
	DATE_FORMAT(DATE(CONCAT_WS('-', YEAR(NOW()), MONTH(birthday_at), DAY(birthday_at))), '%W')  as day,
	COUNT(*) as total
FROM users
	GROUP BY day
	ORDER BY total DESC;

-- 	3. (по желанию) Подсчитайте произведение чисел в столбце таблицы
SELECT EXP(SUM(LN(id))) FROM catalogs;