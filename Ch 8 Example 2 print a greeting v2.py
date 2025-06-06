#Program name: Ch 8 Example 2 print a greeting v2.py
"""
program to get name and print a greeting
#program passes the message as a paramenter
and returns the name entered,
which is used in the main program
"""

def getAndPrintName(message):
    """
    This function asks the user to enter their name,
    and then prints a greeting
    """
    name = input("Please enter your name: ")
    print (message,name)
    return name
    
playerName = getAndPrintName("Hello")
print(playerName, "is Player 1")