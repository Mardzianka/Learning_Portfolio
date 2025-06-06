#Program name: Level 7 Example 7 (extra) Using global keyword 
#defining a global keyword variable

# thirdMusketeer is defined in the main program and by default is global
#and can be used in any subroutine

def printGlobalName():    
    print("Third musketeer: " + thirdMusketeer)
#end function


def defineFourthMusketeer():
    global newName
    newName = "D'Artagnan"

    
thirdMusketeer = "Aramis"
printGlobalName()
defineFourthMusketeer()
print("The fourth musketeer is", newName)
