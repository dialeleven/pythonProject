'''
https://www.w3schools.com/python/python_mysql_getstarted.asp


Install MySQL Driver

Python needs a MySQL driver to access the MySQL database.

In this tutorial we will use the driver "MySQL Connector".

We recommend that you use PIP to install "MySQL Connector".

PIP is most likely already installed in your Python environment.

Navigate your command line to the location of PIP, and type the following:

Download and install "MySQL Connector":

c:\python -m pip install mysql-connector-python
'''
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="test"
)

# select from database
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM item")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)


# INSERT into database
name = "Bob's Burgers"
quantity = 8

sql = "INSERT INTO item (name, quantity) VALUES (%s, %s)"
val = (name, quantity)
mycursor.execute(sql, val)
mydb.commit()

print(mycursor.rowcount, "record inserted.")


# JOIN example and multi line SQL using triple quotes
sql = '''SELECT a.id, email, type 
         FROM users AS a 
         INNER JOIN userTypes AS b ON a.userTypeId = b.id
         GROUP BY id
         ORDER BY email'''

mycursor = mydb.cursor()
mycursor.execute(sql)

# return all rows
result = mycursor.fetchall()

# return only ONE row
#result = mycursor.fetchone()


for x in result:
    print(x)


# DELETE example
sql = "DELETE FROM item WHERE name = %s"

# Tuple version: NOTE for a single value, we need the trailing comma to distinguish it 
# from a simple expression surrounded by parentheses
val = ("Bob's Burgers",)

# List version
val = ["Bob's Burgers"]

# val params can be of type list, tuple or dict
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, 'record(s) deleted')