#Program name: Ch 11 Example 1 create films database v2.py
#In this version, the table is created in a function called from the main program
import sqlite3

def createTable(dbname, sql):
    connection = sqlite3.connect("MyFilms2.db")
    cursor = connection.cursor()
    cursor.execute(sql)
    connection.commit()
    connection.close()

#main
#create or open a database called Films.db with a SQLite DB
dbname = "MyFilms2.db"
#define table structure of a table called tblFilms in MyFilms.db
sqlCommand = """CREATE TABLE tblFilms
    (
    filmID text,
    title text,
    yearReleased integer,
    rating text,
    duration integer,
    genre text,
    primary key (filmID)
    )"""

#call the function create_table() to create the table in the database
createTable(dbname,sqlCommand)
        
print("tblFilms created in ", dbname)



