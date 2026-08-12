select order_id, customer_id, item, amount,
	-- Window function: calculates the total sum of all orders for the same customer
	sum(amount) over (partition by customer_id) as total_by_customer
from orders
order by order_id;