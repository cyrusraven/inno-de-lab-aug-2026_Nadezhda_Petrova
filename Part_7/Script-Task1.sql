select 
    c.first_name || ' ' || c.last_name as full_name,
    c.country,
    count(o.order_id) as total_orders,
    sum(o.amount) as total_amount
from customers as c
join orders as o on c.customer_id = o.customer_id
-- Filter customers who have at least one delivered shipment
where exists (
    select 1
    from shippings as s
    where s.customer = c.customer_id
      and s.status = 'Delivered'
)
group by c.customer_id, c.first_name, c.last_name, c.country
-- Keep only customers with at least 2 orders
having count(o.order_id) >= 2;    