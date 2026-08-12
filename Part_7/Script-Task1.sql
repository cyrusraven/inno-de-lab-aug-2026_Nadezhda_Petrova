select 
	-- We combine the first and last name
    c.first_name || ' ' || c.last_name as full_name,           
    c.country,           
    -- Count of orders
    count(distinct o.order_id) as total_orders,        
    -- Total amount of orders
    sum(o.amount) as total_amount                              
from customers as c
-- We connect with orders
join orders as o on c.customer_id = o.customer_id       
-- We connect with deliveries
join shippings as s on c.customer_id = s.customer   
-- Only delivered
where s.status = 'Delivered'                    
-- Grouping and filtering
group by c.customer_id, c.first_name, c.last_name, c.country   
having count(distinct o.order_id) >= 2;                