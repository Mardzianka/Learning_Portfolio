#Program name: Ch 11 Exercise 1 Print tblFilms.py
#program prints all records in  tblfilms in database MyFilms.db

import sqlite3

conn = sqlite3.connect("MyFilms.db")
cursor = conn.cursor()
for row in cursor.execute('SELECT * FROM tblFilms'):
   print (row)
