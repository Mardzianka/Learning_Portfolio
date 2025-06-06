#Program name: Ch 9 create or append to film file.py
#creates or appends to the film file films.txt file,
#which is in the same folder.


filmFile= open("films.txt", "a")
print("This program lets you write details of films to films.txt")
print("If the file does not exist, it will be created")
filmID = input("Enter film ID, xxx to end: ")

while filmID != "xxx":
    title = input ("Enter film title: ")
    yearReleased = input ("Enter year of release: ")
    rating = input ("Enter rating: ")
    duration =input ("Enter duration in minutes: ")
    genre = input ("Enter genre: ")
    filmFile.write(filmID + "," + title + "," + yearReleased + ","\
                   + rating + "," + duration + "," + genre + "\n")
    filmID = input("Enter film ID, xxx to end: ")
#endwhile
filmFile.close
print("file closed")
