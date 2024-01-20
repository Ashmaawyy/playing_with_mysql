from configparser import ConfigParser
from mysql.connector import connect

config = ConfigParser()
config.read('creds.cfg')

connection = connect(**config)