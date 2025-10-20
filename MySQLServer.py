import mysql.connector

def create_database():
    try:
        # Connect to MySQL server
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Nonzillions1175",
            auth_plugin='mysql_native_password'
        )

        if mydb.is_connected():
            mycursor = mydb.cursor()
            # Create database if it doesn't exist
            mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as err:
        print(f"Error while connecting to MySQL: {err}")

    finally:
        # Safely close connections
        try:
            if mycursor:
                mycursor.close()
        except NameError:
            pass

        try:
            if mydb.is_connected():
                mydb.close()
                print("MySQL connection closed.")
        except NameError:
            pass


if __name__ == "__main__":
    create_database()
