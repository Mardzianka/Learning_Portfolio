#Program name: Level 10 Example 1a Create students3 text file.py
#

studentFile = open("students3.txt","w")

#Accept data from user
moreStudents = True
while  moreStudents:
    surname = input("Enter surname, xxx to end: ")
    if surname == "xxx":
        moreStudents = False
    else:
        firstname = input("Enter firstname: ")
        gender = input("Enter 'M' or 'F': ")
        age = input("Enter age: ")
        studentFile.write(surname + "," + firstname + "," \
                             + gender + "," + age + "\n")
studentFile.close()
