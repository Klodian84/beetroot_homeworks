-- 1. Display the names (first_name, last_name) using alias "First Name" and "Last Name" from the table of employees
SELECT first_name AS "First Name", last_name AS "Last Name"
FROM staff;

-- 2. Get the unique department ID from the employee table
SELECT DISTINCT department_id
FROM staff;

-- 3. Get all employee details from the employee table ordered by first name in descending order
SELECT *
FROM staff
ORDER BY first_name DESC;

-- 4. Get the names (first_name, last_name), salary, and PF (calculated as 12% of salary) of all employees
SELECT first_name, last_name, salary, (salary * 0.12) AS PF
FROM staff;

-- 5. Get the maximum and minimum salary from the employees table
SELECT MAX(salary) AS "Max Salary", MIN(salary) AS "Min Salary"
FROM staff;
