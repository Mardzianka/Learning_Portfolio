"""
Program name:Ch 5 Example 4 2-D list of temperatures.py
#program to allow the user to enter monthly average maximum
and minimum temperatures
"""
monthName = ["January","February","March","April","May","June",
         "July","August","September","October","November","December"]
monthlyAvg = []

for m in range(12):
    print("Enter average maximum and minimum for " + monthName[m])
    maximum = int(input("Maximum: "))
    minimum = int(input ("Minimum: "))
    row = [monthName[m], maximum, minimum]
    monthlyAvg.append(row)
#now print the list
print("\n")
for m in range (12):
    for index in range(3):
        print (monthlyAvg[m][index],end = " ")
    print("\n")
input("Press Enter to exit ")
