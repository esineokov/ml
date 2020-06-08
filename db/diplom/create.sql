create schema mvideo;

use mvideo;

create table actions
(
	id int auto_increment comment 'первичный ключ'
		primary key,
	name varchar(100) not null comment 'название',
	create_at datetime default CURRENT_TIMESTAMP not null comment 'дата создания',
	update_at datetime default CURRENT_TIMESTAMP not null on update CURRENT_TIMESTAMP comment 'дата обновления',
	date_from datetime not null comment 'дата начала',
	date_to datetime not null comment 'дата окончания',
	active tinyint(1) default 0 not null comment 'статус активности'
)
comment 'акции';

create table categories
(
	id int auto_increment comment 'первичный ключ'
		primary key,
	name varchar(100) not null comment 'имя категории',
	create_at datetime default CURRENT_TIMESTAMP not null comment 'дата создания',
	update_at datetime default CURRENT_TIMESTAMP not null on update CURRENT_TIMESTAMP comment 'дата обновления'
)
comment 'категории товаров';

create table order_status
(
	id int auto_increment comment 'первичный ключ'
		primary key,
	name varchar(20) not null comment 'название'
)
comment 'статус заказа';

create table products
(
	id int auto_increment comment 'первичный ключ'
		primary key,
	name varchar(100) null comment 'название товара',
	create_at datetime default CURRENT_TIMESTAMP not null comment 'дата создания',
	update_at datetime default CURRENT_TIMESTAMP not null on update CURRENT_TIMESTAMP comment 'дата обновления',
	deleted tinyint(1) default 0 not null comment 'признак удаления'
)
comment 'товары';

create table action_categories
(
	id int auto_increment comment 'первичный ключ'
		primary key,
	action_id int not null comment 'id акции',
	category_id int null comment 'категория товара',
	product_id int null comment 'id товара',
	include int default 1 not null comment 'статус причастности к акции',
	constraint action_categories_actions_id_fk
		foreign key (action_id) references actions (id),
	constraint action_categories_categories_id_fk
		foreign key (category_id) references categories (id),
	constraint action_categories_products_id_fk
		foreign key (product_id) references products (id)
)
comment 'категории и товары для акции';

create table prices
(
	id int auto_increment comment 'первичный ключ'
		primary key,
	product_id int not null comment 'id товара',
	date_from datetime default CURRENT_TIMESTAMP not null comment 'дата и время, с которого установлена цена',
	date_to datetime null comment 'дата и время, по которое действовала цена',
	constraint prices_products_id_fk
		foreign key (product_id) references products (id)
)
comment 'цены товаров';

create table product_categories
(
	product_id int not null comment 'id товара',
	category_id int not null comment 'id категории',
	constraint product_categories_categories_id_fk
		foreign key (category_id) references categories (id),
	constraint product_categories_products_id_fk
		foreign key (product_id) references products (id)
)
comment 'категории за которыми закреплены продукты';

create index product_categories_product_id_category_id_index
	on product_categories (product_id, category_id);

create table stores
(
	id int auto_increment comment 'первичный ключ'
		primary key,
	name varchar(100) not null comment 'название',
	city varchar(50) not null comment 'город',
	address varchar(100) not null comment 'адрес',
	phone varchar(20) not null comment 'телефон'
)
comment 'склад/магазин';

create table stocks
(
	product_id int not null comment 'id товара',
	store_id int not null comment 'id склада/магазина',
	count int default 0 not null,
	constraint stocks_product_id_store_id_uindex
		unique (product_id, store_id),
	constraint stocks_stores_id_fk
		foreign key (store_id) references stores (id)
)
comment 'складской учет товаров';

create table users
(
	id int auto_increment comment 'первичный ключ'
		primary key,
	email varchar(50) null comment 'почта',
	phone varchar(20) null comment 'телефон',
	name varchar(50) not null comment 'имя',
	blocked tinyint(1) default 0 not null comment 'статус блокировки',
	create_at datetime default CURRENT_TIMESTAMP not null comment 'дата создания',
	update_at datetime default CURRENT_TIMESTAMP not null on update CURRENT_TIMESTAMP comment 'дата обновления',
	confirmed int default 0 not null comment 'статус верификации покупателя'
)
comment 'покупатели';

create table orders
(
	id int auto_increment comment 'первичный ключ'
		primary key,
	user_id int not null comment 'id покупателя',
	create_at datetime default CURRENT_TIMESTAMP not null comment 'дата создания',
	update_at datetime default CURRENT_TIMESTAMP not null on update CURRENT_TIMESTAMP comment 'дата обновления',
	total_price int not null comment 'сумма заказа',
	status_id int default 0 not null comment 'статус заказа',
	constraint orders_order_status_id_fk
		foreign key (status_id) references order_status (id),
	constraint orders_users_id_fk
		foreign key (user_id) references users (id)
)
comment 'заказы';

create table order_products
(
	id int auto_increment comment 'первичный ключ'
		primary key,
	order_id int not null comment 'id заказа',
	product_id int not null comment 'id товара',
	constraint order_products_orders_id_fk
		foreign key (order_id) references orders (id),
	constraint order_products_products_id_fk
		foreign key (product_id) references products (id)
)
comment 'позциии заказа';

create table user_cards
(
	id int auto_increment comment 'первичный ключ'
		primary key,
	user_id int not null comment 'id покупателя',
	code varchar(50) not null comment 'код карты',
	points int default 0 not null comment 'баллы',
	create_at datetime default CURRENT_TIMESTAMP not null comment 'дата создания',
	update_at datetime default CURRENT_TIMESTAMP not null on update CURRENT_TIMESTAMP comment 'дата обновления',
	blocked tinyint(1) default 0 not null comment 'статус блокировки',
	constraint user_cards_users_id_fk
		foreign key (user_id) references users (id)
)
comment 'бонусные карты покупателей';

