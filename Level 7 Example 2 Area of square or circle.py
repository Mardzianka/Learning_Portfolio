#Program name: Level 7 Example 2 area of a square or circle
# Calls functions to calculate area of a square or circle
import math

def square(side):
    area = side * side
    return area

def circle(radius):
    area = math.pi * radius**2  
    return area

#main program
print("This program calculates the area of either a square or a circle\n")
myShape = input("Enter a shape, S for square or C for circle: ")
shape = myShape.upper()

#validate user input
while shape != "S" and  shape != "C":
    myShape = input("Please enter S or C: ")
    shape = myShape.upper()
    
# enter side or radius
if shape == "S":
    sideLength = float(input("Enter length of side: "))
    area = square(sideLength)       #this is a call statement
else:
    circleRadius = float(input("Enter radius: "))
    area = circle(circleRadius)     #this is another call statement

print("Area =",area)
