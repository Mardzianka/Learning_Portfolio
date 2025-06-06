#Program name: Ch 11 Example 6 print temps 25 or more.py
#program prints all records in  tblTemps in database CityTemperatures.db


import sqlite3

conn = sqlite3.connect("CityTemperatures.db")
cursor = conn.cursor()
sql = """
SELECT city, temperature
FROM tblTemps
WHERE temperature >= 25
ORDER BY temperature DESC
""" 
for row in cursor.execute(sql):
   city, temperature = row 
   print(row) 
