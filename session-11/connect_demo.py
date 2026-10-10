import pymysql

connection = None

try:
    connection = pymysql.connect(
        host="localhost",
        user="root",
        password=""
    )

    print("Connection successful")

except pymysql.MySQLError as e:
    print("Connection failed:", e)

finally:
    if connection:
        connection.close()