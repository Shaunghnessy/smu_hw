--1.List the employee number, last name, first name, sex, and salary of each employee.

SELECT 
         employees.emp_no 
AS 
         employee_number, 
         employees.last_name, 
         employees.first_name, 
         employees.sex, 
         salaries.salary
FROM 
         employees
JOIN 
         salaries 
ON 
         employees.emp_no = salaries.emp_no
ORDER BY
         employee_number
LIMIT (5);

--2.List the first name, last name, and hire date for the employees who were hired in 1986.

SELECT 
	* 
FROM 
	employees
WHERE 
	DATE_PART('year',hire_date) = 1986
ORDER BY emp_no
LIMIT 5;

--3.List the manager of each department along with their department number, department name, employee number, last name, and first name.

SELECT 
	managers.dept_no, 
	departments.dept_name, 
	managers.emp_no, 
	employees.last_name, 
	employees.first_name
FROM 
	managers
JOIN 
	employees 
ON 
	managers.emp_no = employees.emp_no
JOIN 
	departments 
ON 
	managers.dept_no = departments.dept_no
LIMIT (5);

--4.List the department number for each employee along with that employee’s employee number, last name, first name, and department name.

SELECT 
employees.emp_no,
	employees.last_name, 
	employees.first_name, 
	departments.dept_name
FROM 
	employees
JOIN 
	departments_employees 
ON 
employees.emp_no = departments_employees.emp_no
JOIN 
	departments 
ON 
departments_employees.dept_no = departments.dept_no
LIMIT (5);

--5.List first name, last name, and sex of each employee whose first name is Hercules and whose last name begins with the letter B.

SELECT 
employees.first_name, 
	employees.last_name, 
	employees.sex
FROM 
	employees
WHERE 
	first_name = 'Hercules' AND last_name LIKE 'B%'
LIMIT (5);

--6.List each employee in the Sales department, including their employee number, last name, and first name.

SELECT 
employees.emp_no, 
	employees.last_name, 
	employees.first_name, 
	departments.dept_name
FROM 
	employees
JOIN 
	departments_employees 
ON 
	employees.emp_no = departments_employees.emp_no
JOIN 
	departments 
ON 
	departments_employees.dept_no = departments.dept_no
WHERE 
	departments.dept_name = 'Sales'
LIMIT (5);

--7.List each employee in the Sales and Development departments, including their employee number, last name, first name, and department name.

SELECT 
employees.emp_no, 
	employees.last_name, 
	employees.first_name, 
	departments.dept_name
FROM 
	employees
JOIN 
	departments_employees 
ON 
	employees.emp_no = departments_employees.emp_no
JOIN 
	departments 
ON 
	departments_employees.dept_no = departments.dept_no
WHERE 
	departments.dept_name = 'Sales' OR departments.dept_name = 'Development'
LIMIT (5);

--8.List the frequency counts, in descending order, of all the employee last names (that is, how many employees share each last name).

SELECT employees.last_name, Count (*)
FROM employees
GROUP BY employees.last_name
ORDER BY Count (*) DESC
LIMIT 5;
