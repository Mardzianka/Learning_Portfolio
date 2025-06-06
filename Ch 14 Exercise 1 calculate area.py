#Program name: Ch 14 Exercise 1 calculate area.py

def circle(radius):
    area = 3.142 * radius
    return area
    
def rectangle(length,width):
    area = length * width
    return area

def menu():
    print("\nEnter 1 for circle, 2 for rectangle, 3 to quit: ")
    shape = input("What shape do you want to find the area for? ") 
    return shape

#main program
print("\nThe program will calculate the area of a shape")
shape = menu()
while shape != "3":    
    while shape not in ["1","2","3"]:
        print("Invalid answer")
        shape = menu() 
    if shape == "1":
        radius = float(input("Enter radius: "))
        area = circle(radius)
        print ("Area of circle is",area)
    elif shape == "2":
        length = float(input("Enter length: "))
        width = float(input("Enter width: "))
        area = rectangle(length,width)
        print ("Area of rectangle is",area)
    else:
        break
    shape = menu()
input("\nGoodbye.. press Enter to exit ")