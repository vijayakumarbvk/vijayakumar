#!/usr/bin/env python3.7

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="Vijay@1234"
)

#print(mydb)
mycursor = mydb.cursor()
mycursor.execute("USE mydatabase")


sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)

mydb.commit()
