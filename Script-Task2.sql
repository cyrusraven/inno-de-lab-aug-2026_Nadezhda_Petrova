create table Departments (
DepartmentID SERIAL PRIMARY KEY,
DepartmentName VARCHAR(50) UNIQUE NOT NULL,
Location VARCHAR(50)
);

alter table employees add column Email varchar(100);

update employees 
set Email = 
    CASE employeeid
        WHEN 1 THEN 'alicesmith@gmail.com'
        WHEN 2 THEN 'bobjohnson@gmail.com'
        WHEN 3 THEN 'charliebrown@gmai.com'
        when 4 then 'dianaprince@gmail.com'
        when 6 then 'jamesanderson@gmai.com'
        when 7 then 'sophiawilliams@gmail.com'
    END;

alter table employees add constraint uq_email unique (Email);

alter table departments rename column location to OfficeLocation;