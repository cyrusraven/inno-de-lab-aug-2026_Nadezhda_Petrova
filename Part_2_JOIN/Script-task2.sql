-- s.status - From table Shippings
-- c.first_name, c.last_name - From table Customers
select s.status, c.first_name, c.last_name
from customers as c
inner join shippings as s
	-- Linking by customer_id
	on c.customer_id = s.customer
-- Sorting by ID клиента
order by c.customer_id;