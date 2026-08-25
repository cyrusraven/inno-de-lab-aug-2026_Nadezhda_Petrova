insert into employees (FirstName, LastName, Department, Salary) values
('James', 'Anderson', 'Finance', 65000.00),
('Sophia', 'Williams', 'HR', 55000.00);

select FirstName || ' ' || LastName as full_name
from employees;

select FirstName, LastName
from employees
where Department = 'IT';

update employees
set Salary = 65000.00
where FirstName = 'Alice' and LastName = 'Smith';

delete from employees
where FirstName = 'Eve' and LastName = 'Davis';

SELECT * FROM employees;