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

# Method to read salaries
def read_salaries(connection):
    cursor = connection.cursor()
    query = "select * from salaries where salary > 100000 limit 10"
    cursor.execute(query)
    salaries = cursor.fetchall()
    for salary in salaries:
        print("Salary: "+str(salary))

def main():
    connection = create_connection(config)

    # Calling method read
    print("Read salaries upper 100000")
    read_salaries(connection)

if __name__ == "__main__":
    main()