import mysql.connector

mydb= mysql.connector.connect(host="localhost",user="root",passwd="7075737323",database="raja")

mycursor =mydb.cursor()

mycursor.execute("show databases")

for i in mycursor:
    print(i)

#OTHER METHOD

import mysql.connector

#establishing the connection
conn = mysql.connector.connect(user='root', password='7075737323', host='127.0.0.1', database='raja')

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Executing an MYSQL function using the execute() method
cursor.execute("Show DATABASES")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()
print("Connection established to: ",data)
