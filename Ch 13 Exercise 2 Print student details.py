#Program name Ch 13 Exercise 2 Print student details.py
#retrieve a student's details from the database studentinfo.db

import sqlite3
conn = sqlite3.connect("studentinfo.db")
cursor = conn.cursor()

studentID = input("Enter user ID of student whose details you want to see: ")
#put quote marks around the user entry
studentID = "'" + studentID + "'"

for row in cursor.execute('SELECT * FROM tblStudent WHERE username =' + studentID):
    print (row)
