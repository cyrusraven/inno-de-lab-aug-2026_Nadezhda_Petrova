select c.first_name, c.last_name, o.amount               
from customers as c
-- Join orders table to get each customer's orders
join orders as o 
	-- Link the two tables using the customer_id foreign key
	on c.customer_id = o.customer_id
where o.amount = (
	-- Subquery: find the highest order amount from the entire orders table
    select MAX(amount) 
    from orders
);