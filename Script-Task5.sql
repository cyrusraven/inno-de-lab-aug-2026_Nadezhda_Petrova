create or replace function CalculateAnnualBonus(
    employee_id INT,
    salary DECIMAL
)
returns DECIMAL as $$
begin
    return salary * 0.10;
end;
$$ language plpgsql;

select 
    employeeid,
    firstname,
    lastname,
    salary,
    CalculateAnnualBonus(employeeid, salary) as Bonus
from employees;

create or replace view IT_Department_View as
select 
    employeeid,
    firstname,
    lastname,
    salary
from employees
where department = 'Senior IT';

select * from IT_Department_View;