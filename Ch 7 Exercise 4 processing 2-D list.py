#Program name: Ch 7 Exercise 4 processing 2-D list.py

#Program prints a list of months in which
#average minimum temperature is below 15 degrees
#and a list of months in which
#average maximum temperature is 20 degrees or above degrees
temps =   [
                ["January  ",6,3],
                ["February ",7,3],
                ["March    ",10,4],
                ["April    ",13,6],
                ["May      ",17,9],
                ["June     ",20,12],
                ["July     ",22,14],
                ["August   ",21,14],
                ["September",19,12],
                ["October  ",14,9],
                ["November ",10,6],
                ["December ",7,3]
            ]
minMonths = []
maxMonths = []
for month in range(12):
    if temps[month][2] < 9:
        minMonths.append(temps[month])
    if temps[month][1] >=20:
        maxMonths.append(temps[month])
print("Months with average minimum temperatures < 9 degrees C")        
for m in range(len(minMonths)):
    print(minMonths[m][0],"\t",minMonths[m][1],"\t",minMonths[m][2],"\t")

print ("\nMonths with average maximum temperatures >= 20 degrees C")
for m in range(len(maxMonths)):
    print(maxMonths[m][0],"\t",maxMonths[m][1],"\t",maxMonths[m][2],"\t")
    
input("\nPress Enter to exit ")
