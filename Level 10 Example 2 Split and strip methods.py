#Program name: Level 10 Example 2 split and strip methods
#reads every line from a file named students1.txt

studentFile = open("students1.txt","r")

for studentRec in studentFile:
#split the record into individual fields 
#comma is the field separator
    field = studentRec.split(",") 
    surname = field[0]
    firstname = field[1]
    gender = field[2]
    age = field[3]
#strip newline character from last field
    age = age.strip("\n")
    print(firstname,surname, "is", age, "years old")

studentFile.close()
