#Program name: Ch 9 Example 4 read and print each  film record.py
# program reads the film.txt file and prints using For loop

filmFile = open("films.txt","r")
for row in filmFile:
    field = row.split(",")
    print(field[0], field[1],field[2],field[3],
          field[4],field[5],end ="")
filmFile.close()
