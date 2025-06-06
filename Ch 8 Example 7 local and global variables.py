#Program name: Ch 8 Example 7 local and global variables.py
#program to illustrate use of local and global variables
def nameOne():
    global myName
    print("In function nameOne, name = ", myName)
    myName = "Alice"
    print("In function nameOne, name = ", myName)

def nameTwo():
    myName = "Bob"
    print("in function nameTwo, name = ", myName)
    
#main program
myName = "Kumar"
print ("In main program, name = ", myName)
nameOne()
print ("In main program, name = ", myName)
nameTwo()
print ("In main program, name = ", myName)
