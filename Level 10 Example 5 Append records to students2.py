#Program name: Level 10 Example 5 Append records to students2
#appends  records to students2.txt
#This is a copy of the original students1.txt

studentFile = open("students2.txt","a")

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
