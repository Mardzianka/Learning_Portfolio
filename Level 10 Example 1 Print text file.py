#Program name: Level 10 Example 1 print text file 
#reads records from a file named students1.txt and prints each record

studentFile = open("students1.txt","r")

for studentRec in studentFile:
    print(studentRec)
studentFile.close()
        
