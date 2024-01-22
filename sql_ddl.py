employees = (
    ''' CREATE TABLE IF NOT EXISTS employees (
            emp_no int(11) NOT NULL AUTO_INCREMENT,
            birth_date date NOT NULL,
            first_name varchar(14) NOT NULL,
            last_name varchar(16) NOT NULL,
            gender enum('M','F') NOT NULL,
            hire_date date NOT NULL,
            PRIMARY KEY (emp_no)
    ) ENGINE=InnoDB
    ''')

departments = (
    ''' CREATE TABLE IF NOT EXISTS departments (
            dept_no char(4) NOT NULL,
            dept_name varchar(40) NOT NULL,
            PRIMARY KEY (dept_no), UNIQUE KEY dept_name (dept_name)
    ) ENGINE=InnoDB
    '''
    )

salaries = (
    ''' CREATE TABLE IF NOT EXISTS `salaries` (
            emp_no int(11) NOT NULL,
            salary int(11) NOT NULL,
            from_date date NOT NULL,
            to_date date NOT NULL,
            PRIMARY KEY (emp_no,from_date), KEY emp_no (emp_no),
            CONSTRAINT salaries_ibfk_1 FOREIGN KEY (emp_no) REFERENCES employees (emp_no) ON DELETE CASCADE
    ) ENGINE=InnoDB '''
    )

dept_emp = (
    ''' CREATE TABLE IF NOT EXISTS `dept_emp` (
            emp_no int(11) NOT NULL,
            dept_no char(4) NOT NULL,
            from_date date NOT NULL,
            to_date date NOT NULL,
            PRIMARY KEY (emp_no,dept_no), KEY emp_no (emp_no),
            KEY dept_no (dept_no),
            CONSTRAINT dept_emp_ibfk_1 FOREIGN KEY (emp_no) REFERENCES employees (emp_no) ON DELETE CASCADE,
            CONSTRAINT dept_emp_ibfk_2 FOREIGN KEY (dept_no) REFERENCES departments (dept_no) ON DELETE CASCADE
    ) ENGINE=InnoDB '''
    )

dept_manager = (
    ''' CREATE TABLE IF NOT EXISTS dept_manager (
            emp_no int(11) NOT NULL,
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

titles = (
    ''' CREATE TABLE IF NOT EXISTS `titles` (
            `emp_no` int(11) NOT NULL,
            `title` varchar(50) NOT NULL,
            `from_date` date NOT NULL,
            `to_date` date DEFAULT NULL,
            PRIMARY KEY (`emp_no`,`title`,`from_date`), KEY `emp_no` (`emp_no`),
            CONSTRAINT `titles_ibfk_1` FOREIGN KEY (`emp_no`) REFERENCES `employees` (`emp_no`) ON DELETE CASCADE
    ) ENGINE=InnoDB" '''
    )
