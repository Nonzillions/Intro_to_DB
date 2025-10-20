import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL server using mysql_native_password plugin
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Nonzillions1175",
            auth_plugin='mysql_native_password'
        )

        if mydb.is_connected():
            mycursor = mydb.cursor()
            mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")

    finally:
        if 'mycursor' in locals() and mycursor:
            mycursor.close()
        if 'mydb' in locals() and mydb.is_connected():
            mydb.close()
            print("MySQL connection closed.")

if __name__ == "__main__":
    create_database()