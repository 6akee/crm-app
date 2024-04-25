import mysql.connector

database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'password123',
)

cursorObject = database.cursor()

cursorObject.execute("CREATE DATABASE elderco")

print("ALL DONE")