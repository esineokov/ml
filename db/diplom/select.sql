use mvideo;

# Активнные бонусные карты покупателя
select u.id, u.email, uc.code, uc.points from users u left join user_cards uc on u.id = uc.user_id where u.id = 1;

# Все заказы покупателя с ценой, статусом и количеством товаров в заказе
select u.id, u.email, o.create_at, o.total_price, os.name, count(*)
from users u
    left join orders o on u.id = o.user_id
    left join order_status os on o.status_id = os.id
    left join order_products op on o.id = op.order_id
where u.id = 3 group by u.id, u.email, o.create_at, o.total_price, os.name;

# Цена товара на момент заказ
select p.id, p.price, o.* from order_products pp
    left join orders o ON pp.order_id = o.id
    left join prices p on pp.product_id = p.product_id
where o.create_at between p.date_from and IFNULL(p.date_to, NOW())