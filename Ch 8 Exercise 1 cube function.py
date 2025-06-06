#Program name: Ch 8 Exercise 1 cube function.py
#calls a function to return the surface area and volume of the cube

def cube(length):
    volume = length*length*length
    surfaceArea = 6 *(length*length)
    return volume, surfaceArea
    
#main program
side = float(input("Enter the length of the side of a cube in cm: "))
vol, area = cube(side)
print("\nVolume of cube is ",vol,"cu cm")
print("\nSurface area of cube is",area,"sq cm")