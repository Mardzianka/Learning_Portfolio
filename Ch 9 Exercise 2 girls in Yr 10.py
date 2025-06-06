#Program name: Ch 9 Exercise 2 girls in Yr 10.py

studentFile = open("students.txt","r")
#print report heading
print("\nGirls in Year 10")
print("%-15s%-15s" %("Surname","First name"))

for studentRec in studentFile:
#    split record into comma-separated fields 
    field = studentRec.split(",")
    username = field[0]
    firstname = field[1]
    surname = field[2]
    gender = field[3]
    year = field[4]

    if year == "10" and gender =="F":
        print("%-15s%-15s" %(surname, firstname))

studentFile.close()
