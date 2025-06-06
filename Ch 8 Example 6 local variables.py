#Program name: Ch 8 Example 6 local variables.py
#program to illustrate use of local variables
def nameOne():
    myName = "Alice"
    print("In function nameOne, name = ", myName)

def nameTwo():
    myName = "Bob"
    print("In function nameTwo, name = ", myName)
    
#main program
myName = "Kumar"
print ("In main program, name = ", myName)
nameOne()
print ("In main program, name = ", myName)
nameTwo()
print ("In main program, name = ", myName)

