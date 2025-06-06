#Program name: Ch 13 Exercise 3 print film database reports
#print a selection of reports
#These functions demonstrate different techniques of writing sql commands
#and printing formatted reports

import sqlite3
def displayMenu():

    choice = 0
    while choice not in ["1","2","3","4","5"]:
        print("\nOptions menu")
        print ("1. Print details of all films")
        print ("2. Print all films of a particular genre")
        print ("3. Print Film titles, ratings and genre sequenced by genre and rating")
        print ("4. Print details of all films released in 2016, sequenced by title")
        print ("5. Exit")
        choice = input ("\nEnter your choice: ")
        if choice not in ["1","2","3","4","5"]:
            print ("Invalid choice")
    return choice

#Option 1: Print details of all films
def option1Print(dbName):
    db = sqlite3.connect(dbName)
    cursor = db.cursor()
    sqlCommand = "SELECT * from tblFilms"
    print("\nHere are the records printed as tuples\n")
    for row in cursor.execute(sqlCommand):        
        #each record in the film table is a tuple       
        print(row)
        
    #Separate the fields and print neatly
    print("\nNow print the rows in neat columns\n")
    print ("ID \t Title\t\t\t\t\t Year   Rating  Duration Genre\n")
    for row in cursor.execute(sqlCommand):
        ID = row[0]
        title = row[1]
        #the next statement pads out the titles to 35 characters
        titleX = "{:<35}".format(title)
        yearReleased = row[2]
        rating = row[3]
        duration = int(row[4])
        genre = row[5]
        print(ID,"\t",titleX, "\t", yearReleased,"\t",rating, "\t",duration, "\t", genre)
    
    
#Option 2: Print all films of a particular genre
def option2Print(dbName):
    mygenre = input ("Enter genre, (Action, Animation, Fantasy, Comedy or Crime): ")
    mygenre = "'" + mygenre + "'"
    with sqlite3.connect(dbName) as db:
        cursor = db.cursor()
        selection = cursor.execute("SELECT * FROM tblFilms WHERE genre =" +  mygenre)
        for row in selection:
            print(row)
            
#to print neatly using formatted output:
        print("\n and nicely formatted in columns...")
        for row in cursor.execute("SELECT * FROM tblFilms WHERE genre =" +  mygenre):
            filmID,title,yearReleased,rating,duration,genre = row
            print("%-6s %-35s %6d %-6s %6d %12s" %(filmID,title,yearReleased,rating,duration,genre))    
    
#Option 3: Print Film titles, ratings and genre sequenced by genre and rating
def option3Print(dbName):
    with sqlite3.connect(dbName) as db:
        cursor = db.cursor()
        selection =cursor.execute("SELECT * from tblFilms ORDER BY genre, rating")
        for row in selection:
            print(row)
    
#Option 4: Print details of all films released in 2016, sequenced by title")
def option4Print(dbName):
    with sqlite3.connect(dbName) as db:
        cursor = db.cursor()
        cursor.execute("SELECT title, rating,genre from tblFilms")
        selection =cursor.execute("SELECT * from tblFilms WHERE yearReleased = 2016 ORDER BY title")
        for row in selection:
            print(row)
       
#main
dbName = "MyFilms.db"
menu = True

while menu == True:
    choice = displayMenu()
    if choice == "1":
        option1Print(dbName)
    elif choice == "2":
        option2Print(dbName)
    elif choice == "3":
        option3Print(dbName)
    elif choice == "4":
        option4Print(dbName)
    else:        
        menu = False
input("Press Enter to exit program")
    
