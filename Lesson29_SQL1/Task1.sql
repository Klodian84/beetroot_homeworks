-- 1. Create a table named "employees" in the SQLite database
CREATE TABLE employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    position TEXT NOT NULL
);

-- 2. Rename the table from "employees" to "staff"
ALTER TABLE employees RENAME TO staff;

-- 3. Add a new column "salary" to the "staff" table
ALTER TABLE staff ADD COLUMN salary REAL;

-- 4. Insert a couple of rows into the "staff" table
INSERT INTO staff (name, position, salary) VALUES ('Alice Smith', 'Manager', 75000.00);
INSERT INTO staff (name, position, salary) VALUES ('Bob Johnson', 'Developer', 65000.00);

-- 5. Update the salary of one of the employees
UPDATE staff SET salary = 70000.00 WHERE name = 'Bob Johnson';

-- 6. Delete one of the rows
DELETE FROM staff WHERE name = 'Alice Smith';

-- To confirm the changes (optional): Select all remaining records in "staff" table
SELECT * FROM staff;
