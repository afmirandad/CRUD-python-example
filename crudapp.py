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

# Method to insert a new salary registry
def create_salaries(connection, emp_no, salary, from_date, to_date):
    cursor = connection.cursor()
    query = "insert into salaries(emp_no, salary, from_date, to_date) values(%s,%s,%s,%s)"
    cursor.execute(query,(emp_no, salary, from_date, to_date))
    connection.commit()
    print(f"New salary for employee '{emp_no}' has been inserted.")

# Method to update a registry
def update_employee(connection, emp_no, salary, from_date, to_date):
    cursor = connection.cursor()
    query = """
    UPDATE salaries 
    SET salary = %s, from_date = %s, to_date = %s
    WHERE emp_no = %s
    """
    cursor.execute(query, (salary, from_date, to_date,emp_no))
    connection.commit()
    print(f"Employee {emp_no} updated successfully.")

# Method to delete an employee
def delete_employee(connection, emp_no):
    cursor = connection.cursor()
    query = "DELETE FROM salaries WHERE emp_no = %s"
    cursor.execute(query, (emp_no,))
    connection.commit()
    print(f"Employee {emp_no} deleted successfully.")

def main():
    connection = create_connection(config)

    # Calling method delete
    print("Delete employee")
    delete_employee(connection,999999)

    # Calling method create a new salary
    create_salaries(connection,999999,130000,'1985-10-20','1986-10-20')

    # Calling method read
    print("Read salaries upper 100000")
    read_salaries(connection)

    # Calling method update
    print("Update employee data")
    update_employee(connection,999999,130000,'1985-10-20','1986-10-20')

if __name__ == "__main__":
    main()