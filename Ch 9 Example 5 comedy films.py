#Program name: Ch 9 Example 5 comedy films.py
# program reads the film.txt file and prints all films of genre "Comedy"

filmFile = open("films.txt","r")
for row in filmFile:
    field = row.split(",")
    ID = field[0]
    title = field[1]
    yearReleased = field[2]
    rating = field[3]
    duration = int(field[4])
    genre = field[5]
#slice off the last character of genre
#as this is the newline character
    lastchar = len(genre)- 1
    genre = genre[0:lastchar]
    if genre == "Comedy":
        print(ID,title,yearReleased,rating,genre,duration)
filmFile.close()

input ("\nPress Enter to exit ")
