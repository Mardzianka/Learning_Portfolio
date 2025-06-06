#Program name: Level 10 Example 3 Use readline() to read and print male students

#read records from a file named students1.txt
studentFile = open("students1.txt","r")

#Print all male students
endOfFile = False
while not endOfFile:
    studentRec = studentFile.readline()
    #returns an empty string on the end of file
    if studentRec == "":
        endOfFile = True
    else:
        #split the record into individual fields 
        #comma is the field separator
        fieldList = studentRec.split(",") 
        surname = fieldList[0]
        firstname = fieldList[1]
        gender = fieldList[2]
        age = fieldList[3]
        #select male students
        if gender == "M":   
            print(surname, firstname,gender,age, end = "")
         
studentFile.close()
