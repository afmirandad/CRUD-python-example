#Libraries required
import mysql.connector
from mysql.connector import Error

# Database configuration
config = {
    'host':'18.191.204.59',
    'user':'studentsucundi',
    'password':'mami_prende_la_radi0',
    'database':'employees'
}

# Method that allow connect to MySQL Server
def create_connection(config):
    connection = None
    try:
        connection = mysql.connector.connect(**config)
        print("Connection has been successful!")
    except Error as e:
        print(f"This error '{e}' occured")
    return connection
