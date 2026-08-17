create user hr_user with password '1234';

create role editor;
grant select on Employees to editor;
grant editor to hr_user;

create role upgrated_editor;
grant insert, update on employees to upgrated_editor;
grant upgrated_editor to hr_user;

grant usage, select on sequence employees_employeeid_seq to hr_user;

