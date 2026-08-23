-- Fulfilling the task condition
select order_id, item, amount, customer_id
from Orders
where amount > 1000; -- Where the amount is more than 1000

