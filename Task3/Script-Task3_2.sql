SELECT current_user;

SELECT * FROM Employees;

INSERT INTO Employees (FirstName, LastName, Department, Salary)
VALUES ('John', 'Doe', 'IT', 55000.00);


UPDATE employees
SET Salary = 75000.00
WHERE EmployeeID = 9;