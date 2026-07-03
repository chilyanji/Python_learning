import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(
        host="localhost",        # MySQL server
        port=3306,               # Default MySQL port
        user="root",
        password="Aditya@123",
        database="chilyanji"
    )

    if connection.is_connected():
        print("Successfully connected to MySQL!")
        db_info = connection.get_server_info()
        print("MySQL Server version:", db_info)

except Error as e:
    print("Error while connecting to MySQL:", e)

finally:
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print("MySQL connection closed.")