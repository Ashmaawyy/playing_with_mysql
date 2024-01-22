from mysql.connector import connect, Error
from sql_ddl import create_queries, drop_queries

def drop_database_tables_if_exist(cursor, connection):
    try:
        cursor.execute('SET foreign_key_checks = 0;')
        for query in drop_queries:
            cursor.execute(query)
            connection.commit()
        print('Dropped existing tables successfully : )')
        cursor.execute('SET foreign_key_checks = 1;')
        connection.commit()

    except SyntaxError as e:
        #todo develop error handling
        print('Failed dropping existing tables:\n{}'.format(e))
        exit(1)

def create_database_tables(cursor, connection):
    try:
        for query in create_queries:
            cursor.execute(query)
            connection.commit()
        print('Created database tables successfully : )')
    
    except Error as e:
        #todo develop error handling
        print('Failed creating tables:\n{}'.format(e))
        exit(1)

def main():
    db_creds = {
        'user':'root',
        'host': '127.0.0.1',
        'database': 'employees',
        'raise_on_warnings': True
    }

    try:
        connection = connect(**db_creds)
        print('Connected to mysql successfully ; )')
        
        cursor = connection.cursor()
        
        drop_database_tables_if_exist(cursor, connection)
        create_database_tables(cursor, connection)
        
        connection.commit()
        connection.close()

    except Error as e:
        #todo  develop error handling
        print(e)

if __name__ == '__main__':
    main()