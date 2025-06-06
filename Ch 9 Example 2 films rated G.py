#Program name: Ch 9 Example 2 split fields in film file.py
#Reads film file and print details of all films rated "G"

filmFile = open("films.txt","r")
filmRec = filmFile.readline()

while filmRec != "":
    field = filmRec.split(",")
    ID = field[0]
    title = field[1]
    rating = field[3]
    duration = int(field[4])
    genre = field[5]
    if rating == "G":
        print(ID,title,rating,duration)
    filmRec = filmFile.readline()
filmFile.close()
