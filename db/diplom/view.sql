use mvideo2;

CREATE VIEW current_prices AS 
    select p.id AS id,
           pc.category_id AS category_id,
           p2.price AS price,
           sum(ifnull(a.discount,0)) AS total_discount,
           round((p2.price - ((p2.price / 100) * sum(ifnull(a.discount,0)))),2) AS discount_price 
    from products p
        left join prices p2 on p.id = p2.product_id
        left join product_categories pc on p.id = pc.product_id
        left join action_categories ac on (p.id = ac.product_id or pc.category_id = ac.category_id) and ac.include = 1
        left join actions a on ac.action_id = a.id and now() between a.date_from and a.date_to and a.active = 1
    where p2.date_to is null and p2.price is not null group by p.id,pc.category_id, p2.price;


CREATE VIEW product_stocks AS
    select p.id AS id,
           p.name AS name,
           ifnull(sum(s2.count),0) AS total_count
    from products p
    left join stocks s2 on p.id = s2.product_id
    group by p.id, p.name;

