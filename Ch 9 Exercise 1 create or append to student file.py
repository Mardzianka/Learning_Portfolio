#Program name: Ch 9 Exercise 1 create or append to student file.py
#The newline character is inserted into an extra field at the end of each record
#separated from the previous field by a comma

studentFile = open("students.txt","a")
username = input("Enter four-character student username: ")

while username!= "xxx":
    firstname = input("enter first name: ")
    surname = input("Enter surname: ")
    gender = input("Enter gender, M or F: ")
    year = input("Enter year, 7-13: ")
    studentRec = username +"," + firstname + "," + surname + \
                 "," + gender + "," + year + ",\n"
    print (studentRec)
    studentFile.write(studentRec)
    username = input("Enter four-character student username, xxx to end: ")

studentFile.close()
