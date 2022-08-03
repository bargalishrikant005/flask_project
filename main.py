"""Python MySQL Connector is a Python driver that helps to integrate Python and MySQL.
This Python MySQL library allows the conversion between Python and MySQL data types.
MySQL Connector API is implemented using pure Python and does not require any third-party library.

 Installation : To install the Python-mysql-connector module,
 one must have Python and PIP, preinstalled on their system.
 If Python and pip are already installed type the below command in the terminal.
 pip install mysql-connector-python """

# importing required libraries
import mysql.connector

dataBase = mysql.connector.connect(
host ="localhost",
user ="root",
passwd ="shrikant12345"
)

print(dataBase)

# Disconnecting from the server
dataBase.close()
