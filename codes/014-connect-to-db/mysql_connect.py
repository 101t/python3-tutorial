#!/usr/bin/python3
import pymysql

db = pymysql.connect('localhost', 'root', 'YOUR_PASSWORD', 'DATABASE_NAME')

cursor = db.cursor()

cursor.execute("SELECT VERSION()")

data = cursor.fetchone()
print ("Database version : %s " % data)

db.close()
