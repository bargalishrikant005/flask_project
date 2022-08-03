""" After connecting to the MySQL server let’s see how to create
a MySQL database using Python.
For this, we will first create a cursor() object and will
then pass the SQL command as a string to the execute() method.
The SQL command to create a database is –

CREATE DATABASE DATABASE_NAME"""
# importing required libraries
import mysql.connector

dataBase = mysql.connector.connect(
host ="localhost",
user ="root",
passwd ="shrikant12345"
)

# preparing a cursor object
cursorObject = dataBase.cursor()

# creating database
cursorObject.execute("CREATE DATABASE products")
