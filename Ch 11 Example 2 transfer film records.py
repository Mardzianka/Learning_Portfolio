#Program name: Ch 11 Example 2 transfer film records.py
#transfer records to film database from text file 
import sqlite3

#function to read text records and store in record filmDBRec[]
def readTextFile(filmFile):
    connection = sqlite3.connect('MyFilms.db')
    cursor = connection.cursor()
    numRecs = 0
    filmDBRec = []
    filmTextRec = filmFile.readline() 
    while filmTextRec != "":
        numRecs += 1
        field = filmTextRec.split(",")
        ID = field[0]
        title = field[1]
        yearReleased = field[2]
        rating = field[3]
        duration = int(field[4])
        genre = field[5]
        #strip off the newline character \n from genre
        lastchar = len(genre)- 1
        genre = genre[0:lastchar]
        print(ID, title,yearReleased,rating,duration,genre)

        #append fields to the list variable filmDBRec
        #to construct the record to be inserted
        filmDBRec.append(ID)
        filmDBRec.append(title)
        filmDBRec.append(yearReleased)
        filmDBRec.append(rating)
        filmDBRec.append(duration)
        filmDBRec.append(genre)
        #insert this record into the database
        #with sqlite3.connect('MyFilms.db') as db:
        #connection = sqlite3.connect('MyFilms.db')
        #cursor = connection.cursor()
        cursor.execute ("INSERT INTO tblFilms VALUES (?,?,?,?,?,?)", filmDBRec)
        connection.commit()            
 
        #empty the list of fields ready for next record
        filmDBRec = []
        #read the next record from the text file
        filmTextRec = filmFile.readline()
    #endwhile
    connection.close()
    return numRecs
#end function readTextFile
    

#main
filmFile = open("films.txt","r")
numRecs = readTextFile(filmFile)
print("\n",numRecs,"records transferred")
#close the text file
filmFile.close()
