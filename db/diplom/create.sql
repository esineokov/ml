create schema mvideo;
use mvideo;

DROP TABLE IF EXISTS `actions`;
CREATE TABLE `actions` (
  `id` int NOT NULL AUTO_INCREMENT COMMENT 'первичный ключ',
  `name` varchar(100) NOT NULL COMMENT 'название',
  `create_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'дата создания',
  `update_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT 'дата обновления',
  `discount` int NOT NULL,
  `date_from` datetime NOT NULL COMMENT 'дата начала',
  `date_to` datetime NOT NULL COMMENT 'дата окончания',
  `active` tinyint(1) NOT NULL DEFAULT '0' COMMENT 'статус активности',
  PRIMARY KEY (`id`)
) COMMENT='акции';


DROP TABLE IF EXISTS `categories`;
CREATE TABLE `categories` (
  `id` int NOT NULL AUTO_INCREMENT COMMENT 'первичный ключ',
  `name` varchar(100) NOT NULL COMMENT 'имя категории',
  `create_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'дата создания',
  `update_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT 'дата обновления',
  PRIMARY KEY (`id`)
) COMMENT='категории товаров';


DROP TABLE IF EXISTS `order_status`;
CREATE TABLE `order_status` (
  `id` int NOT NULL AUTO_INCREMENT COMMENT 'первичный ключ',
  `name` varchar(20) NOT NULL COMMENT 'название',
  PRIMARY KEY (`id`)
) COMMENT='статус заказа';


DROP TABLE IF EXISTS `products`;
CREATE TABLE `products` (
  `id` int NOT NULL AUTO_INCREMENT COMMENT 'первичный ключ',
  `name` varchar(100) DEFAULT NULL COMMENT 'название товара',
  `create_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'дата создания',
  `update_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT 'дата обновления',
  `deleted` tinyint(1) NOT NULL DEFAULT '0' COMMENT 'признак удаления',
  PRIMARY KEY (`id`)
) COMMENT='товары';

DROP TABLE IF EXISTS `action_categories`;
CREATE TABLE `action_categories` (
  `id` int NOT NULL AUTO_INCREMENT COMMENT 'первичный ключ',
  `action_id` int NOT NULL COMMENT 'id акции',
  `category_id` int DEFAULT NULL COMMENT 'категория товара',
  `product_id` int DEFAULT NULL COMMENT 'id товара',
  `include` int NOT NULL DEFAULT '1' COMMENT 'статус причастности к акции',
  PRIMARY KEY (`id`),
  KEY `action_categories_actions_id_fk` (`action_id`),
  KEY `action_categories_categories_id_fk` (`category_id`),
  KEY `action_categories_products_id_fk` (`product_id`),
  CONSTRAINT `action_categories_actions_id_fk` FOREIGN KEY (`action_id`) REFERENCES `actions` (`id`),
  CONSTRAINT `action_categories_categories_id_fk` FOREIGN KEY (`category_id`) REFERENCES `categories` (`id`),
  CONSTRAINT `action_categories_products_id_fk` FOREIGN KEY (`product_id`) REFERENCES `products` (`id`)
) COMMENT='категории и товары для акции';


DROP TABLE IF EXISTS `prices`;
CREATE TABLE `prices` (
  `id` int NOT NULL AUTO_INCREMENT COMMENT 'первичный ключ',
  `product_id` int NOT NULL COMMENT 'id товара',
  `price` float DEFAULT NULL COMMENT 'цена',
  `date_from` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'дата и время, с которого установлена цена',
  `date_to` datetime DEFAULT NULL COMMENT 'дата и время, по которое действовала цена',
  PRIMARY KEY (`id`),
  KEY `prices_products_id_fk` (`product_id`),
  CONSTRAINT `prices_products_id_fk` FOREIGN KEY (`product_id`) REFERENCES `products` (`id`)
) COMMENT='цены товаров';


DROP TABLE IF EXISTS `product_categories`;
CREATE TABLE `product_categories` (
  `product_id` int NOT NULL COMMENT 'id товара',
  `category_id` int NOT NULL COMMENT 'id категории',
  KEY `product_categories_categories_id_fk` (`category_id`),
  KEY `product_categories_product_id_category_id_index` (`product_id`,`category_id`),
  CONSTRAINT `product_categories_categories_id_fk` FOREIGN KEY (`category_id`) REFERENCES `categories` (`id`),
  CONSTRAINT `product_categories_products_id_fk` FOREIGN KEY (`product_id`) REFERENCES `products` (`id`)
) COMMENT='категории за которыми закреплены продукты';


