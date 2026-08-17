-- 1. Find the ProjectName of all projects where 'Bob Johnson' worked > 150 hours
select distinct p.projectname
from employees as e
join employeeprojects as ep on e.employeeid = ep.employeeid
join projects as p on ep.projectid = p.projectid
where e.firstname = 'Bob' and e.lastname = 'Johnson'
  and ep.hoursworked > 150;

-- Check: display a list of projects with hours for Bob Johnson
select p.projectname, ep.hoursworked
from employees as e
join employeeprojects as ep on e.employeeid = ep.employeeid
join projects as p on ep.projectid = p.projectid
where e.firstname = 'Bob' and e.lastname = 'Johnson'
order by p.projectname;

-- 2. Increase the budget for all projects by 10% if at least one IT employee is assigned to them
update projects
set budget = budget * 1.10
where projectid in (
    select distinct ep.projectid
    from employeeprojects as ep
    join employees as e on ep.employeeid = e.employeeid
    where e.department = 'Senior IT'
);

-- Check: show the modified budgets (only the affected projects)
select p.projectid, p.projectname, p.budget
from projects as p
where p.projectid in (
    select distinct ep.projectid
    from employeeprojects as ep
    join employees as e on ep.employeeid = e.employeeid
    where e.department = 'Senior IT'
)
order by p.projectid;

-- 3. For any project without an EndDate, set the EndDate to be 1 year later than the StartDate
update projects
set enddate = startdate + INTERVAL '1 year'
where enddate is null;

-- Check: show projects where EndDate was NULL and is now filled in.
select projectid, projectname, startdate, enddate
from projects
where startdate + INTERVAL '1 year' = enddate
   or (enddate is not null and startdate is not null)  
order by projectid;

-- 4. Transaction: add a new employee and assign them to ‘Website Redesign’ with 80 hours
begin;

with new_emp as (
    insert into employees (firstname, lastname, department, salary, email)
    values ('Ivan', 'Ivanov', 'HR', 60000.00, 'ivanivanov@gmail.com')
    returning employeeid
)
insert into employeeprojects (employeeid, projectid, hoursworked)
select 
    (select employeeid from new_emp),
    (select projectid from projects where projectname = 'Website Redesign'),
    80;

commit;

-- Check: show the new employee and their assignment.
select e.employeeid, e.firstname, e.lastname, e.department, e.salary,
       p.projectname, ep.hoursworked
from employees as e
join employeeprojects as ep on e.employeeid = ep.employeeid
join projects as p on ep.projectid = p.projectid
where e.firstname = 'Ivan' and e.lastname = 'Ivanov';