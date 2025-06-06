#Program name: Ch 11 Example 3 Populate tblTemps.py
#Program creates a table called tblTemps in database CityTemperatures.db
#It then adds temperatures for several cities to tblTemps

import sqlite3

conn = sqlite3.connect("CityTemperatures.db")
cursor = conn.cursor()

#create a table
cursor.execute("""CREATE TABLE tblTemps
                (city text,
                temperature integer,
                localTime text,
                PRIMARY KEY (city))
                """)

#insert multiple records
tblTemps = [('London',7,'1200'),
            ('Accra',30,'1200'),
            ('Baghdad',20,'1500'),
            ('Winnipeg',-12,'0600'),
            ('New York',14,'0700'),
            ('Nairobi',27,'1500'),
            ('Sydney',22,'2300')
            ]
cursor.executemany("INSERT INTO tblTemps VALUES (?,?,?)",tblTemps)

#save data to database
conn.commit()
conn.close()
print("Table successfully created")

