employees_drop_sql = ('DROP TABLE IF EXISTS employees')
departments_drop_sql = ('DROP TABLE IF EXISTS departments')
salaries_drop_sql = ('DROP TABLE IF EXISTS salaries')
dept_emp_drop_sql= ('DROP TABLE IF EXISTS dept_emp')
dept_manager_drop_sql = ('DROP TABLE IF EXISTS  dept_manager')
titles_drop_sql = ('DROP TABLE IF EXISTS titles')

employees_create_sql = (
    ''' CREATE TABLE IF NOT EXISTS employees (
            emp_no int NOT NULL AUTO_INCREMENT,
            birth_date date NOT NULL,
            first_name varchar(14) NOT NULL,
            last_name varchar(16) NOT NULL,
            gender enum('M','F') NOT NULL,
            hire_date date NOT NULL,
            PRIMARY KEY (emp_no)
    ) ENGINE=InnoDB
    ''')

departments_create_sql = (
    ''' CREATE TABLE IF NOT EXISTS departments (
            dept_no char(4) NOT NULL,
            dept_name varchar(40) NOT NULL,
            PRIMARY KEY (dept_no), UNIQUE KEY dept_name (dept_name)
    ) ENGINE=InnoDB
    '''
    )

salaries_create_sql = (
    ''' CREATE TABLE IF NOT EXISTS salaries (
            emp_no int NOT NULL,
            salary int NOT NULL,
            from_date date NOT NULL,
            to_date date NOT NULL,
            PRIMARY KEY (emp_no,from_date), KEY emp_no (emp_no),
            CONSTRAINT salaries_ibfk_1 FOREIGN KEY (emp_no) REFERENCES employees (emp_no) ON DELETE CASCADE
    ) ENGINE=InnoDB '''
    )

dept_emp_create_sql = (
    ''' CREATE TABLE IF NOT EXISTS dept_emp (
            emp_no int NOT NULL,
            dept_no char(4) NOT NULL,
            from_date date NOT NULL,
            to_date date NOT NULL,
            PRIMARY KEY (emp_no,dept_no), KEY emp_no (emp_no),
            KEY dept_no (dept_no),
            CONSTRAINT dept_emp_ibfk_1 FOREIGN KEY (emp_no) REFERENCES employees (emp_no) ON DELETE CASCADE,
            CONSTRAINT dept_emp_ibfk_2 FOREIGN KEY (dept_no) REFERENCES departments (dept_no) ON DELETE CASCADE
    ) ENGINE=InnoDB '''
    )

dept_manager_create_sql = (
    ''' CREATE TABLE IF NOT EXISTS dept_manager (
            emp_no int NOT NULL,
            dept_no char(4) NOT NULL,
            from_date date NOT NULL,
            to_date date NOT NULL,
            PRIMARY KEY (emp_no,dept_no),
            KEY emp_no (emp_no),
            KEY dept_no (dept_no),
            CONSTRAINT dept_manager_ibfk_1 FOREIGN KEY (emp_no)  REFERENCES employees (emp_no) ON DELETE CASCADE,
            CONSTRAINT dept_manager_ibfk_2 FOREIGN KEY (dept_no) REFERENCES departments (dept_no) ON DELETE CASCADE
    ) ENGINE=InnoDB '''
    )

titles_create_sql = (
    ''' CREATE TABLE IF NOT EXISTS titles (
            emp_no int NOT NULL,
            title varchar(50) NOT NULL,
            from_date date NOT NULL,
            to_date date DEFAULT NULL,
            PRIMARY KEY (emp_no,title,from_date), KEY emp_no (emp_no),
            CONSTRAINT titles_ibfk_1 FOREIGN KEY (emp_no) REFERENCES employees (emp_no) ON DELETE CASCADE
    ) ENGINE=InnoDB '''
    )

create_queries = [employees_create_sql,
                  departments_create_sql,
                  salaries_create_sql,
                  dept_emp_create_sql,
                  dept_manager_create_sql,
                  titles_create_sql]

drop_queries = [employees_drop_sql,
                departments_drop_sql,
                salaries_drop_sql,
                dept_emp_drop_sql,
                dept_manager_drop_sql,
                titles_drop_sql]
