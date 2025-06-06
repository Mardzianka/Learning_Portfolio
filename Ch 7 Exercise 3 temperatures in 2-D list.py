#Program name: Ch 7 Exercise 3.py

#Program prints the 6 months with the highest average maximum temperatures
# in descending order of maximum termperature

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

#sort in descending sequence on maximum temperature
tempsSorted = sorted(temps, key = lambda x:x[1],reverse = True)

#print headings
print("Month\t\tMax\tMin")
for month in range(6):
    print(tempsSorted[month][0],"\t",tempsSorted[month][1],"\t",tempsSorted[month][2])
    