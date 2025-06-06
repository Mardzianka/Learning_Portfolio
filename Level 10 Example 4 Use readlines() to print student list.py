#Program name: Level 10 Example 4 Use readlines() to print student list
#<alist> = <fileid>.readlines()returns a list
#where each item is a line from the file

studentFile = open("students1.txt","r")

studentList = studentFile.readlines()
    
print("Print studentList")
print(studentList)

print("\n\nPrint each element of the list\n")

for nameString in studentList:
    print(nameString, end ="")
    
studentFile.close()
