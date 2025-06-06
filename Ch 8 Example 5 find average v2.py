#Program name: Ch8 Example 5 find average v2.py
#program finds average of three numbers input by the user

def findAverage(x,y,z):
    total = x + y + z
    average = total/3
    return average

def printHeading():
    print("This program uses a function", 
      "to find the average of 3 numbers\n")
    
def userInput():
    n1 = float(input("Enter first number: "))
    n2 = float(input("Enter second number: "))
    n3 = float(input("Enter third number: "))
    return n1, n2, n3

def printResult(answer):
   print("Average is ",answer)
   
#main program
printHeading()
num1, num2, num3 = userInput()
average = findAverage(num1, num2, num3)
printResult(average)

