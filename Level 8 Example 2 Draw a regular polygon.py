#Program name: Level 8 Example 2 Draw a regular polygon
import turtle

#Procedure to draw a regular polygon
def drawPolygon(sideLength, numSides):
    interiorAngle = (numSides - 2) * 180 / numSides
    turnAngle = 180 - interiorAngle

#clear the drawing canvas, send the turtle home
#and reset variables to default values
    turtle.reset()
    for n in range(numSides):
        turtle.forward(sideLength)
        turtle.right(turnAngle) 
#end of procedure

#main program
#This is where you would call the function
#Try Challenge 9
