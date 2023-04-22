# DROP TABLE

drop_employees_table = 'DROP TABLE IF EXISTS employees'

# CREATE TABLE

create_employees_table = '''
CREATE TABLE IF NOT EXISTS employees
(
employee_id INT PRIMARY KEY,
first_name VARCHAR(50),
last_name VARCHAR(50),
email VARCHAR(50),
hire_date DATE,
shop_name VARCHAR(50),
salary INT
)
'''

# INSERT INTO

insert_employees_table = '''
INSERT INTO employees
(employee_id, first_name, last_name, email, hire_date, shop_name, salary)
VALUES (%s, %s, %s, %s, %s, %s, %s)
'''