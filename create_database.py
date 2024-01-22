from mysql.connector import connect, Error

db_creds = {
    'user':'root',
    'host': '127.0.0.1',
    'database': 'employees',
    'raise_on_warnings': True
}

try:
    connection = connect(**db_creds)
    print('Connected to mysql successfully ; )')

except Error as e:
    print(e)
