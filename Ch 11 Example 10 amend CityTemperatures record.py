#Program name: Ch 11 Example 10 amend CityTemperatures record.py
import sqlite3

def amend():
#print the records before amendment
    with sqlite3.connect("CityTemperatures.db") as conn:
        cursor = conn.cursor()
        for row in cursor.execute('SELECT * FROM tblTemps'): 
            print (row)

        keyfield = input("Enter city name of the record to amend: ")

#       Put quote marks around city name, e.g. 'London'        
        keyfield = "'" + keyfield + "'"
        
        field = input("Change which field (temperature or localTime)? ")
        newvalue = input("Enter the new value for this field: ")

#       Validate the entry - temperature should be numeric or program will crash               
        try:         
            cursor.execute("UPDATE tblTemps SET " + field + "=" +  
                           newvalue + " WHERE city =" + keyfield) 
            print("\nRecord updated")
        except:
            print("\nNo record updated - invalid data entered")
        for row in cursor.execute('SELECT * FROM tblTemps'):
            print (row)

#main
amend()
