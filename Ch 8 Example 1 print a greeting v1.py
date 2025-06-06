#Program name: Ch 8 Example 1 print a greeting v1.py
#program to get name and print a greeting

def getAndPrintName():
    """
    This function asks the user to enter their name,
    and then prints a greeting
    """
    name = input("Please enter your name: ")
    print ("Hello",name)
    
getAndPrintName()