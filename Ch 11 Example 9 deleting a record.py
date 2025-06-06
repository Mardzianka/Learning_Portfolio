#Program name: Ch 11 Example 9 deleting a record.py

import sqlite3
def deleteRec(dbname):
    conn = sqlite3.connect (dbname)
    with conn:
        cursor = conn.cursor()
        myCity = input("Enter name of city to delete: ")
        keyfield = "'" + myCity + "'"
        cursor.execute("DELETE FROM tblTemps WHERE city =" + keyfield)
        #conn.commit() is not needed if the with statement is used

    for row in cursor.execute("SELECT * FROM tblTemps"):
        print (row)        
    
        
#main
deleteRec("cityTemperatures.db")
conn.close()
input ("\nPress Enter to exit: ")

