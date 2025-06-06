#Program name: Ch 3 Exercise 1 area of square or rectangle.py
#Calculate area of shape

length = float(input("Enter length of rectangle: "))
width = float(input("Enter width of rectangle: "))
area = round(length*width,2)
if length == width:
    print("This is a square of area",area)
else:
    print("This is a rectangle of area",area)          
