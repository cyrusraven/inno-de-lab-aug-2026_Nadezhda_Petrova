select item, count(item), trunc(avg(amount), 2) as avg_amount -- Rounding avg(amount) to two decimal places
from orders 
group by item;