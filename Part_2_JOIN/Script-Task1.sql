-- Fulfilling the task condition
-- Selecting the required fields:
-- c.first_name, c.last_name - From the table Customers
-- o.item, o.amount - From the table Orders
select c.first_name, c.last_name, o.item, o.amount
from customers as c
inner join orders as o
	-- Linking by customer_id
	on c.customer_id = o.customer_id  
-- Sorting by ID клиента 
order by c.customer_id; 