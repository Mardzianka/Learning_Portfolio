#Program name: Ch 11 Example 8 error trapping.py
#The user will enter new records to be added to the database Temperatures.db

import sqlite3

conn = sqlite3.connect("CityTemperatures.db")
cursor = conn.cursor()
myRec = []
city = input("\nEnter city name: ")

while city != "xxx":
    temperature = int(input ("Enter temperature: "))
    localTime = input ("Enter local time: ")
    myRec.append(city)
    myRec.append(temperature)
    myRec.append(localTime)
    try:
        cursor.execute("INSERT INTO tblTemps VALUES (?,?,?)",myRec)
        conn.commit()
    except:
        print ("\nA record for this city already exists")
    myRec = []
    city = input("\nEnter city name (xxx to end): ")
conn.close()

input("Press Enter to exit")
