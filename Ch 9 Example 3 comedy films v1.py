#Program name: Ch 9 Example 3 comedy films v1.py
#program to read film file and print details of all comedy films

filmFile = open("films.txt","r")
filmRec = filmFile.readline()

while filmRec != "":
    field = filmRec.split(",")
    ID = field[0]
    title = field[1]
    rating = field[3]
    duration = int(field[4])
    genre = field[5]
    if genre == "Comedy\n":
        print(ID,title,rating,genre,duration)
    filmRec = filmFile.readline()
filmFile.close()
