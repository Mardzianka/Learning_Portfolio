#Program name: Ch 9 Exercise 3 student records in order of surname.py

studentFile = open("students.txt","r")
#print report heading
print("%-15s%-15s%-7s%+10s" %("Surname","First name", "Gender", "Year"))

studentTable = []
newStudentRec = []

for studentRec in studentFile:
#    split record into comma-separated fields 
    field = studentRec.split(",")
    username = field[0]
    firstname = field[1]
    surname = field[2]
    gender = field[3]
    year = field[4]

    #create new row to be appended to 2-D list of data
    newStudentRec.append(surname)
    newStudentRec.append(firstname)
    newStudentRec.append(gender)
    newStudentRec.append(year)

    studentTable.append(newStudentRec)
    #clear the row in the new table
    #ready to append the next row from the text file
    newStudentRec = []

    sortedTable = sorted(studentTable, key = lambda x: x[0])

for n in range(len(sortedTable)):
    print("%-15s%-15s%-7s%+10s" %(sortedTable[n][0],\
    sortedTable[n][1],sortedTable[n][2],sortedTable[n][3]))
    
    
