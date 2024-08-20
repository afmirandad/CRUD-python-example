#Libraries required
import mysql.connector
from mysql.connector import Error
from config import config

# Method that allow connect to MySQL Server
def create_connection(config):
    connection = None
    try:
        connection = mysql.connector.connect(**config)
        print("Connection has been successful!")
    except Error as e:
        print(f"This error '{e}'  occured")
    return connection

def main():
    connection = create_connection(config)

if __name__ == "__main__":
    main()