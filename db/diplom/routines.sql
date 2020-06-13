use mvideo;

# Процедура пересчета цены заказа
create procedure recalc_order_price(IN order_id int)
BEGIN
    update orders o
    set o.total_price = (select sum(cp.discount_price)
                         from order_products op
                                  left join current_prices cp ON op.product_id = cp.id
                         where op.order_id = order_id)
    where o.id = order_id;
end;

# Триггеры для вызова процедуры пересчета цены зкааз при изменении количества позиций в заказе
CREATE TRIGGER order_insert AFTER INSERT ON order_products FOR EACH ROW call recalc_order_price(NEW.order_id);
CREATE TRIGGER order_delete AFTER DELETE ON order_products FOR EACH ROW call recalc_order_price(OLD.order_id);
