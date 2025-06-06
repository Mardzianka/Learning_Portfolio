"""
Program name: Ch 11 Example 3 alternative solution.py
Creates a new database named CityTemperatures2.db
with an empty table named tblTemps

The with conn statement is also used in Ch 11 Example 9 
"""

import sqlite3

def create_table(dbname, sql):
    with sqlite3.connect(dbname) as db:
        cursor = db.cursor()
        cursor.execute(sql)

#main
#define structure of a table called tblTemps
#note the triple quotes used to maintain the formatting of the SQL statement

sql =   """
        create table tblTemps
        (
        cityName string,
        temperature integer,
        localTime string,
        primary key (cityName)
        )
        """

#name the database
dbname = "CityTemperatures2.db"

#call a function to execute the sql command,
#passing the database name and the sql as parameters
create_table(dbname,sql)

print("\ntblTemps created in new database " + dbname)
