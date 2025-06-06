#Program name: Ch 8 Example 4 find average.py
#program finds average of three numbers input by the user

def findAverage(x,y,z):
    total = x + y + z
    average = total/3
    return average

#main program
print("""This program uses a function 
to find the average of 3 numbers \n""")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

result = findAverage(num1, num2, num3)
print("Average is ",result)


    
    
