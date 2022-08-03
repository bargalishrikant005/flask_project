"""Cursor is a Temporary Memory or Temporary Work Station.
It is Allocated by Database Server at
the Time of Performing DML(Data Manipulation Language) operations on Table by User.
Cursors are used to store Database Tables.
Creating Tables
For creating tables we will follow
the similar approach of writing
the SQL commands as strings and
then passing it to the execute() method of the cursor object.
SQL command for creating a table is –

CREATE TABLE
(
    column_name_1 column_Data_type,
    column_name_2 column_Data_type,
    :
    :
    column_name_n column_Data_type
);"""
# importing required libraries
import mysql.connector

dataBase = mysql.connector.connect(
host ="localhost",
user ="root",
passwd ="shrikant12345",
database = "products"
)

# preparing a cursor object
cursorObject = dataBase.cursor()

# creating table
studentRecord = """CREATE TABLE STUDENT (
				NAME VARCHAR(20) NOT NULL,
				BRANCH VARCHAR(50),
				ROLL INT NOT NULL,
				SECTION VARCHAR(5),
				AGE INT
				)"""

# table created
cursorObject.execute(studentRecord)

# disconnecting from server
dataBase.close()
