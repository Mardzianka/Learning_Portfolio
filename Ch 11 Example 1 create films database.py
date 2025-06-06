#Program name: Ch 11 Example 1 create films database.py
import sqlite3

#create or open a database called Films.db
connection = sqlite3.connect('MyFilms.db')
cursor = connection.cursor()

#SQL to create the table structure of tblFilms in MyFilms.db
sqlCommand = """
    CREATE TABLE tblFilms
    (
    filmID TEXT,
    title TEXT,
    yearReleased DATE,
    rating TEXT,
    duration INTEGER,
    genre TEXT,
    primary key (filmID)
    )"""

cursor.execute(sqlCommand)        
print("tblFilms created in MyFilms.db")

#The commit statement saves the changes to the database
connection.commit()
connection.close()
