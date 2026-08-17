update employees 
set salary = salary * 1.10
where department = 'HR';

update employees 
set department = 'Senior IT'
where salary > 70000.00;

delete from employees 
where not exists (
	select 1
	from employeeprojects
	where employeeprojects.employeeid  = employees.employeeid );


begin;

with new_project as (
    insert into projects (projectname, budget, startdate, enddate)
    values ('AI Migration', 120000.00, '2023-06-10', '2023-12-31')
    returning projectid
)
insert into employeeprojects (employeeid, projectid, hoursworked)
select
    employeeid,
    (select projectid from new_project),
    hoursworked
from (values (1, 40), (2, 35)) as emp(employeeid, hoursworked);

commit;
