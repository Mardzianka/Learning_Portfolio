#Program name: Ch 11 Example 4 print tblTemps.py
#Program prints records in tblTemps in database CityTemperatures.db
#in descending order of temperature
#It shows three ways of displaying the data

import sqlite3

conn = sqlite3.connect("CityTemperatures.db")
cursor = conn.cursor()

#This prints the data as a collection of tuples
for row in cursor.execute\
('SELECT * FROM tblTemps ORDER BY temperature DESC'):
   city, temperature, localTime = row 
   print(row)
print("\n\n")

#This prints the first five records with no formatting
for row in cursor.execute\
    ('SELECT * FROM tblTemps ORDER BY temperature DESC LIMIT 5'):
   city, temperature, localTime = row 
   print(city, temperature, localTime)
print("\n\n")

#This prints the data in neat columns   
#It also shows a different way of defining the for loop condition
#and the records are displayed in the sequence of city

#print headings
print("%-15s%20s%20s" %("City","Temperature","Local time"))
sql = cursor.execute('SELECT * FROM tblTemps ORDER BY city')

for row in sql:
#for row in cursor.execute('SELECT * FROM tblTemps  ORDER BY temperature DESC'):
   city, temperature, localTime = row 
   print ("%-15s %15d %20s" %(city, temperature, localTime))

input("\nPress Enter to exit: ")
