"""
Program name:Ch 5 Exercise 4 2-D temperatures.py
#program to allow the user to enter monthly average maximum
and minimum temperatures
Program finds and prints months with hooest average temperature
and coldest average temperature.
"""
monthName = ["January","February","March","April","May","June",\
         "July","August","September","October","November","December"]
monthlyAvg = []

for m in range(3):
    print("Enter average maximum and minimum for " + monthName[m])
    maximum = int(input("Maximum: "))
    minimum = int(input ("Minimum: "))
    row = [monthName[m], maximum, minimum]
    monthlyAvg.append(row)
#now print the list
print("\n")
for m in range (3):
    for index in range(3):
        print (monthlyAvg[m][index],end = " ")
    print("\n")
    
# Print the hottest and the coldest months
hottestTemp = -50
coldestTemp = 50
for m in range(3):
    month, maximum, minimum = monthlyAvg[m]
    if  maximum > hottestTemp:
        hottestTemp = maximum
        hottestMonth = month
    if  minimum < coldestTemp:
        coldestTemp = minimum
        coldestMonth = month
print("\nHottest month ", hottestMonth, "Maximum temperature ", hottestTemp)
print("Coldest month ",coldestMonth, "Minimum temperature ", coldestTemp)
