#Program name: Ch 9 Example 1 read film file.py
#program to read a text file and print all records

filmFile = open("films.txt","r")
films = filmFile.read()
print(films)
filmFile.close()
 