DROP TABLE IF EXISTS `stores`;
CREATE TABLE `stores` (
  `id` int NOT NULL AUTO_INCREMENT COMMENT 'первичный ключ',
  `name` varchar(100) NOT NULL COMMENT 'название',
  `city` varchar(50) NOT NULL COMMENT 'город',
  `address` varchar(100) NOT NULL COMMENT 'адрес',
  `phone` varchar(20) NOT NULL COMMENT 'телефон',
  PRIMARY KEY (`id`)
) COMMENT='склад/магазин';


DROP TABLE IF EXISTS `stocks`;
CREATE TABLE `stocks` (
  `product_id` int NOT NULL COMMENT 'id товара',
  `store_id` int NOT NULL COMMENT 'id склада/магазина',
  `count` int NOT NULL DEFAULT '0',
  UNIQUE KEY `stocks_product_id_store_id_uindex` (`product_id`,`store_id`),
  KEY `stocks_stores_id_fk` (`store_id`),
  CONSTRAINT `stocks_stores_id_fk` FOREIGN KEY (`store_id`) REFERENCES `stores` (`id`)
) COMMENT='складской учет товаров';


DROP TABLE IF EXISTS `users`;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT COMMENT 'первичный ключ',
  `email` varchar(50) DEFAULT NULL COMMENT 'почта',
  `phone` varchar(20) DEFAULT NULL COMMENT 'телефон',
  `name` varchar(50) NOT NULL COMMENT 'имя',
  `blocked` tinyint(1) NOT NULL DEFAULT '0' COMMENT 'статус блокировки',
  `create_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'дата создания',
  `update_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT 'дата обновления',
  `confirmed` int NOT NULL DEFAULT '0' COMMENT 'статус верификации покупателя',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='покупатели';


DROP TABLE IF EXISTS `orders`;
CREATE TABLE `orders` (
  `id` int NOT NULL AUTO_INCREMENT COMMENT 'первичный ключ',
  `user_id` int NOT NULL COMMENT 'id покупателя',
  `create_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'дата создания',
  `update_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT 'дата обновления',
  `total_price` int NOT NULL COMMENT 'сумма заказа',
  `status_id` int NOT NULL DEFAULT '0' COMMENT 'статус заказа',
  PRIMARY KEY (`id`),
  KEY `orders_order_status_id_fk` (`status_id`),
  KEY `orders_users_id_fk` (`user_id`),
  CONSTRAINT `orders_order_status_id_fk` FOREIGN KEY (`status_id`) REFERENCES `order_status` (`id`),
  CONSTRAINT `orders_users_id_fk` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) COMMENT='заказы';


DROP TABLE IF EXISTS `order_products`;
CREATE TABLE `order_products` (
  `id` int NOT NULL AUTO_INCREMENT COMMENT 'первичный ключ',
  `order_id` int NOT NULL COMMENT 'id заказа',
  `product_id` int NOT NULL COMMENT 'id товара',
  PRIMARY KEY (`id`),
  KEY `order_products_orders_id_fk` (`order_id`),
  KEY `order_products_products_id_fk` (`product_id`),
  CONSTRAINT `order_products_orders_id_fk` FOREIGN KEY (`order_id`) REFERENCES `orders` (`id`),
  CONSTRAINT `order_products_products_id_fk` FOREIGN KEY (`product_id`) REFERENCES `products` (`id`)
)  COMMENT='позциии заказа';


DROP TABLE IF EXISTS `user_cards`;
CREATE TABLE `user_cards` (
  `id` int NOT NULL AUTO_INCREMENT COMMENT 'первичный ключ',
  `user_id` int NOT NULL COMMENT 'id покупателя',
  `code` varchar(50) NOT NULL COMMENT 'код карты',
  `points` int NOT NULL DEFAULT '0' COMMENT 'баллы',
  `create_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'дата создания',
  `update_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT 'дата обновления',
  `blocked` tinyint(1) NOT NULL DEFAULT '0' COMMENT 'статус блокировки',
  PRIMARY KEY (`id`),
  KEY `user_cards_users_id_fk` (`user_id`),
  CONSTRAINT `user_cards_users_id_fk` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) COMMENT='бонусные карты покупателей';